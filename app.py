#!/usr/bin/env python3

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python!
    '''),

    # dropdown
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='SF'
    ),

    # button
    html.Button('Submit', id='button'),

    # output
    html.Div(id='output')


])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='button', component_property='n_clicks')],
    [State(component_id='dropdown', component_property='value')]
)
def update_output_div(n_clicks, selected_value):
    if n_clicks is not None:
        return f'You have selected "{selected_value}"'

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)



