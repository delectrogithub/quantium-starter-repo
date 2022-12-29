from dash import Dash, html, dcc, Input, Output
from datetime import time
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.read_csv('./simplesales.csv')
dfall = pd.read_csv('./pmsales.csv')
dfall = dfall.reindex(index=dfall.index[::-1])


df = df.reindex(index=df.index[::-1])
date = []
for index, row in df.iterrows():
   date.append(str(row['month'])+ '-' + str(row['year']))

df['date'] = date




app.layout =html.Div([
    dcc.Graph(id='graph',
              figure = {},
                 ),
    dcc.RadioItems(
    [
        {
            "label": html.Div(['Simplified'], style={'color': 'Black', 'font-size': 25, 'display' : 'inline-block', 'font-family' : 'Verdana','width' : '15%', 'margin': 'auto', 'padding' : '10px' }),
            "value": "simple",
        },
        {
            "label": html.Div(['North'], style={'color': 'Black', 'font-size': 25, 'display' : 'inline-block', 'font-family' : 'Verdana','width' : '10%', 'margin': 'auto', 'padding' : '10px' }),
            "value": "north",
        },
        {
            "label": html.Div(['East'], style={'color': 'Black', 'font-size': 25, 'display' : 'inline-block', 'font-family' : 'Verdana','width' : '10%', 'margin': 'auto', 'padding' : '10px' }),
            "value": "east",
        },
        {
            "label": html.Div(['South'], style={'color': 'Black', 'font-size': 25, 'display' : 'inline-block', 'font-family' : 'Verdana','width' : '10%', 'margin': 'auto', 'padding' : '10px'}),
            "value": "south",
        },
        {
            "label": html.Div(['West'], style={'color': 'Black', 'font-size': 25, 'display' : 'inline-block', 'font-family' : 'Verdana','width' : '10%', 'margin': 'auto', 'padding' : '10px' }),
            "value": "west",
        },
        {
            "label": html.Div(['All'], style={'color': 'Black', 'font-size': 25, 'display' : 'inline-block', 'font-family' : 'Verdana','width' : '10%', 'margin': 'auto', 'padding' : '10px'  }),
            "value": "all",
        },

    ], value='simple', inline = False, id = 'radio-button-picker'
)])


@app.callback(
    Output('graph', 'figure'),
    Input('radio-button-picker', 'value'))
def update_graph(region):
    if region == 'all':
        dfr = dfall.copy()
    elif region == 'simple':
        dfr = df.copy()
    else:
        dfr = dfall.copy()
        dfr = dfr[dfr['region'] == str(region)]

    fig = px.line(dfr, x = 'date', y = 'sales', labels={
                     "date": "Date of Purchase",
                     "sales": "Sales(£)",
                 },
                title="Pink Morsel Sales - Soul Foods")

    fig.update_layout(
        font_family="Verdana",
        font_color="Black",
        font_size=15,
        title_font_family="Arial",
        title_font_color="black",
        title_font_size=30
    )

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)

