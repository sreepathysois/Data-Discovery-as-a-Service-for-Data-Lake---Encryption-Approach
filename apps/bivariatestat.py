import io
import os
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import mysql.connector

from app import app
from apps import homepage, exploreview, overallstat, statselection, overviewstat,univariatestat, bivariatestat, completestat, datastat, datasetselect
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}
#app = dash.Dash()   #initialising dash app
global df
#df = pd.read_csv("rainfall_flood.csv") 
"""
options = []
for col in df.columns:
   options.append({'label':'{}'.format(col, col), 'value':col}) 
"""

layout = html.Div([
        html.H1("Data Lake  Data Discovery Service",  style={
            'textAlign': 'center',
            #'color': colors['text']
        }
),

        html.H1("Select any  features from drop-down for Multi-Variate Statistics",  style={
            'textAlign': 'center',
            #'color': colors['text']
        }
),
        html.H2("Select BiVariate fields of your Interest for Statistics View:",  style={
            'textAlign': 'center',
            #'color': colors['text']
        }
),
        dcc.RadioItems(
        id='bivariate', 
        options=[{'value': x, 'label': x} 
                 for x in ['ScatterPlots', 'BoxPlots', 'ViolinPlots']],
        value='ScatterPlots', 
         style={
            'textAlign': 'center',
            "font-size": 20, 
            "padding":"10px", 
            #'color': colors['text']
        }, 

        labelStyle={'display': 'inline-block'}
        ),
      
        dcc.Dropdown(
            id = 'my_dropdown2',
            #options= options
            #value='Choose columns'
        ),
        dcc.Dropdown(
            id = 'my_dropdown3',
            #options= options
            #value='Choose columns'
        ),
        dcc.Graph(id='my_label2'), 
  ]) 

@app.callback(
    Output('my_label2', 'figure'),
    [Input('bivariate', 'value'), 
     Input('my_dropdown2', 'value'), 
     Input('my_dropdown3', 'value')] 
    
    )
def update_dropdown(value1,value2,value3):
   if(value1=='ScatterPlots'):
     v1=value2
     v2=value3
     fig = px.scatter(df,x=v1,y=v2)
     """
     fig.update_layout(
     plot_bgcolor=colors['background'],
     paper_bgcolor=colors['background'],
     font_color=colors['text']), 
     """
     return fig

   elif(value1=='BoxPlots'):
     v1=value2 
     v2=value3 
     fig = px.box(df,x=v1,y=v2)
     """
     fig.update_layout(
     plot_bgcolor=colors['background'],
     paper_bgcolor=colors['background'],
     font_color=colors['text']), 
     """
     return fig

   elif(value1=='ViolinPlots'):
     #x=['{}'.format(value2)]
     #y=['{}'.format(value3)]
     v1=value2 
     v2=value3 
     fig = px.violin(df,v1,v2)
     """
     fig.update_layout(
     plot_bgcolor=colors['background'],
     paper_bgcolor=colors['background'],
     font_color=colors['text']), 
     """  
     return fig



@app.callback(
              [Output('my_dropdown2', 'options'),
              Output('my_dropdown3', 'options')],
              [Input('session_dataset', 'data'),
               Input('session_seldata','data'), 
               Input('session','data')]
              )
def selectionresult(dataset,tabledata,dbdata):
    database = dbdata
    print(database)
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123", database=str(dbdata))
    table = tabledata
    print(table)
    global df
    c=conn.cursor()
    """
    querry = "SELECT * FROM " + table
    c = conn.cursor()
    #c.execute(querry)
    #tables = c.fetchall()
    #c.execute(" SELECT * FROM rainfalldata ")
    global df
    #df = pd.DataFrame(c.fetchall())
    df=pd.read_sql(querry,con=conn)
    #df=pd.read_csv("rainfall_flood.csv")
    """
    cond="WHERE TableName="
    querry = "SELECT Location FROM " + ' ' + str(table) + ' ' + cond + '"' +dataset + '"'
    print(querry)
    c=conn.cursor()
    c.execute(querry)
    #tables = c.fetchall()
    locationpath = c.fetchall()
    print(locationpath)

    filepath = []
    for (location,) in locationpath:
       filepath.append(location)
    print(filepath[0])


    querry='sshpass -p "university" scp' + ' '  + str(filepath[0]) + ' ' + 'assets/data.csv'
    print(querry)
    os.system(querry )
    df=pd.read_csv('assets/data.csv')
    options = []
    for col in df.columns:
       options.append({'label':'{}'.format(col, col), 'value':col})
    print(options)
    print(df.head(2))
    return options,options

