    dash_table.DataTable(
        id='stats-table',
        columns=[{'name': col, 'id': col} for col in pokemon.columns[11:16]],
        style_table={'width': '50%', 'margin': 'auto', 'marginTop': '20px'},
        style_cell={'textAlign': 'center'},
        style_header={'fontWeight': 'bold'}
    ),