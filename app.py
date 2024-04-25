import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

from frontend.frontend import Layout

app.layout = Layout



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)