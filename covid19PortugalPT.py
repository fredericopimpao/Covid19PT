import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#mapbox_token
mapbox_access_token = open('mapbox_access_token').read()

#get portugal data
portugal_url='https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/data.csv'
portugal_df=pd.read_csv(portugal_url)

#organize Portugal Data
date = portugal_df.data
date_formated=[]


for x in date:
    a=x.replace('/','-')
    parts = a.split('-')
    mys = parts[2] + '-' + parts[1] + '-' + parts[0]
    date_formated.append(mys)

date=date_formated

confirmados = portugal_df.confirmados
recuperados = portugal_df.recuperados
obitos = portugal_df.obitos

activos = confirmados-obitos-recuperados

internados = portugal_df.internados
internados_uci = portugal_df.internados_uci

population_pt = 10196707
number_beds = 35429
number_ventilators = 1392

#calculate Percentage Grow
def percentageGrow(Current,Preview):
    percentageGrow = ((Current-Preview)/Preview)*100
    return percentageGrow


#Map Portugal
scale=[portugal_df.confirmados_arsnorte.iloc[-1],
                    portugal_df.confirmados_arscentro.iloc[-1],
                    portugal_df.confirmados_arslvt.iloc[-1],
                    portugal_df.confirmados_arsalentejo.iloc[-1],
                    portugal_df.confirmados_arsalgarve.iloc[-1],
                    portugal_df.confirmados_acores.iloc[-1],
                    portugal_df.confirmados_madeira.iloc[-1],
                    portugal_df.confirmados_estrangeiro.iloc[-1]]
size=[]
for x in enumerate(scale):

    if x[1]<200:
        size.append(10)
    if x[1]>200 and x[1]<400:
        size.append(11)
    if x[1]>400 and x[1]<600:
        size.append(12)
    if x[1]>600 and x[1]<800:
        size.append(13)
    if x[1]>600 and x[1]<800:
        size.append(13)
    if x[1]>800 and x[1]<1000:
        size.append(14)
    if x[1]>1000 and x[1]<1200:
        size.append(15)
    if x[1]>1200 and x[1]<1400:
        size.append(16)
    if x[1]>1400 and x[1]<1600:
        size.append(17)
    if x[1]>1600 and x[1]<1800:
        size.append(18)
    if x[1]>1800 and x[1]<2000:
        size.append(19)

fig_map = go.Figure(go.Scattermapbox(
        lat=['41.1567','40.2033','38.7059',
             '38.5586','37.189','37.794594',
             '32.3716'],
        lon=['-8.6239','-8.4103','-9.1443',
             '-7.9084','-8.4412','-25.506134',
             '-16.2749'],
        hovertext=['Norte '+ str(portugal_df.confirmados_arsnorte.iloc[-1])+'  Casos',
                    'Centro'+ str(portugal_df.confirmados_arscentro.iloc[-1])+'  Casos',
                    'Lisboa e V.Tejo'+ str(portugal_df.confirmados_arslvt.iloc[-1])+'  Casos',
                    'Alentejo'+ str(portugal_df.confirmados_arsalentejo.iloc[-1])+'  Casos',
                    'Algarve'+ str(portugal_df.confirmados_arsalgarve.iloc[-1])+'  Casos',
                    'Açores'+ str(portugal_df.confirmados_acores.iloc[-1])+'  Casos',
                    'Madeira'+ str(portugal_df.confirmados_madeira.iloc[-1])+'  Casos',],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=size,
            color='red'
        ),
     
        text=[portugal_df.confirmados_arsnorte.iloc[-1],
                    portugal_df.confirmados_arscentro.iloc[-1],
                    portugal_df.confirmados_arslvt.iloc[-1],
                    portugal_df.confirmados_arsalentejo.iloc[-1],
                    portugal_df.confirmados_arsalgarve.iloc[-1],
                    portugal_df.confirmados_acores.iloc[-1],
                    portugal_df.confirmados_madeira.iloc[-1],
                    portugal_df.confirmados_estrangeiro.iloc[-1]],
    ))

maps=[fig_map]

for elements in maps:
    elements.update_layout(
        autosize=True,
        mapbox=dict(
            accesstoken=mapbox_access_token,
            style = 'mapbox://styles/fredericopimpao/ck84zqv9l0esk1jqm4xuxmldn',
            bearing=0,
            center=dict(
                lat=38.7059,
                lon=-9.1443,
            ),
            pitch=0,
            zoom=4,

    ),
)

############################################################################                                 Graphs



fig_cases_pt = go.Figure()
fig_cases_zones = go.Figure()
fig_percentage_timeline_grow_pt = go.Figure()
fig_percentage_timeline_grow_zones = go.Figure()

line_graphs = [fig_cases_pt,
              fig_cases_zones,
              fig_percentage_timeline_grow_pt,
              fig_percentage_timeline_grow_zones
            ]

