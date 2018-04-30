"""
Author: Yi Li
Time: May 30, 2017

"""

from bs4 import BeautifulSoup
import requests



with open("harvard_extension2.txt", "w", encoding="utf-8") as f:     # raw_unicode_escape
    f.write('course_name' + '|' + 'professor' + '|' + 'url' + '|' + 'description' + '|' + 'term' + '|' + 'online' + '|' + 'course_num' + "\n")
    for i in range(1, 44):
        start_url = "https://www.extension.harvard.edu/academics/courses/course-catalog?search_api_views_fulltext=&page=" + str(i)
        resp = requests.get(start_url) #.content.decode()
        soup = BeautifulSoup(resp.content, "html.parser")
        # print(soup)

        for title in soup.find_all("td", class_="views-field views-field-field-course-display-name"):   #.get_text()
            # print(title)
            try:
                course_name = title.find("a").get_text()
                print(course_name)
                professor = title.find("p").get_text()
                print(professor)

                url = title.find("a", href=True)
                print(url['href'])
                resp2 = requests.get(url['href'])
                soup2 = BeautifulSoup(resp2.content, "html.parser")
                description = soup2.find_all("div", class_="pane-content")[2].get_text()
                description = description.strip()
                print(description)

                term = title.find_next("td", class_="views-field views-field-field-term-display-name").get_text()
                term = term.strip()
                print(term)

                online = title.find_next("td", class_="views-field views-field-field-course-format").get_text()
                online = online.strip()
                print(online)

                course_num = title.find_next("td", class_="views-field views-field-field-crn").get_text()
                course_num = course_num.strip()
                print(course_num)

                f.write(course_name + '|' + professor + '|' + url['href'] + '|' + description + '|' + term + '|' + online + '|' + course_num + "\n")
            except:
                pass


