from bs4 import BeautifulSoup
import requests
import re

url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
list_of_data = []
list_of_states =[]
res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')

#extract all lists of data
for items in soup.find('table', class_='wikitable sortable plainrowheaders').find_all('tr')[2::]:
    data = str(items.find_all(['th', 'td']))
    list_of_data.append(data)

#use regex to extract the name and add to file
states_file = open("states_file.txt", "w+")
for row in list_of_data:
    # result = re.search(r'title=(\"(.*)\">)([a-z, A-z]*)', row)
    result = re.search(r'title=\"([A-Z a-z]*)', row)
    list_of_states.append(result.group(1))
    # list_of_states.append(result.group(2))
    states_file.write(result.group(1) + "\n")
states_file.close()

print(list_of_states)
print(len(list_of_states))





