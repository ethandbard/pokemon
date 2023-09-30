import dash
from dash import Dash, dcc, html, Input, Output
import pokebase as pb
import pandas as pd
import numpy as np

# import pokemon data
pokemon = pd.read_csv('pokemon.csv')

# pokemon names
pokemon_names = pokemon['Pokemon'].tolist()

# create options for the dropdown list
options = [{'label': pokemon, 'value': pokemon} for pokemon in pokemon_names]


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    
    html.Div([
        
        # header
        html.H1(children='My Pokemon App'),

        html.Div([
        # larvitar.png
        html.A(html.Img(src=app.get_asset_url('larvitar.png')), href='https://www.pokemon.com/us/pokedex/larvitar'),
        # charmander.png
        html.A(html.Img(src=app.get_asset_url('charmander.png')), href='https://www.pokemon.com/us/pokedex/charmander'),
        # bulbasaur.png
        html.A(html.Img(src=app.get_asset_url('bulbasaur.png')), href='https://www.pokemon.com/us/pokedex/bulbasaur'),
        # squirtle.png
        html.A(html.Img(src=app.get_asset_url('squirtle.png')), href='https://www.pokemon.com/us/pokedex/squirtle')
        ], style={'textAlign': 'center'})
        
    ], style={'textAlign': 'center'}),
    
    
    # header line
    html.Hr(),
    
    # description
    html.Div(children='''
        Select a pokemon to see its information.
    ''', style={'textAlign': 'center'}),
    
    # dropdown
    dcc.Dropdown(
    id='dropdown',
    options=options,
    style={'width': '50%', 'margin': 'auto'}),
    
    # Text output for dropdown value
    html.Div(id='output',
             style={'width': '25%', 'margin': 'auto', 'border': '2px solid black', 'padding': '10px', 'marginTop': '20px'}),
    
    # large image
    html.Img(id='large-image', style={'width': '25%', 'display': 'block', 'margin': 'auto', 'border': '2px solid black', 'marginTop': '20px'}), 
    
    # show evolves to
    html.Div(id='evolves-to', style={'width': '25%', 'margin': 'auto', 'border': '2px solid black', 'padding': '10px', 'marginTop': '20px'}),
    
    # footer
    html.Div([
        html.A('Code on Github', href='https://github.com/ethandbard/pokemon')
    ]   
)]
    )



# check dropdown value change
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='dropdown', component_property='value')],
)

def update_output_div(selected_value):
    if selected_value is not None:
        return f'You have selected "{selected_value}"'
    
    
# show large image based on dropdown value
@app.callback(
    Output(component_id='large-image', component_property='src'),
    [Input(component_id='dropdown', component_property='value')],
)
def update_large_image(selected_value):
    if selected_value is not None:
        return dash.get_asset_url(f'{selected_value}.png')


# update description based on dropdown value
@app.callback(
    Output(component_id='evolves-to', component_property='children'),
    [Input(component_id='dropdown', component_property='value')],
)
def update_evolves_to(selected_value):
    if selected_value is not None:
        # return evolves_to for that pokemon if not 'None'
        if pokemon[pokemon['Pokemon'] == selected_value]['Evolves To'].values[0] == 'None':
            return f"{selected_value} does not evolve."
        else:
            return f"Evolves to: {pokemon[pokemon['Pokemon'] == selected_value]['Evolves To'].values[0]}"


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)



