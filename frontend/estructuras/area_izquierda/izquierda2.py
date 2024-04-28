import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import valor_2

Izquierda_2= dbc.Container([
    html.H4("PRECIO UNITARIO COTIZANTE 2"),
    dash_table.DataTable(
        id='tabla_valor_1',
        columns=[
            {'name':'PRECIO_UNITARIO_2','id':'PRECIO_UNITARIO_2','editable':True},
        ],
    data= valor_2.to_dict('records')
    )
        
    ]
)

