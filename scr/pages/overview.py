import dash_core_components as dcc
import dash_html_components as html
import altair as alt
from utils import Header, make_dash_table
import pathlib
import pandas as pd
import numpy as np


def create_layout(app):
    # Page layouts
    return html.Div(    
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    
                    # Row 3
                    html.Div(
                        [
                            html.H5('Motivation'),
                            html.Br([]),
                            html.P(
                                "\
                                Wine is a multi billion dollar global industry. \
                                With 36 billion bottles of wine produced each year 1,producers are constantly looking for ways to outperform \
                                the competition and create the best wines they can. \
                                Portugal in particular is second in the world for per-capita wine \
                                consumption 2 and eleventh for wine production, creating over 600,000 \
                                litres per year 3.Physicochemical components are fundamental to a wine’s quality \
                                and those who understand this aspect of wine will have a greater edge into crafting an enjoyable \
                                and profitable product.Wine quality evaluation is the main part of the certification process to \
                                improve wine making. It is generally assessed by physicochemical tests and sensory analysis. \
                                The relationship between physicochemical structure and subjective quality is complex. \
                                No individual component can be used to accurately predict a wine’s quality, and interactions \
                                are as important as the components themselves. For example, perhaps higher alcohol content only  \
                                improves a wine within a certain range of sulphate content, and wines outside this range are made \
                                worse by higher alcohol content. Trained wine tasting experts are able to reliably score wine on a \
                                scale ranging from 0 (very bad) to 10 (excellent), and those scores can be used to determine how these \
                                physicochemical properties affect quality.Our interactive dashboard will allow users to explore a number \
                                of physicochemical variables and how they interact to determine the subjective quality of a wine. \
                                Our visualizations will allow users to test and discover for themselves these relationships. \
                                Wine producers, wine enthusiasts, and curious individuals can all make use of this dashboard.",
                                    style={'color':"black"},
                                     className="row",  
                                ),
                        ],
                        className="product"
                    )
                    
                    
                ],
            ),    
                
        ],
        className="page",
    )