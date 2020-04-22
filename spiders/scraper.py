from bs4 import BeautifulSoup
from requests import session
import json
from setting import payload

url = "https://sia.mercubuana-yogya.ac.id/"

with session() as req:
    req.post(url + "gate.php/login", data=payload())
    request = req.get(url + "akad.php/biomhs/jadwal")
    # print(request.headers)
    soup = BeautifulSoup(request.text, 'lxml')


def getCourse():
    courses = {}
    courses["results"] = []
    table = soup.find("table", attrs={"class": "table table-striped table-condensed"})

    for columns in table.tbody.find_all("tr"):
        rows = columns.find_all("td")
        results = {
            "courseId": rows[0].text,
            "courseDay": rows[1].text,
            "courseStart": rows[2].text,
            "courseEnd": rows[3].text,
            "courseCode": rows[4].text,
            "courseName": rows[5].text,
            "courseClass": rows[6].text,
            "courseLecturer": rows[7].text,
            "courseRoom": rows[8].text
        }
        courses["results"].append(results)
        
    with open('results.json', 'w') as outfile:
        json.dump(courses, outfile, indent=4)
        

getCourse()