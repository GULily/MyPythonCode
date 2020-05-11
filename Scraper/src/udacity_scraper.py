"""
Author: Yi Li
Time: May 31, 2017

"""

from bs4 import BeautifulSoup
import requests

start_url = 'https://www.udacity.com/courses/all'
resp = requests.get(start_url)  # .content.decode()
soup = BeautifulSoup(resp.content, "html.parser")
# print(soup)

with open("data/udacity_courses.txt", "w", encoding="utf-8") as f:
    f.write('course_name' + '|' + 'url' + '|' + 'level' + '|' + 'description' + '\n')
    for title in soup.find_all("h3", class_="h-slim"):   #.get_text()
        # print(title)
        try:
            course_name = title.find("a").get_text()
            course_name = course_name.strip()
            print(course_name)

            url = title.find("a", href=True)
            url = 'https://www.udacity.com' + url['href']
            print(url)

            level1 = title.find_next("div", class_="col-sm-4 hidden-xs")
            level = level1.get_text().strip()
            print(level)

            # bookmark_count = level1.find_next("span", class_="count").get_text()
            # print(bookmark_count)

            description = level1.find_next("div").get_text()  # "data-course-short-summary"
            description = description.strip()
            description = description.strip('\n')
            print(description)

            f.write(course_name + '|' + url + '|' + level + '|' + description + "\n")
        except:
            pass




