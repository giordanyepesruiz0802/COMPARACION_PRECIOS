import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback
import pandas as pd 


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

from frontend.layout import Layout

app.layout = Layout
    



# @app.callback(
#         Output('tabla_valor_2','data'),
#         Input('tabla_valor_2','data'),
#         Input('tabla_valor_2','columns')
# )

# def update_granulometria_table(rows,columns):
#     valor_2= pd.DataFrame(rows)
    
#     return valor_2.to_dict('record')

# @app.callback(
#         Output('tabla_item_2','data'),
#         Input('tabla_item_2','data'),
#         Input('tabla_item_2','columns')
# )

# def update_granulometria_table(rows,columns):
#     item_2= pd.DataFrame(rows)
    
#     return item_2.to_dict('record')

# @app.callback(
#         Output('tabla_valor_1','data'),
#         Input('tabla_valor_1','data'),
#         Input('tabla_valor_1','columns')
# )

# def update_granulometria_table(rows,columns):
#     valor_1= pd.DataFrame(rows)
    
#     return valor_1.to_dict('record')




# @app.callback(
#         Output('tabla_item_1','data'),
#         Input('tabla_item_1','data'),
#         Input('tabla_item_1','columns')
# )

# def update_granulometria_table(rows,columns):
#     item_1= pd.DataFrame(rows)
    
#     return item_1.to_dict('record')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)