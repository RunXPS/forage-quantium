# Goals:
# => Create an app with a header & title
# => Use line graph to visualize filtered sales data

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash("Pink Morsel Sales")

def plot_graph (relative_path: str):
    df = pd.read_csv(relative_path)
    graph = px.line(df, x="date", y="sales", color="region")

    dcc.Graph(id='graph_1', figure=graph)

    app.layout = html.Div(children=[
        html.H1(children='Sales of Pink Morsels Over Time',
                style={
            'textAlign': 'center',
        }),

        dcc.Graph(
            id='line graph',
            figure=graph
        ),
    ])


plot_graph("../filtered_daily_sales_data.csv")    

if __name__ == '__main__':
    app.run(debug=True)