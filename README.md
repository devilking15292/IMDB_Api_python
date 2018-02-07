# IMDB_Api_python

#setup
pip install IMDB

#windows
py -m pip install IMDB

#with setup.py
py setup.py install


#current verision is 0.1Beta
#Has only one function getRating() which returns the rating of the requsted movie

#Example

>>> from IMDB import IMDB

>>> imdb = IMDB()

>>> print("Movie rated: "+imdb.getRating('darknight rises')+" out of 10")
Movie: The Dark Knight Rises
Movie rated:  '8.4' out of 10
