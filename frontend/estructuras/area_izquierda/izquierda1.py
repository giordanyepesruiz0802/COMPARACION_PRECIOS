import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import item_1

Izquierda_1= dbc.Container([
    html.H4("PRECIO UNITARIO COTIZANTE 1"),
    
    dash_table.DataTable(
        id='tabla_item_1',
        columns=[
            {'name':'ITEM_1','id':'ITEM_1','editable':True}, #explicar
        ],
    data= item_1.to_dict('records')
    )
        
    ]
)
