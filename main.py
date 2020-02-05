import requests
import json
import html
import webbrowser
from bs4 import BeautifulSoup

url = "https://www.twitter.com"
response = requests.get(url)

if response.status_code == 200:
	print('Sucesss!')
	print('Parsing data ...')
	#print(response.text)
	#file = open("twitter.html","w",encoding="utf8")
	#file.write(response.text)
	#file.close()
	soup = BeautifulSoup(response.text,"html.parser")
	escapedJson = soup.find_all(id="init-data")
	for data in escapedJson:
		jsonString = json.loads(html.unescape(data.get('value').replace("\\/", "/")))
	htmlData = "<html><body><center><h1>Twitter Avtars</h1>"
	for key,value in jsonString['activeHashflags'].items():
		htmlData += '<h6>' + key + '</h6><img src = "'+ value +'">'
else:
	print('Failed to fetch response for' + url)

file = open("twitter.html","w",encoding="utf8")
file.write(htmlData+"</center></body></html>")
file.close()
webbrowser.open('twitter.html', new=2)