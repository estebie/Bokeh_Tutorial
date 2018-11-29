from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure
from bs4 import BeautifulSoup
from random import randrange

import requests

#create webscraping function
def extract_value():
    r = requests.get(
        "https://bitcoincharts.com/markets/coinbaseUSD.html", 
        headers = {'User-Agent' : 'Mozilla/5.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    value_raw = soup.find_all("p")
    value_net = float(value_raw[0].span.text)
    return value_net

#create figure
f = figure()

#create data source
source = ColumnDataSource(
    dict(
        x = [1], 
        y = [extract_value()]))

#create glyphs
f.circle(
    x = 'x',
    y = 'y',
    color = 'olive',
    line_color = 'brown',
    source = source)

f.line(
    x = 'x',
    y = 'y',
    source = source)

def update():
    new_data=dict(
        x = [source.data['x'][-1]+1],
        y = [extract_value()])
    source.stream(new_data,rollover=15)
    print(source.data)

curdoc().add_root(f)
curdoc().add_periodic_callback(update, 2000)
