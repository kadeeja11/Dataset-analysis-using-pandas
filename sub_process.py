from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import webbrowser
import sys
import threading

def func(file_name):
    file_name=r'C:/Users/junai/Downloads/archive/ '.strip()+file_name+r".csv"
    #file_name=r'/home/sadham/sadham/tkinter_project/archive/ '.strip()+file_name+r".csv"
    print(file_name)
    app = Dash(__name__)

    app.layout = html.Div([
        html.H4('Apple stock candlestick chart'),
        dcc.Checklist(
            id='toggle-rangeslider',
            options=[{'label': 'Include Rangeslider', 
                    'value': 'slider'}],
            value=['slider']
        ),
        dcc.Graph(id="graph"),
    ])


    @app.callback(
        Output("graph", "figure"), 
        Input("toggle-rangeslider", "value"))
    def display_candlestick(value):
        df = pd.read_csv(file_name)
        fig = go.Figure(go.Candlestick(
            x=df['Date'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close']
        ))

        fig.update_layout(
            xaxis_rangeslider_visible='slider' in value
        )
        
        return fig
    
# webbrowser.open('http://127.0.0.1:8050/')
    webbrowser.open_new_tab('http://127.0.0.1:8050/')
    app.run_server(debug=True,use_reloader=False)
    # threading.Thread(args=(app.run_server(debug=True,use_reloader=False)))

file_name = sys.argv[1]
func(file_name=file_name)