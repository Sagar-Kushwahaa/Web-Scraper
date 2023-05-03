from bs4 import BeautifulSoup
from sys import argv
import requests

userName = argv[1]
GITHUB_URL = f'https://github.com/{userName}?tab=repositories'

response=requests.get(GITHUB_URL).text
soup=BeautifulSoup(response,'html.parser')
try:
    noOfRepos=soup.find('span',class_='Counter').text
except(AttributeError):
    print(f"Your given user {[userName]} does not exist!!!")
else:
    print(noOfRepos)
