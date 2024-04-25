import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback

from backend.granulometria import granulometria

Izquierda_3= dbc.Container([
   html.H1("VALOR UNITARIO COMPARADO"),
   dash_table.DataTable(
      id='tabla_granulometria',
      columns=[
          {'name':'PRECIO UNITARIO','id':'PRECIO UNITARIO','editable':False},
        ],
    data= granulometria.to_dict('record')
  )
])