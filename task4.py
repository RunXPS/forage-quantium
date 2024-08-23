# Goals:
# => radio button filtering based on region
# => Have fun

from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash("Pink Morsel Sales")

df = pd.read_csv("./filtered_daily_sales_data.csv")
app.layout = html.Div( children=[
    html.Header(children="Test App"),
    html.H1(children='Sales of Pink Morsels Over Time',
            style={
        'textAlign': 'center',
    }),
    html.Div(children=[
        dcc.Graph(
            id='line-graph',
            # figure=graph
        ),
        ], style={'width': '49%', 'height': '450px', 'display': 'inline-block', 'border':'solid', 'float': 'left'}),
    html.Div(children=[
        html.H2(children="Options", style={'textAlign' : 'center'}),
        html.H4(children='Region:'),
        dcc.RadioItems(
            ['north', 'south', 'east', 'west', 'all'],
            'all',
            id = 'region_set',
            inline=True,
        )
        ], style={'width': '49%', 'height': '450px', 'display': 'inline-block', 'border':'solid', 'float': 'right'}),        
])
@callback(
    Output('line-graph', 'figure'),
    Input('region_set', 'value')
)
def update_graph(region_set):
    if (region_set == 'all'):
        filtered_df = df
    else: 
        filtered_df = df[df.region == region_set]
    fig =  px.line(filtered_df, x="date", y="sales", color="region")
    fig.update_layout(transition_duration=500)
    return fig    

if __name__ == '__main__':
    app.run(debug=True)