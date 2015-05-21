import urllib2
import requests
from bs4 import BeautifulSoup

def download(download_url,file_name):
	file_name = check(file_name)
	response = urllib2.urlopen(download_url)
	file = open(file_name+".pdf", 'w')
	file.write(response.read())
	file.close()
	print file_name + "Downloaded"

def check(file_name):
	file_name = file_name.replace("?","")
	file_name = file_name.replace("<","")
	file_name = file_name.replace(">","")
	file_name = file_name.replace("/","")
	file_name = file_name.replace(":","")
	file_name = file_name.replace("|","")
	file_name = file_name.replace("%20"," ")
	file_name = file_name.replace("+","")
	return file_name
	
print 'Enter the course number whose content you wish to download:'
courseNum = raw_input()
courseNum = courseNum.lower()

url  = 'https://sites.google.com/a/mitr.iitm.ac.in/iitmcivil/'
courseUrl = url + courseNum

resp = requests.get(courseUrl)

soup = BeautifulSoup(resp.content)

for link in soup.find_all('a'):
	if link.text == 'Download':
		download_url = "https://sites.google.com"+link.get('href')[:link.get('href').find('?')]
		file_name = link.get('href')[link.get('href').find(courseNum)+7:link.get('href').find(".pdf")]
		download(download_url,file_name)


