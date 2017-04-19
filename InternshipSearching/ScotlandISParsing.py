from bs4 import BeautifulSoup
import requests

URL = 'http://www.scotlandis.com/digitaltech2017/digitaltech2017-shortlist/'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(response.content, 'lxml')

unordered_lists = soup.find_all('ul', class_=None)

companies = set()

for ul in unordered_lists:
    list_items = ul.find_all('li')

    if len(list_items) <= 3:

        for li in list_items:
            if len(li.find_all('a')) == 0:
                companies.add(li.text)


with open('companies', 'w') as company_list_file:
    for company in companies:
        company_list_file.write('{0} \n'.format(company))
