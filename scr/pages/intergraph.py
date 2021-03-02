import dash_core_components as dcc
import dash_html_components as html
import altair as alt
from utils import Header, make_dash_table
import pathlib
import pandas as pd
import numpy as np



#------------------
# imort data

wine = pd.read_csv("scr/data/wine.csv")
wine['Taste'] = np.where(wine['quality']<6, 'Below average', (np.where(wine['quality']>6.5, 'Above average', 'Average')))

#---------------------


     
def create_layout(app):

    return html.Div(
        [
             Header(app),
             html.H1('Add plot here'),
             html.Iframe(
                 id='scatter',
                 style={'border-width': '0', 'width': '100%', 'height': '400px'}),
             dcc.Dropdown(
                 id='xcol-widget',
                 value='',  # REQUIRED to show the plot on the first page load
                 options=[{'label': col, 'value': col} for col in wine.columns])
                    
             
        ])

 
 



    
if __name__ == '__main__':
    app.run_server(debug=True)