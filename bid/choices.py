__author__ = 'animesh'
from datetime import datetime
def tuplify(x): return (x,x)   # str(x) if needed
current_year = datetime.now().year
YEARS = map(tuplify, range(1930, current_year + 1))  # range(1,4) gives [1,2,3]
