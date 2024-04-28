import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

# from backend.granulometria import granulometria

centro_l= dbc.Container([
   html.H4("VALOR UNITARIO COMPARADO"),
   dash_table.DataTable(
      id='tabla_granulometria',
      columns=[
          {'name':'PRECIO UNITARIO','id':'PRECIO UNITARIO','editable':False},
        ],
    # data= granulometria.to_dict('records')
  )
])