import requests
from bs4 import BeautifulSoup

url = "https://www.hull.ac.uk/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# scrape only sections with course, admissions, and finance information
file = open("hull_courses.txt", "w")
file.write(soup.find_all('div', class_='study')[0].get_text())
file.close()