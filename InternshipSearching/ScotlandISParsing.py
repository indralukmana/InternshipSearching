from bs4 import BeautifulSoup
import requests

URLS = ['http://www.scotlandis.com/digitaltech2017/digitaltech2017-shortlist/',
        'http://www.scotlandis.com/digitaltech2017/2016-nominees/']
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Make company variable as set, because just need unique company name
companies = set()

for URL in URLS:
    # make a request and read the html tags of the contents
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')

    # get all elements that contain unordered list of companies
    unordered_lists = soup.find_all('ul', class_=None)

    for ul in unordered_lists:
        list_items = ul.find_all('li')

        if len(list_items) <= 3:

            for li in list_items:
                if len(li.find_all('a')) == 0:
                    company_name = li.text.replace(' > WINNER', '')
                    companies.add(company_name)

with open('companies', 'w') as company_list_file:
    for company in companies:
        company_list_file.write('{0} \n'.format(company))
