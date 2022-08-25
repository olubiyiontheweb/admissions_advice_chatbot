from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
import time

hull_website_url = 'https://www.hull.ac.uk'

def web_scraper(url: str, element: str):
    """
    Scrape the web page for the specified element.
    """
    # delay the requests for 5 seconds to avoid being blocked
    time.sleep(5)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    if soup:
        return soup.find(element), page.content
    return None, page.content

def web_scraper_with_class(url: str, element: str, class_name: str):
    """
    Scrape the web page for the specified element and classname.
    """
    # delay the requests for 5 seconds to avoid being blocked
    time.sleep(5)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    if soup:
        return soup.find(element, class_=class_name), soup
    return None, page.content

def web_scraper_all(url: str, element: str):
    """
    Scrape the web page for the specified element.
    """
    # delay the requests for 5 seconds to avoid being blocked
    time.sleep(5)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    if soup:
        return soup.find_all(element)
    return None

def web_scraper_all_with_class(url: str, element: str, class_name: str):
    """
    Scrape the web page for the specified element and classname.
    """
    # delay the requests for 5 seconds to avoid being blocked
    time.sleep(5)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    if soup:
        return soup.find_all(element, class_=class_name)
    return None

# scrape from page content recursively with given elements and class names
def web_scraper_from_content(content: str, element: str):
    """
    Scrape the web page for the specified element.
    """
    return content.find(element)

def web_scraper_from_content_class(content: BeautifulSoup, element: str, class_name: str):
    """
    Scrape the web page for the specified element and classname.
    """
    return content.find(element, class_=class_name)

def web_scraper_all_from_content(content: BeautifulSoup, element: str):
    """
    Scrape the web page for the specified element.
    """
    return content.find_all(element)
    
def web_scraper_all_from_content_class(content: BeautifulSoup, element: str, class_name: str):
    """
    Scrape the web page for the specified element and classname.
    """    
    return content.find_all(element, class_=class_name)

def map_fac_to_course(course_list: list, course_urls: list, f_name: str, f_url: str):
    """
    Map faculty to their courses.
    """
    for course in course_list:
        if course["url"] in course_urls:
            course["faculty"] = f_name
            course["faculty_url"] = f_url
        else:
            course["faculty"] = ""
            course["faculty_url"] = ""
        
    return course_list