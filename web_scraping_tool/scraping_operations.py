"""
    Project Name: Admissions Advice Webscraping Tool
    Description: Crawls and retrieves course and faculty lists and their individual 
                details from university website and exports them as a JSON for 
                easy accessibility by the Admissions Advice chatbot.
    Author: Oluwatosin Olubiyi
    Website: http://olubiyiontheweb.com/
"""

# Imports all custom functions for the scraping operation
from ntpath import join
from web_scrapers import (
    hull_website_url as hull_url,
    map_fac_to_course,
    web_scraper_all,
    web_scraper_with_class,
    web_scraper_all_with_class,
    web_scraper_from_content,
    web_scraper_from_content_class,
    web_scraper_all_from_content,
    web_scraper_all_from_content_class,
)


# get list of all available courses on the University"s website, 
# undergraduate and postgraduate (taught and research)
# "https://www.hull.ac.uk/study
url = hull_url + "/study"
sections = web_scraper_all(url, "section")

course_list = []
intake = []

# traverse through the html elements and extract course details
for section in sections:
    level = web_scraper_from_content_class(section, "h2", "heading-style")
    courses = web_scraper_all_from_content(section, "a")
    
    if level:
        level = level.get_text().strip()
        for course in courses:
            url = hull_url + course.get("href")
            
            # reset all variables, before moving to the next course
            intake.clear()
            international_fee = ""
            home_fee = ""
            
            # get undergraduate course details
            if level == "Undergraduate":
                fees_element, page_content = web_scraper_with_class(url, "div", "standard-fees")
            
                start_dates = web_scraper_from_content_class(page_content, "div", "start")
                if start_dates:
                    dates = web_scraper_all_from_content(start_dates, "label")
                    for date in dates:
                        intake.append(date.get_text().strip())
                
                if fees_element:
                    home_fee = web_scraper_from_content_class(fees_element, "div", "home")
                    if home_fee:
                        home_fee = web_scraper_from_content(home_fee, "p")
                        home_fee = home_fee.get_text().strip()
                    
                    international_fee = web_scraper_from_content_class(fees_element, "div", "international")
                    if international_fee:
                        international_fee = web_scraper_from_content(international_fee, "p")
                        international_fee = international_fee.get_text().strip()
            
            # get postgraduate taught courses
            elif "Taught" in level:
                try:
                    fees_element, page_content = web_scraper_with_class(url, "section", "fees")                           
                    fees_element = web_scraper_from_content_class(fees_element, "div", "whole") 
                    fees_element = web_scraper_all_from_content(fees_element, "li")     

                    for fee in fees_element:                        
                        if "Home" in fee.get_text():
                            try:
                                home_fee = fee.get_text().split()[1]
                            except:
                                home_fee = fee.get_text().strip()                   
                        
                        if "International" in fee.get_text():                                
                            try:
                                international_fee = fee.get_text().split()[1]
                            except:
                                international_fee = fee.get_text().strip()
                        
                except Exception as e:
                    pass
                
            # get research programme details
            else:
                try:
                    fees = []
                    fees_element, page_content = web_scraper_with_class(url, "section", "fees")
                    fees_element = web_scraper_from_content_class(fees_element, "div", "whole")
                    fees_element = web_scraper_all_from_content(fees_element, "p")               
                
                    for fee in fees_element:
                        if "time" in fee.get_text():
                            try:
                                fees.append(fee.get_text().split(":")[1])
                            except:
                                pass
                        
                    international_fee = fees[-1]
                    fees.remove(international_fee)
                    home_fee = ", ".join(fees)
                    
                except Exception as e:
                    pass
                    
            current_course = {
                "level": level, 
                "course": course.get_text().strip(),
                "home_fee": home_fee,
                "international_fee": international_fee,
                "url": course.get("href"),
                "intake": ", ".join(intake)}
            
            course_list.append(current_course)
            
            # print status of scraping operation
            print("Course {0} Completed: ".format(len(course_list)), current_course)


#________________________________________________________________________
# get list of departments
url = hull_url +"/faculties"
divs = web_scraper_all_with_class(url, "div", "thirds")

count = 1
for element in divs:
    link = web_scraper_all_from_content_class(element, "a", "image")
    link = link[0].get("href").strip()    
    for faculty in web_scraper_all_from_content(element, "div"):
        faculty_name = faculty.get_text().strip()
        
        # get courses url for mapping on the faculty page
        try:
            course_element = web_scraper_all_with_class(hull_url + link, "a", "course")            
            course_urls = []
            for course in course_element:
                course_urls.append(course.get("href").strip())
            
            course_list = map_fac_to_course(course_list, course_urls, faculty_name, link)
        except Exception as e:
            pass
        
        print("Faculty {0} Completed: ".format(count), {"name": faculty_name, "url": link})   
        
        count +=1


#________________________________________________________________________
# Write the scraped course and faculty details to a file.

# Write course information to file
file = open("hull_courses_faculties.json", "w")
file.write(course_list.__str__())
file.close()