import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback, dash_table

from backend.valores import item_2

Derecha_2= dbc.Container([
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
