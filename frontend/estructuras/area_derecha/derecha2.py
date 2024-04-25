import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback

from backend.valores import item_2

Derecha_1= dbc.Container([
    html.H1("PRECIO UNITARIO COTIZANTE 2"),
    dash_table.DataTable(
        id='tabla_item_2',
        columns=[
            {'name':'PRECIO UNITARIO','id':'PRECIO UNITARIO','editable':False},
        ],
    data= item_2.to_dict('record')
    )
        
    ]
)

@app.callback(
        Output('tabla_item_2','data'),
        Input('tabla_item_2','data'),
        Input('tabla_item_2','columns')
)

def update_granulometria_table(rows,columns):
    item_2= pd.DataFrame(rows)
    
    return item_2.to_dict('record')