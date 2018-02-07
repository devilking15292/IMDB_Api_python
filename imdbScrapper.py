import html5lib
import requests
from bs4 import BeautifulSoup

class IMDB:
    baseUrl = "http://www.imdb.com/"
    titleUrl = baseUrl+"title/"
    searchUrl = baseUrl+"find?s=all&q="

    def getRating(self, title):
        try:
            url = IMDB.titleUrl+IMDB.getIdFromName(title)+"/"
            soup = IMDB.scrapSite(url)
            return soup.find('div',{'class':'ratingValue'}).strong.span.text
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
        #print(url)
        resp = requests.get(url)
        return BeautifulSoup(resp.text, "html5lib")

def main():
    while 1:
        imdb = IMDB()
        movie = input("Enter a movie: ").strip();
        if movie == 'quit':
            break
        if movie:
            print("Movie Rated: "+imdb.getRating(movie)+" out Of 10")
        else:
            print("enter a valid movie name")
main()