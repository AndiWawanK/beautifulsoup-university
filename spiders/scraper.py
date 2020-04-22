from bs4 import BeautifulSoup
from requests import session

payload = {
    "act": "login",
    "username": "17111066",
    "password": "13111998"
}
url = "https://sia.mercubuana-yogya.ac.id/"

with session() as req:
    req.post(url + "gate.php/login", data=payload)
    request = req.get(url + "akad.php/biomhs/jadwal")
    # print(request.headers)
    soup = BeautifulSoup(request.text, 'lxml')


def getmatkul():
    table = soup.find('table', class_='table table-striped table-condensed')
    for column in table.find_all('tr'):
        rows = column.find_all('td')
        # print(rows[0].text)
        for results in rows:
            print(results.text)

getmatkul()