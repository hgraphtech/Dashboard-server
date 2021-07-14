from flask import Flask
from flask import render_template

app = Flask(__name__)

dates = ['Jan','Feb','Mar','Apr','May','Jun','Jul']

prices = [
  {'commodity':'Oil', 'price_series':[47,53,61,60,65,67.5,75]},
  {'commodity':'Gold', 'price_series':[1950,1860,1720,1730,1790,1905,1770]},
  {'commodity':'Silver', 'price_series':[26.3,29,26.5,25,26.5,28.2,26]},
  {'commodity':'Iron ore', 'price_series':[159,148,172,166,188,210,217]},
  {'commodity':'Nickel', 'price_series':[16400,17600,18700,16200,18200,18100,18770]},
  {'commodity':'Steel', 'price_series':[4200,4150,4600,4870,5300,4750,4800]},
  {'commodity':'Soybeans', 'price_series':[1310,1365,1400,1400,1570,1550,1450]},
  {'commodity':'Wheat', 'price_series':[640,645,640,610,725,690,650]}
]

data = [
    {'commodity':'Oil', 'price':74.4, 'om':5, 'sm':53},
    {'commodity':'Gold', 'price':1802, 'om':-3, 'sm':-5},
    {'commodity':'Silver', 'price':26.0, 'om':-6, 'sm':-1},
    {'commodity':'Iron ore', 'price':218, 'om':1, 'sm':39},
    {'commodity':'Nickel', 'price':18770, 'om':1.4, 'sm':13},
    {'commodity':'Steel', 'price':4917, 'om':2, 'sm':17},
    {'commodity':'Soybeans', 'price':1404, 'om':-3, 'sm':9},
    {'commodity':'Wheat', 'price':606, 'om':-7, 'sm':-2}
]

@app.route("/")
def index():
    return render_template('index.html', data=data)
