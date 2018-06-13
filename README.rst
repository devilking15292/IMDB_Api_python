
IMDB_Api_python
===============


.. image:: https://img.shields.io/pypi/v/IMDBAPI.svg
   :target: https://pypi.python.org/pypi/IMDBAPI
   :alt: PyPI


Install
-------

.. code-block:: bash

   pip install IMDBAPI

windows
-------

.. code-block:: bash

   py -m pip install IMDBAPI

with setup.py
-------------

.. code-block:: bash

   py setup.py install

API
---

getRating(movieName ):
^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the rating of the requsted movie by passing Movie Name as a parameter


getRatingByImdbId(IMDB_ID ):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the rating of the requsted movie by IMDB ID as a prameter


getDirector(movieName):
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the Directors name of the requsted movie by passing Movie Name as a parameter


getDirectorByImdbId(IMDB_ID ):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the Directors name of the requsted movie by IMDB ID as a prameter


getCasting(movieName, length=10, all=False):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the cast list of the requsted movie by passing Movie Name as a parameter

length: No of castlist which will be returned (default "10")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

all: if set to True returns all the cast list (default "False")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

getCastingByImdbId(IMDB_ID , length=10, all=False):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the cast list of the requsted movie by IMDB ID as a prameter

length: No of castlist which will be returned (default "10")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

all: if set to True returns all the cast list (default "False")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

getSummary(movieName ):
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the summary of the requsted movie by passing Movie Name as a parameter


getSummaryByImdbId(IMDB_ID ):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the summary of the requsted movie by IMDB ID as a prameter


getMovie(movieName ):
^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the an object with data of the requsted movie by passing Movie Name as a parameter (see getMovieByImdbId() for more deatails)


getMovieByImdbId(IMDB_ID ):
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

       which returns the data of the requsted movie by IMDB ID as a prameter, data is as follows

       title - Movie full tile
       runTime - duration of the movie
       titleYear - year of the movie title
       releaseDate - date of the movie
       gener - gener as an array
       posterUrl - url of the movie poster
       rating - rating of the movie
       summary - summary text
       director - name of the director
       casting - list of top 10 cast (can be tweaked to print all the casting)


Example
-------

.. code-block:: python

   from IMDBAPI import IMDB

   imdb = IMDB()

   print("Movie rated: "+imdb.getRating('darknight rises')+" out of 10")

   Movie: The Dark Knight Rises
   Movie rated:  '8.4' out of 10


   Sample1.py output: (pretty printed just for viewing)

   Enter a movie: darknight rises

   Movie: The Dark Knight Rises
   Movie Rated: 8.4 out Of 10

   Movie: The Dark Knight Rises
   Summary: Eight years after the Joker's reign of anarchy, Batman, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.

   Movie: The Dark Knight Rises
   Director: ChristopherNolan

   Movie: The Dark Knight Rises
   Cast_list size: 10

   {
       'actor': 'Christian Bale',
       'role': 'Bruce Wayne'
   } {
       'actor': 'Gary Oldman',
       'role': 'Commissioner Gordon'
   } {
       'actor': 'Tom Hardy',
       'role': 'Bane'
   } {
       'actor': 'Joseph Gordon-Levitt',
       'role': 'Blake'
   } {
       'actor': 'Anne Hathaway',
       'role': 'Selina'
   } {
       'actor': 'Marion Cotillard',
       'role': 'Miranda'
   } {
       'actor': 'Morgan Freeman',
       'role': 'Fox'
   } {
       'actor': 'Michael Caine',
       'role': 'Alfred'
   } {
       'actor': 'Matthew Modine',
       'role': 'Foley'
   } {
       'actor': 'Alon Aboutboul',
       'role': 'Dr. Pavel       (as Alon Moni Aboutboul)'
   }


   Movie Details:
   Movie: The Dark Knight Rises

   {
       "title": "The Dark Knight Rises",

       "runTime": "2h44min",

       "titleYear": "2012",

       "releaseDate": "2012-07-20",

       "gener": ["Action", "Thriller"],

       "posterUrl": "https://m.media-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",

       "rating ": "8.4 ",

       "summary ": "Eight years after the Joker 's reign of anarchy,Batman with the help of the enigmatic Catwoman,is forced from his exile to save Gotham City",

       "director ": "ChristopherNolan ", 

       "casting ": [{
           'actor': 'Christian Bale',
               'role': 'Bruce Wayne'
           }, {
               'actor': 'Gary Oldman',
               'role': 'Commissioner Gordon'
           }, {
               'actor': 'Tom Hardy',
               'role': 'Bane'
           }, {
               'actor': 'Joseph Gordon-Levitt',
               'role': 'Blake'
           }, {
               'actor': 'Anne Hathaway',
               'role': 'Selina'
           }, {
               'actor': 'Marion Cotillard',
               'role': 'Miranda'
           }, {
               'actor': 'Morgan Freeman',
               'role': 'Fox'
           }, {
               'actor': 'Michael Caine',
               'role': 'Alfred'
           }, {
               'actor': 'Matthew Modine',
               'role': 'Foley'
           }, {
               'actor': 'Alon Aboutboul',
               'role': 'Dr. Pavel       (as Alon Moni Aboutboul)'
           }
       ]
   }

IMDB_ID :
---------

.. code-block::

   is an unique ID given by IMDB to a movie or series or a celebrity, IMDB_ID can be found in the URL.
   if you open IMDB for a movie, say "The Dark night rises" the URL will be "https://www.imdb.com/title/tt1345836/"

   this last text "tt1345836" is the IMDB ID of the movie
