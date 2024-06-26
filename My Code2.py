#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
#app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Years Statistics Report', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Periodic Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1('Automobile Sales Statistics Dashboard', 
                                style={'textAlign': 'centre', 'color': '#503D36',
                                'font-size': 24}),#May include style for title
html.Div([#TASK 2.2: Add two dropdown menus
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Periodic Statistics'}
], 
            value='Select Statistics',
            placeholder='Select a report type',
            style={'width':'80%','padding':'3px','size':'20px','text-align-last':'centre'}
        ),
    ]),
html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value='Input Year',
            placeholder='Select year',
            style={'width':'80%','padding':'3px','size':'20px','text-align-last':'centre'}
        )),
        html.Div([#TASK 2.3: Add a division for output display
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),])
])
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select year', component_property='disabled'),
    Input(component_id='dropdown-statistics',component_property='....'))

def update_input_container(Recession_Statistics, Yearly_Statistics):
    if selected_statistics =='Yearly Statistics': 
        return False
    else: 
        return True
#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-year', component_property='children'), Input(component_id='dropdown-statistics', component_property='children')])

def update_output_container(Yearly_Statistics_report, Recession_Period_Statistics):
    if selected_report == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]    
#TASK 2.5: Create and display graphs for Recession Report Statistics

#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # use groupby to create relevant data for plotting
        yearly_rec=recession_data.groupby('...')['...'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px......(....., 
                x='....',
                y='......',
                title="Average Automobile Sales fluctuation over Recession Period"))

#Plot 2 Calculate the average number of vehicles sold by vehicle type       
        # use groupby to create relevant data for plotting
        average_sales = ...............mean().reset_index()                           
        R_chart2  = dcc.Graph(figure=px....................
        
# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # use groupby to create relevant data for plotting
        exp_rec= ....................
        R_chart3 = .............

# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        ................
        ...................


        return [
            html.Div(className='..........', children=[html.Div(children=R_chart1),html.Div(children=.....)],style={.....}),
            html.Div(className='chart-item', children=[html.Div(children=...........),html.Div(.............)],style={....})
            ]


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

