import pandas as pd
import dash
from dash import dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc

# import pokemon data
gen1 = pd.read_csv('data/gen-1.csv')
gen2 = pd.read_csv('data/gen-2.csv')

# combine data
pokemon = pd.concat([gen1, gen2], ignore_index=True)

# pokemon names
pokemon_names = pokemon['Pokemon'].tolist()

# create options for the dropdown list
options = [{'label': pokemon, 'value': pokemon} for pokemon in pokemon_names]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    
# header
dbc.Row(
    dbc.Col(
        [
            # header
            html.H1(children='My Pokemon App'),
        ],
        width={'size': 6, 'offset': 3},
        style={'textAlign': 'center'}
    )
),
    
    
# header line
html.Hr(),
    
    
# description and dropdowns
dbc.Row(dbc.Col([
    # description
    html.Div(children='''Select a pokemon to see its information.''', style={'textAlign': 'center'}),
    # dropdown
    dbc.Row(
        [dbc.Col(
            dcc.Dropdown(
                id='dropdown',
                options=options,
                placeholder='Select a pokemon'
            )
        ),
         dbc.Col(
             dbc.Button('Next Evolution', id='next-button')
             )
         ], style={'width': '50%', 'margin': 'auto'}
    )])
),

# cards
dbc.Row([
    dbc.Col(
        dbc.Card(
            [
                dbc.CardImg(src='assets/ditto.png',id='card-img', top=True),
                dbc.CardBody(
                    [
                        html.H4(id='card-title', className='card-title')
                    ]
                )
            ],
            style={'textAlign': 'center', 'margin': 'auto', 'marginTop': '20px'}
        ),
        width={'size': 4}
    ),
    dbc.Col(
        dbc.Card([
            dbc.CardBody(
                [
                    # facts table
                    dash_table.DataTable(
                        id='facts-table',
                        columns=[{'name': col, 'id': col} for col in pokemon.columns[:7]],
                        style_table={'width': '100%', 'margin': 'auto', 'marginTop': '20px'},
                        style_cell={'textAlign': 'center'},
                        style_header={'fontWeight': 'bold'}
                    ),
                    # types
                    dash_table.DataTable(
                        id='type-table',
                        columns=[{'name': col, 'id': col} for col in pokemon.columns[8:10]],
                        style_table={'width': '100%', 'margin': 'auto', 'marginTop': '20px'},
                        style_cell={'textAlign': 'center'},
                        style_header={'fontWeight': 'bold'}
                    ),
                    # stats
                    dash_table.DataTable(
                        id='stats-table',
                        columns=[{'name': col, 'id': col} for col in pokemon.columns[10:16]],
                        style_table={'width': '100%', 'margin': 'auto', 'marginTop': '20px'},
                        style_cell={'textAlign': 'center'},
                        style_header={'fontWeight': 'bold'}
                    )
                ]
            )
        ],
            style={'margin': 'auto', 'marginTop': '20px'}
        ),
        width={'size': 8}
    )]
),
    
# card line
html.Hr(),


# footer line
html.Hr(),

# footer
html.Div([
    html.A('Code on Github', href='https://github.com/ethandbard/pokemon')
])
    
], style={'textAlign': 'center', 'border': '2px solid black', 
           'width': '100%', 'height': '100%',
           'margin': 'auto'})



# update all components based on dropdown value 
@app.callback(
    [
        Output(component_id='facts-table', component_property='data'),
        Output(component_id='type-table', component_property='data'),
        Output(component_id='stats-table', component_property='data'),
        Output(component_id='card-title', component_property='children'),
        Output(component_id='card-img', component_property='src')
     ],
    [
        Input(component_id='dropdown', component_property='value')
    ],
)
def update_components(selected_value):
    if selected_value is not None:
        return [pokemon[pokemon['Pokemon'] == selected_value].to_dict('records'),
                pokemon[pokemon['Pokemon'] == selected_value][['Type 1', 'Type 2']].to_dict('records'),
                pokemon[pokemon['Pokemon'] == selected_value][['HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed']].to_dict('records'),
                selected_value,
                dash.get_asset_url(f'{selected_value}.png')]
    else:
        return [None, None, None, None, None]
    
    
# add this callback function to your file
@app.callback(
    Output('dropdown', 'value'),
    [Input('next-button', 'n_clicks')],
    [State('dropdown', 'value')]
)
def evolve_pokemon(n_clicks, current_pokemon):
    if n_clicks > 0:
        evolves_to = pokemon.loc[pokemon['Pokemon'] == current_pokemon, 'Evolves To'].values[0]
        return evolves_to
    else:
        return current_pokemon


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)



