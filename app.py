import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback
import pandas as pd 


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

from frontend.layout import Layout

app.layout = Layout
    


if __name__ == '__main__':
    app.run_server(debug=True)