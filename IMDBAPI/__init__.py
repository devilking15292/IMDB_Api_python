import html5lib
import requests
import re
from bs4 import BeautifulSoup

class IMDB:
	baseUrl = "http://www.imdb.com/"
	titleUrl = baseUrl+"title/"
	searchUrl = baseUrl+"find?s=all&q="
	creditsPath = 'fullcredits/'
	currentSearchTitle = None
	
	
	def getMovie(self, title):
		return IMDB.getMovieByImdbId(self, IMDB.getIdFromName(title))
	
	def getMovieByImdbId(self, title):
		soup = IMDB.getSoup(title, None)
		movie = IMDB.getFeatures(soup);
		movie['rating'] = IMDB.getRatingByImdbId(self, title, soup)
		movie['summary'] = IMDB.getSummaryByImdbId(self, title, soup)
		movie['director'] = IMDB.getDirectorByImdbId(self, title, soup)
		movie['casting'] = IMDB.getCastingByImdbId(self, title)
		
		return movie;

	#############################
	'''get Ratings only STARTS'''
	#############################

	def getRating(self, title):
		return IMDB.getRatingByImdbId(self, IMDB.getIdFromName(title))

	def getRatingByImdbId(self, title, soup=None):
		soup = IMDB.getSoup(title, soup)
		return re.sub('\s+', '', IMDB.parseHTML(soup, 'div', 'class', 'ratingValue').strong.span.text)

	###########################
	'''get Ratings only ENDS'''
	###########################

	'''--------------------------------------------------------------------'''

	#############################
	'''get Summary only STARTS'''
	#############################

	def getSummary(self, title):
		return IMDB.getSummaryByImdbId(self, IMDB.getIdFromName(title))

	def getSummaryByImdbId(self, title, soup=None):
		soup = IMDB.getSoup(title, soup)
		return (re.sub(r'[\t\r\n]', '', (IMDB.parseHTML(soup, 'div', 'class', 'summary_text').text))).strip()

	#############################
	'''get Summary only ENDS'''
	#############################

	'''--------------------------------------------------------------------'''

	#############################
	'''get Director only STARTS'''
	#############################

	def getDirector(self, title):
		return IMDB.getDirectorByImdbId(self, IMDB.getIdFromName(title))

	def getDirectorByImdbId(self, title, soup=None):
		soup = IMDB.getSoup(title, soup)
		return re.sub('\s+', '', IMDB.parseHTML(soup, 'span', 'itemprop', 'director').a.span.text)

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
				cast = {}
				cast['actor'] = re.sub(r'[\t\r\n]', '', "".join(tds[1].find_all(text=True))).strip()
				cast['role'] = re.sub(r'[\t\r\n]', '', "".join(tds[3].find_all(text=True))).strip()
				castList.append(cast)
				if not all:
					counter+=1;
					if counter == 10:
						break;
		return castList;

	#############################
	'''get Casting only ENDS'''
	#############################

	'''--------------------------------------------------------------------'''
	
	def getFeatures(soup):
		features = {}
		features['title'] = IMDB.currentSearchTitle
		features['runTime'] = re.sub('\s+', '', IMDB.parseHTML(soup, 'time', 'itemprop', 'duration').text)
		features['titleYear'] = IMDB.parseHTML(soup, 'span', 'id', 'titleYear').a.text
		features['releaseDate'] = IMDB.parseHTML(soup, 'meta', 'itemprop', 'datePublished')['content']
		
		generDirty = soup.find_all(attrs = {"itemprop":"genre", "class":"itemprop"});
		gener = []
		for tag in generDirty:
			gener.append(tag.text)
		
		features['gener'] = gener;
		features['posterUrl'] = IMDB.parseHTML(soup, 'div', 'class', 'poster').a.img['src']
		
		return features;
	
	def getSoup(title, soup):
		if soup is None:
			soup = IMDB.scrapSite(IMDB.titleUrl+title+"/")
		return soup;

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
			IMDB.currentSearchTitle = movie.text;
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
