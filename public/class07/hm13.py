# hm13.py

# Ref:
# http://bokeh.pydata.org/en/latest/docs/gallery/heatmap_chart.html

# Demo:
# ~/anaconda3/bin/python hm13.py

import pandas as pd

from bokeh.charts import HeatMap, bins, output_file, show
from bokeh.layouts import column, gridplot
from bokeh.palettes import RdYlGn6, RdYlGn9
from bokeh.sampledata.unemployment1948 import data

# setup data sources
del data['Annual']
data['Year'] = data['Year'].astype(str)
unempl = pd.melt(data, var_name='Month', value_name='Unemployment', id_vars=['Year'])

fruits = {'fruit': ['apples', 'apples', 'apples', 'apples', 'apples',
                    'pears', 'pears', 'pears', 'pears', 'pears',
                    'bananas', 'bananas', 'bananas', 'bananas', 'bananas'],
          'fruit_count': [4, 5, 8, 12, 4, 6, 5, 4, 8, 7, 1, 2, 4, 8, 12],
          'year': [2009, 2010, 2011, 2012, 2013, 2009, 2010, 2011, 2012, 2013, 2009, 2010,
                   2011, 2012, 2013]}
fruits['year'] = [str(yr) for yr in fruits['year']]

hm9 = HeatMap(fruits, y='year', x='fruit', values='fruit_count', stat=None)

hm10 = HeatMap(unempl, x='Year', y='Month', values='Unemployment', stat=None,
              sort_dim={'x': False}, width=900, plot_height=500)

output_file("hm13.html", title="Bokeh heatmap example (hm13.py)")

show(column(hm9,hm10))

