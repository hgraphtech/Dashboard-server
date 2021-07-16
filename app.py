from flask import Flask
from flask import render_template
import pandas as pd
import datetime as dt



app = Flask(__name__)


df = pd.read_pickle('commod_price_data.pkl')
df = df.fillna(method="ffill")

commodities = df.columns

table_data = [{'commodity':c, 'price': round(df[c][-1],1),
      'om': round(100*(df[c][-1]-df[c][-20])/df[c][-20],1),
      'sm': round(100*(df[c][-1]-df[c][-120])/df[c][-120],1)}
      for c in df.columns]

dates = [d.strftime('%F')  for d in df.index]

prices_data = [{'commodity':c, 'price_series':list(df[c].values)} for c in df.columns]

chart_data = {}
for c in commodities:
  chart_data[c] = list(df[c].values)



@app.route("/")
def index():
    return render_template('index.html', table_data=table_data)

# @app.route("/<name>")
# def hello(name):
#   return render_template('index.html', table_data=table_data, commodity=name, chart_dates=dates, chart_data=chart_data[name])

@app.route('/api/test', methods=['GET'])
def test():
  return {'data':[1,2,3,4,5]}

@app.route('/api/table', methods=['GET'])
def table():
  return {'table_data':table_data}

@app.route('/api/price', methods=['GET'])
def chart():
  return {'dates':dates, 'prices':prices_data}

if __name__ == "__main__":
  app.run(debug=True)