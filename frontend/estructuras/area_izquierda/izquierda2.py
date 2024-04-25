import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback

from backend.valores import valor_1

Derecha_1= dbc.Container([
    html.H1("PRECIO UNITARIO COTIZANTE 2"),
    dash_table.DataTable(
        id='tabla_valor_1',
        columns=[
            {'name':'PRECIO UNITARIO','id':'PRECIO UNITARIO','editable':False},
        ],
    data= valor_1.to_dict('record')
    )
        
    ]
)

@app.callback(
        Output('tabla_valor_1','data'),
        Input('tabla_valor_1','data'),
        Input('tabla_valor_1','columns')
)

def update_granulometria_table(rows,columns):
    valor_1= pd.DataFrame(rows)
    
    return valor_1.to_dict('record')