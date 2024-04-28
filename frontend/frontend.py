import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback

from .estructuras.derecha import Derecha
from .estructuras.izquierda import Izquierda


Layout= dbc.Container([
    dbc.Row([
        dbc.Col(Izquierda,md=7,style={'background-color':'grey61'}),
        dbc.Col(Derecha,md=5,style={'background-color':'PaleGreen3'}),

    ])

    
])