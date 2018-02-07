# IMDB_Api_python
[![PyPI](https://img.shields.io/pypi/v/IMDBAPI.svg)](https://pypi.python.org/pypi/IMDBAPI)


## Install

```bash
pip install IMDBAPI
```

#windows
```bash
py -m pip install IMDBAPI
```

#with setup.py
```bash
py setup.py install
```

#current verision is 0.1Beta

#Has only one function getRating() which returns the rating of the requsted movie

#Example

```python
from IMDBAPI import IMDB

imdb = IMDB()

print("Movie rated: "+imdb.getRating('darknight rises')+" out of 10")
Movie: The Dark Knight Rises
Movie rated:  '8.4' out of 10
```


