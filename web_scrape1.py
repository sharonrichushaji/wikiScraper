from bs4 import BeautifulSoup
#from urllib3 import urljoin
import requests

search_input = "India"
url = "https://en.wikipedia.org/wiki/Lilly_Singh"
#page = requests.post(url, data = search_input)
page = requests.post(url)
print(page)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('h1', class_="firstHeading").get_text())
#full_body = soup.find('div', class_="mw-parser-output").get_text()
#print(soup.find('p', full_body[10]))
#print(soup.prettify())
#print(list(soup.children))
#print(full_body)
#print(soup.find('div', class_="noprint").get_text())
#nav = soup.find('div', id="simpleSearch")
#nav.searchInput = input()
#print(page.json())
str_add = raw_input("Search Wikipedia: ")
list1 = list(str_add)
for i in range(0,50):
	if list1[i] == " ":
		list1[i] = "%20"
		print(list1)
	else:
		break
str_add = ''.join(list1)
search_url = "https://en.wikipedia.org/w/index.php?search=%20&title=Special%3ASearch"
search_url1 = search_url[:44] + str_add + search_url[44:]
page1 = requests.get(search_url1)
print(page1)
soup = BeautifulSoup(page1.content, 'html.parser')

print(soup.find('h1', class_="firstHeading").get_text())
full_body = soup.find('div', class_="mw-parser-output").get_text()
print(full_body)