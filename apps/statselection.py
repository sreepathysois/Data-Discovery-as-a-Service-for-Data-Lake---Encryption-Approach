import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_extensions import Download
import dash_core_components as dcc
import dash_table
import pandas as pd
import mysql.connector
import base64
import io, os, sys, time
from app import app
from apps import homepage, exploreview, overallstat, datastat, statselection, datasetselect 
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)
#conn = mysql.connector.connect(host="172.16.51.28", user="sois", password="Msois@123", database="weatherdata")
"""
conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123")
c = conn.cursor()
c.execute(" SHOW DATABASES  ")
databases = c.fetchall()
"""

#app= dash.Dash()

layout= html.Div([
    html.H1("Data Lake  Data Discovery Service",  style={
            'textAlign': 'center',
            #'color': colors['text']
        }
),

    html.H1(id='myresults', style={
            'textAlign': 'center',
            #'color': colors['text']
        }
), 
    html.H2('Explore and Understand your Selected Dataset ',  style={
            'textAlign': 'center',
            #'color': colors['text']
        }
), 
    html.Br(),
       dcc.Link(
    html.Button('Explore Overall Statistics'),
    href='/overviewstat'), 
       dcc.Link(
    html.Button('Explore Univariate Statistics'),
    href='/univariatestat'), 
       dcc.Link(
    html.Button('Explore Bivariate Statistics'),
    href='/bivariatestat'), 
       dcc.Link(
    html.Button('View Complete Statistics'),
    href='/completestat') 
])

@app.callback(
              Output('myresults', 'children'),
              Input('session_dataset', 'data'),
              )
def selectionresult(data):
    #category=data
    print(data)
    #return category
    return 'Welcome to Explore Dataset Selected by You "{}"'.format(data) 
