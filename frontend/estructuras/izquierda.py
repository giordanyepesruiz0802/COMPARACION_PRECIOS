import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback

from .area_izquierda.izquierda1 import Izquierda_1
from .area_izquierda.izquierda2 import Izquierda_2
from .area_izquierda.izquierda3 import Izquierda_3

Izquierda= dbc.Container([
    dbc.Row([
        dbc.Col(Izquierda_1,md=2,style={'background-color':'PaleGreen3'}),
        dbc.Col(Izquierda_2,md=2,style={'background-color':'grey61'}),
        dbc.Col(Izquierda_3,md=4,style={'background-color':'LightCyan2'}),

    ])

    
])