# Line Graph
line_graphs_name = [['confirmados','casos activos','obitos','recuperados'],

                    ['Norte',
                    'Centro',
                    'Lisboa e V.Tejo',
                    'Alentejo',
                    'Algarve',
                    'Açores',
                    'Madeira',
                    'estrangeiro'],
                    
                    ['Crescimento'],

                    ['Norte',
                    'Centro',
                    'Lisboa e V.Tejo',
                    'Alentejo',
                    'Algarve',
                    'Açores',
                    'Madeira',
                    'estrangeiro'],
                    ]

line_graphs_color=[['grey',
                'black',
                'red','#7FFFD4'],

                ['grey',
                'black',
                '#7FFFD4',
                'red',
                'grey',
                'black',
                '#7FFFD4',
                'red',],
                
                ['grey'],

                ['grey',
                'black',
                '#7FFFD4',
                'red',
                'grey',
                'black',
                '#7FFFD4',
                'red',],
                ]

line_graphs_data=[[confirmados,
                activos,
                obitos,
                recuperados],

                [portugal_df.confirmados_arsnorte,
                portugal_df.confirmados_arscentro,
                portugal_df.confirmados_arslvt,
                portugal_df.confirmados_arsalentejo,
                portugal_df.confirmados_arsalgarve,
                portugal_df.confirmados_acores,
                portugal_df.confirmados_madeira,
                portugal_df.confirmados_estrangeiro],
                
                [percentageGrow(confirmados,confirmados.shift(1))],

                [percentageGrow(portugal_df.confirmados_arsnorte, portugal_df.confirmados_arsnorte.shift(1)),
                percentageGrow(portugal_df.confirmados_arscentro, portugal_df.confirmados_arscentro.shift(1)),
                percentageGrow(portugal_df.confirmados_arslvt, portugal_df.confirmados_arslvt.shift(1)),
                percentageGrow(portugal_df.confirmados_arsalentejo, portugal_df.confirmados_arsalentejo.shift(1)),
                percentageGrow(portugal_df.confirmados_arsalgarve, portugal_df.confirmados_arsalgarve.shift(1)),
                percentageGrow(portugal_df.confirmados_acores, portugal_df.confirmados_acores.shift(1)),
                percentageGrow(portugal_df.confirmados_madeira, portugal_df.confirmados_madeira.shift(1)),
                percentageGrow(portugal_df.confirmados_estrangeiro, portugal_df.confirmados_estrangeiro.shift(1))],

                ]


for fig_index, fig in enumerate(line_graphs):
    for index, val in enumerate(line_graphs_data[fig_index]):
        fig.add_trace(go.Scatter(
            x=date, 
            y=val,
            name= line_graphs_name[fig_index][index],
            mode='lines+markers',
            line=dict(
                color=line_graphs_color[fig_index][index], 
                width=1)
        ))

#Percentage Graphs



circle_graph_data=[[activos.iloc[-1], recuperados.iloc[-1], obitos.iloc[-1]],
                   [internados_uci.iloc[-1], number_ventilators],
                   [portugal_df.confirmados_arsnorte.iloc[-1],
                    portugal_df.confirmados_arscentro.iloc[-1],
                    portugal_df.confirmados_arslvt.iloc[-1],
                    portugal_df.confirmados_arsalentejo.iloc[-1],
                    portugal_df.confirmados_arsalgarve.iloc[-1],
                    portugal_df.confirmados_acores.iloc[-1],
                    portugal_df.confirmados_madeira.iloc[-1],
                    portugal_df.confirmados_estrangeiro.iloc[-1]],
                    [internados.iloc[-1],number_beds]
                ]
circle_graph_name=[['Activos','Recuperados','Obitos'],
                    ['Internados UCI','Ventiladores'],
                    ['Norte',
                    'Centro',
                    'Lisboa e V.Tejo',
                    'Alentejo',
                    'Algarve',
                    'Açores',
                    'Madeira',
                    'Estrangeiro'],
                    ['Internados', 'numero de camas']
                    ]
circle_graph_color=[['grey', 'black', '#7FFFD4',]]

fig_percentage_dead_rec_act = go.Figure()
fig_percentage_uci = go.Figure()
fig_percentage_zones = go.Figure()
fig_percentage_beds = go.Figure()

circle_graph =[fig_percentage_dead_rec_act,
            fig_percentage_uci,
            fig_percentage_zones,
            fig_percentage_beds,
            ]
for index, fig in enumerate(circle_graph):
    circle_graph[index] = go.Figure(data=[go.Pie(
                             labels=circle_graph_name[index],
                             values=circle_graph_data[index],
                             textinfo='label+percent', 
                             hole = .95,
                             insidetextorientation='radial',
                            )])



line_graphs = [fig_cases_pt,
              fig_cases_zones,
              fig_percentage_timeline_grow_pt,
              fig_percentage_timeline_grow_zones
            ]
#Style

line_y_axis_name=['numero de casos','numero de casos','percentagem','percentagem']
line_title=['numero de casos em portugal','numero de casos em portugal por zona','percentagem de crescimento exponensial em portugal','percentagem de crescimento exponensial em portugal por zona']
for x, elements in enumerate(line_graphs):
    elements.update_layout(
        title={
            'text': line_title[x],
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_title="",
        yaxis_title=line_y_axis_name[x],
        plot_bgcolor="#FFFFFF",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="#7f7f7f"
        )
    )
    elements.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')

