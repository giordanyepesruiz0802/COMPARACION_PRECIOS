import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback

from .estructuras.derecha import Derecha
from .estructuras.izquierda import Izquierda
from .estructuras.Centro import centro_l



Layout= dbc.Container([
    dbc.Row([
        dbc.Col(Izquierda,md=4,style={'background-color':'cadetblue'}),
        dbc.Col(centro_l,md=4,style={'background-color':'lightcyan'}),
        dbc.Col(Derecha,md=4,style={'background-color':'lightseagreen'}),

    ])

    
])