import html5lib
import requests
import re
from bs4 import BeautifulSoup

class IMDB:
	baseUrl = "http://www.imdb.com/"
	titleUrl = baseUrl+"title/"
	searchUrl = baseUrl+"find?s=all&q="
	creditsPath = 'fullcredits/'

	#############################
	'''get Ratings only STARTS'''
	#############################

	def getRating(self, title):
		return IMDB.getRatingByImdbId(self, IMDB.getIdFromName(title))

	def getRatingByImdbId(self, title):
		return re.sub('\s+', '', IMDB.parseHTML(IMDB.scrapSite(IMDB.titleUrl+title+"/"), 'div', 'class', 'ratingValue').strong.span.text)

	###########################
	'''get Ratings only ENDS'''
	###########################

	'''--------------------------------------------------------------------'''

	#############################
	'''get Summary only STARTS'''
	#############################

	def getSummary(self, title):
		return IMDB.getSummaryByImdbId(self, IMDB.getIdFromName(title))

	def getSummaryByImdbId(self, title):
		return (re.sub(r'[\t\r\n]', '', (IMDB.parseHTML(IMDB.scrapSite(IMDB.titleUrl+title+"/"), 'div', 'class', 'summary_text').text))).strip()

	#############################
	'''get Summary only ENDS'''
	#############################

	'''--------------------------------------------------------------------'''

	#############################
	'''get Director only STARTS'''
	#############################

	def getDirector(self, title):
		return IMDB.getDirectorByImdbId(self, IMDB.getIdFromName(title))

	def getDirectorByImdbId(self, title):
		return re.sub('\s+', '', IMDB.parseHTML(IMDB.scrapSite(IMDB.titleUrl+title+"/"), 'span', 'itemprop', 'director').a.span.text)

	#############################
	'''get Director only ENDS'''
	#############################

	'''--------------------------------------------------------------------'''

	#############################
	'''get Casting only STARTS'''
	#############################

	def getCasting(self, title, length=10, all=False):
		return IMDB.getCastingByImdbId(self, IMDB.getIdFromName(title), length=length, all=all)

	def getCastingByImdbId(self, title, length=10, all=False):
		soup = IMDB.parseHTML(IMDB.scrapSite(IMDB.titleUrl+title+"/"+IMDB.creditsPath), 'table', 'class', 'cast_list')
		castList = []
		counter = 0;
		for tr in soup.find_all('tr'):
			tds = tr.find_all('td')
			if len(tds) > 2:
				castList.append(re.sub(r'[\t\r\n]', '', "".join(tds[1].find_all(text=True))).strip() +" AS "+ re.sub(r'[\t\r\n]', '', "".join(tds[3].find_all(text=True))).strip())
				if not all:
					counter+=1;
					if counter == 10:
						break;
		return castList;

	#############################
	'''get Casting only ENDS'''
	#############################

	'''--------------------------------------------------------------------'''

	def parseHTML(soup, ele, idType, idValue):
		try:
			return soup.find( ele, {idType:idValue})
		except Exception:
			print("Sorry an error accured cant get data extracted")
		return ""

	def getIdFromName(title):
		try:
			soup = IMDB.scrapSite(IMDB.searchUrl+title)
			movie = soup.find('td',{'class':'result_text'}).a
			print("Movie: "+movie.text)
			return movie['href'].split('/')[2]
		except Exception:
			print("Sorry an error accured cant get data extracted")
		
		return ""

	def scrapSite(url):
		try:
			resp = requests.get(url)
			return BeautifulSoup(resp.text, "html5lib")
		except Exception:
			print("Problem with the network connection, please check your wifi or lan connection")
