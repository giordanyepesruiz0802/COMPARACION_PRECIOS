import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import valor_1

Derecha_1= dbc.Container([
    html.H4("PRECIO UNITARIO COTIZANTE 2"),
    dash_table.DataTable(
        id='tabla_valor_2',
        columns=[
            {'name':'PRECIO_UNITARIO_1','id':'PRECIO_UNITARIO_1','editable':True},
        ],
    data= valor_1.to_dict('records')
    )
        
    ]
)
