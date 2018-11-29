from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure
from bs4 import BeautifulSoup
from random import randrange

import requests

#create figure
f = figure(x_range = (0,11), y_range = (0,11))

#create data source
source = ColumnDataSource(dict(x = [], y = []))

#create glyphs
f.circle(
    x = 'x',
    y = 'y',
    color = 'olive',
    line_color = 'brown',
    source = source)

#create webscraping function
def extract_value():
    r = requests.get("https://bitcoincharts.com/markets/coinbaseUSD.html", headers = {'User-Agent' : 'Mozilla/5.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    value_raw = soup.find_all("p")
    value_net = float(value_raw[0].span.text)
    return value_net

def update():
    new_data=dict(x=[randrange(1,10)],y=[randrange(1,10)])
    source.stream(new_data,rollover=15)
    print(source.data)

curdoc().add_root(f)
curdoc().add_periodic_callback(update, 1000)
