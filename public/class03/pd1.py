"""
pd1.py

This script should read 
http://www.spy611.com/csv/allpredictions.csv
using Pandas.
"""

# Google:
# In Python how to use requests package to get CSV file?

import requests
import pandas as pd

url_s = 'http://www.spy611.com/csv/allpredictions.csv'

with requests.Session() as session:
  download          = session.get(url_s)
  decoded_content_s = download.content.decode('utf-8')

# Google:
# In Python how to write string to file?
with open('/tmp/allpredictions.csv', 'w') as myfile:
  myfile.write(decoded_content_s)

# Google:
# In Python Pandas, how to read a CSV file into DataFrame?
allpredictions_df = pd.read_csv('/tmp/allpredictions.csv')
print(allpredictions_df.tail())

# Google:
# In Python Pandas, how to read a CSV file from URL?
easier_df = pd.read_csv(url_s)
print(easier_df.tail())

'bye'
