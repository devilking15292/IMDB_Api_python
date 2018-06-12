# IMDB_Api_python
[![PyPI](https://img.shields.io/pypi/v/IMDBAPI.svg)](https://pypi.python.org/pypi/IMDBAPI)


## Install

```bash
pip install IMDBAPI
```

## windows
```bash
py -m pip install IMDBAPI
```

## with setup.py
```bash
py setup.py install
```

## API
		
 ### getRating(movieName ):
		
		which returns the rating of the requsted movie by passing Movie Name as a parameter
		
 ### getRatingByImdbId(IMDB_ID ):
		
		which returns the rating of the requsted movie by IMDB ID as a prameter

 ### getDirector(movieName):
		
		which returns the Directors name of the requsted movie by passing Movie Name as a parameter

 ### getDirectorByImdbId(IMDB_ID ):
		
		which returns the Directors name of the requsted movie by IMDB ID as a prameter

 ### getCasting(movieName, length=10, all=False):
		
		which returns the cast list of the requsted movie by passing Movie Name as a parameter
	#### length: No of castlist which will be returned (default "10")
	#### all: if set to True returns all the cast list (default "False")
		
 ### getCastingByImdbId(IMDB_ID , length=10, all=False):
		
		which returns the cast list of the requsted movie by IMDB ID as a prameter
	#### length: No of castlist which will be returned (default "10")
	#### all: if set to True returns all the cast list (default "False")

 ### getSummary(movieName ):
		
		which returns the summary of the requsted movie by passing Movie Name as a parameter

 ### getSummaryByImdbId(IMDB_ID ):
		
		which returns the summary of the requsted movie by IMDB ID as a prameter

## Example

```python
from IMDBAPI import IMDB

imdb = IMDB()

print("Movie rated: "+imdb.getRating('darknight rises')+" out of 10")

Movie: The Dark Knight Rises
Movie rated:  '8.4' out of 10
```


## IMDB_ID : 
	is an unique ID given by IMDB to a movie or series or a celebrity, IMDB_ID can be found in the URL.
if you open IMDB for a movie, say "The Dark night rises" the URL will be "https://www.imdb.com/title/tt1345836/"

this last text "tt1345836" is the IMDB ID of the movie



