import requests
from bs4 import BeautifulSoup

url = "https://www.gasbuddy.com/USA"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("div", "col-sm-6 col-xs-6 siteName")
tests = soup.find_all("div", "col-sm-2 col-xs-3 text-right")

newDict = {}
for i in range(len(links)):
	link = links[i]
	test = tests[i]
	newDict[str(link.contents[0].strip())] = str(test.contents[0].strip())


print(newDict)