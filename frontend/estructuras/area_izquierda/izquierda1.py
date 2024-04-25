import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback

from backend.valores import item_1

Derecha_1= dbc.Container([
    html.H1("PRECIO UNITARIO COTIZANTE 1"),
    dash_table.DataTable(
        id='tabla_item_1',
        columns=[
            {'name':'PRECIO UNITARIO','id':'PRECIO UNITARIO','editable':False},
        ],
    data= item_1.to_dict('record')
    )
        
    ]
)

@app.callback(
        Output('tabla_item_1','data'),
        Input('tabla_item_1','data'),
        Input('tabla_item_1','columns')
)

def update_granulometria_table(rows,columns):
    item_1= pd.DataFrame(rows)
    
    return item_1.to_dict('record')