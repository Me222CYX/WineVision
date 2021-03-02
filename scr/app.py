# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    intergraph,
    overview
)
app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == '/WineVison/scr/intergraph':
        return intergraph.create_layout(app) 

    elif pathname == "/WineVision/scr/full-view":
        return (
            overview.create_layout(app),
            intergraph.create_layout(app),
            modelling.create_layout(app)
        )   

    else:
        return overview.create_layout(app)
    
@app.callback(
     Output('scatter', 'srcDoc'),
     Input('xcol-widget', 'value')
     )

def plot_altair(xcol):
    chart= alt.Chart(wine).mark_bar().encode(
        x=xcol,
        y=alt.Y('count()'),
        color='Taste').interactive()
    return chart.to_html()
if __name__ == "__main__":
    app.run_server(debug=True)