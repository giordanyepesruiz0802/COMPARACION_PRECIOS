import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import item_1

Izquierda_1= dbc.Container([
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
