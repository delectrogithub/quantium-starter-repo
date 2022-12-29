from dash import Dash, html, dcc, Input, Output
from datetime import time
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.read_csv('./simplesales.csv')
df = df.reindex(index=df.index[::-1])
date = []
for index, row in df.iterrows():
   date.append(str(row['month'])+ '-' + str(row['year']))


df['date'] = date

fig = px.line(df, x = 'date', y = 'sales')


app.layout = html.Div([
    dcc.Slider(2018, 2022, 1, value = 2018,
               marks={
                   2018: {'label': '2018',},
                   2019: {'label': '2019'},
                   2020: {'label': '2020'},
                   2021: {'label': '2021'},
                   2022: {'label': '2022'},

               },
               id = 'date-slider-picker'),
    dcc.Graph(figure=fig,
              id = 'graph',
              animate = True
              ),


    html.Div(id = 'slider-output-container')])


@app.callback(
    Output('slider-output-container', 'children'),
    Input('date-slider-picker', 'value')
)
def update_output(value):
    pass

if __name__ == '__main__':
    app.run_server(debug=True)

