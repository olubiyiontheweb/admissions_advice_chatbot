'''
    Project Name: Admissions Advice Webscraping Tool
    Description: Crawls and retrieves course and faculty lists and their individual 
                details from university website and exports them as a JSON for 
                easy accessibility by the Admissions Advice chatbot.
    Author: Oluwatosin Olubiyi
    Website: http://olubiyiontheweb.com/
'''

# Imports all custom functions for the scraping operation
from web_scrapers import (
    hull_website_url as hull_url,
    web_scraper_all,
    web_scraper_with_class,
    web_scraper_all_with_class,
    web_scraper_from_content,
    web_scraper_from_content_class,
    web_scraper_all_from_content,
    web_scraper_all_from_content_class,
)


# get list of all available courses on the University's website, 
# undergraduate and postgraduate (taught and research)
# "https://www.hull.ac.uk/study
url = hull_url + "/study"
sections = web_scraper_all(url, 'section')

course_list = []
intake = []

# traverse through the html elements and extract course details
for section in sections:
    level = web_scraper_from_content_class(section, 'h2', 'heading-style')
    courses = web_scraper_all_from_content(section, 'a')
    
    if level:
        for course in courses:            
            url = hull_url + course.get('href')
            fees_element, page_content = web_scraper_with_class(url, 'div', 'standard-fees')
            
            start_dates = web_scraper_from_content_class(page_content, 'div', 'start')
            if start_dates:
                dates = web_scraper_all_from_content(start_dates, 'label')
                for date in dates:
                    intake.append(date.get_text().strip())
                
            if fees_element:
                home_fee = web_scraper_from_content_class(fees_element, 'div', 'home')
                if home_fee:
                    home_fee = web_scraper_from_content(home_fee, 'p')
                
                international_fee = web_scraper_from_content_class(fees_element, 'div', 'international')
                if international_fee:
                    international_fee = web_scraper_from_content(international_fee, 'p')
                    
            current_course = {
                'level': level.get_text().strip(), 
                'course': course.get_text().strip(),
                'home_fee': home_fee.get_text().strip() if home_fee else None,
                'international_fee': international_fee.get_text().strip() if international_fee else None,
                'url': course.get('href'),
                'intake': intake}
            
            course_list.append(current_course)
            
            # print status of scraping operation
            print("Course {0} Completed: ".format(len(course_list)), current_course)
            
            # reset all variables, before moving to the next course
            intake.clear()
            international_fee = None
            home_fee = None



#________________________________________________________________________
# get list of departments
url = hull_url +"/faculties"
divs = web_scraper_all_with_class(url, 'div', 'thirds')

faculties = []
for element in divs:
    link = web_scraper_all_from_content_class(element, 'a', 'image')
    link = link[0].get('href')
    for j in web_scraper_all_from_content(element, 'div'):
        faculty = j.get_text().strip()
        data = {'name': faculty, 'url': link}
        
        ## append a dictionary with faculty name and link to their page
        faculties.append(data)
        
        print("Faculty {0} Completed: ".format(len(faculties)), data)        
        


#________________________________________________________________________
# Write the scraped course and faculty details to a file.

# Write course information to file
file = open("hull_courses.json", "w")
file.write(course_list.__str__())
file.close()

# Write faculty information to file
file = open("hull_faculties.json", "w")
file.write(faculties.__str__())
file.close()