circle_title=['percentagem de infectados/ obitos/ recuperados','percentagem de ventiladores livres','percentagem de casos/zona ','percentagem de camas livres']
for x, elements in enumerate(circle_graph):
    elements.update_layout(
        showlegend=True,
        legend=dict(
        bgcolor='rgba(0, 0, 0, 0)',
        x=1,
        y=1),
        title={
            'text': circle_title[x],
            'y':.95,
            'x':0.1,
            },
        plot_bgcolor="#FFFFFF",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="#7f7f7f"
        )
    )
    elements.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=14,
                  marker=dict(colors=['black','#7FFFD4','red','LightGrey'], line=dict(color='#000000', width=.2)))


#pip install dash

import dash
import flask
import dash_html_components as html
import dash_core_components as dcc

server = flask.Flask('app')
app = dash.Dash('app', server=server,
                external_stylesheets=['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'])
data = []


data.append(html.H1(
        'COVID-19 Portugal',
        className='col-sm-12',
        style={
            'color':'black',
            'margin-left': '7vh',
            'fontSize': '14',
            'font-family':'Courier New, monospace',
        }
    ))


data.append(html.H5(
        'numero de casos activos   ' + str(activos.iloc[-1]),
        className='col-sm-12',
        style={
            'color':'black',
            'margin-left': '7vh',
            'fontSize': '14',
            'font-family':'Courier New, monospace',
        }
    ))

data.append(html.H5(
        'numero de casos confirmados   ' + str(confirmados.iloc[-1]),
        className='col-sm-12',
        style={
            'color':'black',
            'margin-left': '7vh',
            'fontSize': '14',
            'font-family':'Courier New, monospace',
        }
    ))

data.append(html.H5(
        'numero de obitos   ' + str(obitos.iloc[-1]),
        className='col-sm-12',
        style={
            'color':'black',
            'margin-left': '7vh',
            'fontSize': '14',
            'font-family':'Courier New, monospace',
        }
    ))

data.append(html.H5(
        'numero de recuperados   ' + str(recuperados.iloc[-1]),
        className='col-sm-12',
        style={
            'color':'black',
            'margin-left': '7vh',
            'fontSize': '14',
            'font-family':'Courier New, monospace',
        }
    ))

data.append(html.A(
        'doações',
        href='https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=fredericopimpao@gmail.com&lc=US&item_name=Apoio+ao+desenvolvimento+de+grafismos+relacionados+com+covid19&no_note=0&cn=&currency_code=USD&bn=PP-DonationsBF:btn_donateCC_LG.gif:NonHosted', 
        target="_blank",
        className='col-sm-12',
        style={
            'color':'red',
            'margin-left': '7vh',
            'fontSize': '3em',
            'font-family':'Courier New, monospace',
        }
    ))

data.append(html.A(
        '+ informação sobre o projecto',
        href='https://github.com/fredericopimpao/Covid19PT', 
        target="_blank",
        className='col-sm-12',
        style={
            'color':'red',
            'margin-left': '7vh',
            'fontSize': '1.2em',
            'font-family':'Courier New, monospace',
        }
    ))

data.append(dcc.Graph(id='example7',figure=fig_map, className='col-sm-12', style={'width': '50vh', 'height': '50vh'}))
data.append(dcc.Graph(id='example2',figure=fig_cases_zones, className='col-sm-6'))
data.append(dcc.Graph(id='example1',figure=fig_cases_pt, className='col-sm-6'))
data.append(dcc.Graph(id='example3',figure=fig_percentage_timeline_grow_pt, className='col-sm-6'))
data.append(dcc.Graph(id='example4',figure=fig_percentage_timeline_grow_zones, className='col-sm-6'))
data.append(dcc.Graph(id='example80',figure=circle_graph[2], className='col-sm-6'))
data.append(dcc.Graph(id='example81',figure=circle_graph[3], className='col-sm-6'))
data.append(dcc.Graph(id='example79',figure=circle_graph[0], className='col-sm-6'))
data.append(dcc.Graph(id='example5',figure=circle_graph[1], className='col-sm-6'))


'''
data.append(dcc.Graph(id='example6', figure=fig, className='col-sm-4'))
data.append(dcc.Graph(id='example5', figure=fig, className='col-sm-4'))
data.append(dcc.Graph(id='example4',figure=fig_beds, className='col-sm-4'))
data.append(dcc.Graph(id='example',figure=fig_percentage_pt, className='col-sm-12'))
data.append(dcc.Graph(id='example3',figure=fig_cases_eu, className='col-sm-12'))
data.append(dcc.Graph(id='example2',figure=fig_percentage_eu, className='col-sm-12'))
'''

    

app.layout = html.Div(data,className='row')

if __name__ == '__main__':
    app.run_server(debug=True)
