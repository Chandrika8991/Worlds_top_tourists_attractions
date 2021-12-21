
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('wonders_of_world.csv')

df = pd.DataFrame(data=df)

def Table(dataframe, max_rows=100):
    rows = []
    
    for i in range(len(dataframe)):
        row = []
        for col in dataframe.columns:
                
            value = dataframe.iloc[i][col]
            # using Wikipedia Link column and picture column as hyperlinks
        
            if (col == ('Wikipedia link')) or (col == ('Picture link')):
                cell = html.Td(html.A(href=value, children=value))
            
            else:
                cell = html.Td(children=value)
            row.append(cell)
        
        rows.append(html.Tr(row))
        
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        rows
    )

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=stylesheet)

fig = px.bar(df, x= 'Name', y = 'Rating')


app.layout = html.Div([html.Div([html.Img(src = 'https://img.freepik.com/free-photo/female-tourists-hand-have-happy-travel-map_1150-7411.jpg?size=626&ext=jpg', style = {'width' : '33.33%'}),
                                 html.Img(src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNVhxdXaER1PWBUGgviVY3RPKIWaFTmutVPQ&usqp=CAU', style = {'width' : '33.33%'}),
                                 html.Img(src = 'https://images.pexels.com/photos/3935702/pexels-photo-3935702.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500', style = {'width' : '33.34%'})
                                 ]),
                       
                       html.Br(),
                      
                       html.Div([html.H1("World's top tourists Attraction", style = { 'color' : 'Blue', 'textAlign' : 'center', 'text-decoration': 'underline'}),
                      
                       html.H3("Individual MA705 Project | Chandrika Sharma", style = { 'color' : 'purple', 'textAlign' : 'center','text-decoration': 'italics'})]),
                       html.H5("What is this Project about?", style = { 'color' : 'Red', 'textAlign' : 'left'}),
                       html.H6("This is for the travel enthusiasts who wish to know about new places.This dashboard helps you explore more about the top tourists places across the world."),
                       html.H5("How to use this dashboard?", style = { 'color' : 'Red', 'textAlign' : 'left'}),
                       html.H6("Select the country from the dropdown list to see the top attractions of that country. Get more information and picture of the place using the wikipedia and picture link."),
                       
                       html.Br(),
                       html.Div([html.H5('Choose Countries :'),
                                 dcc.Dropdown(
                                     options = [{'label': 'Egypt', 'value' : 'Egypt'},
                                                {'label': 'United Kingdom ', 'value' : 'United Kingdom'},
                                                {'label': 'Egypt', 'value' : 'Egypt'},
                                                {'label': 'Iraq', 'value' : 'Iraq'},
                                                {'label': 'Italy', 'value' : 'Italy'},
                                                {'label': 'Turkey', 'value' : 'Turkey'},
                                                {'label': 'United States', 'value' : 'United States'},
                                                {'label': 'Canada', 'value' : 'Canada'},
                                                {'label': 'Netherlands', 'value' : 'Netherlands'},
                                                {'label': 'Panama', 'value' : 'Panama'},
                                                {'label': 'Brazil', 'value' : 'Brazil'},
                                                {'label': 'China', 'value' : 'China'},
                                                {'label': 'Mexico', 'value' : 'Mexico'},
                                                {'label': 'Peru', 'value' : 'Peru'},
                                                {'label': 'Jordan', 'value' : 'Jordan'},
                                                {'label': 'India', 'value' : 'India'},
                                                {'label': 'Northen Pole', 'value' : 'Northen Pole'},
                                                {'label': 'Zambia', 'value' : 'Zambia'},
                                                {'label': 'Nepal', 'value' : 'Nepal'},
                                                {'label': 'Australia', 'value' : 'Australia'},
                                                {'label': 'England', 'value' : 'England'},
                                                {'label': 'Israel', 'value' : 'Israel'},
                                                {'label': 'Kenya', 'value' : 'Kenya'},
                                                {'label': 'Tibet', 'value' : 'Tibet'}],
                                     value = ["United States"],
                                     multi = True, 
                                     id = 'country_dropdown')],
                                     style={'width' : '100%'}),
                       html.Br(),
                       html.Div(dcc.Graph(figure = fig, id = 'country_plot'),
                                style = {'width' : '100%'}),
                       
                       html.H6("Rating of 5 means best among the best. 5's are the highest rated places",style = { 'color' : 'Grey', 'textAlign' : 'center'}),
                       
                       html.Br(),
                       html.Div(Table(df), 
                                id = 'table_div',
                                style={'font-size': 15 ,'width':'200%', ' float':'center', 'background': 'lightgrey'}),
                       ])

server = app.server

@app.callback( 
    Output(component_id="table_div", component_property="children"),
    [Input(component_id="country_dropdown", component_property="value")])

def update_table(countries):
    x = df[df.Country.isin(countries)]
    return Table(x)


@app.callback(
    Output(component_id="country_plot", component_property="figure"),
    [Input(component_id="country_dropdown", component_property="value")])

def update_plot(cities):
    df2 = df[df.Country.isin(cities)]
    fig = px.bar(df2, x="Name", y="Rating")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)