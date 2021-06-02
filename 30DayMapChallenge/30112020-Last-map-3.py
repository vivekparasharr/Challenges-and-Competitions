
# https://chart-studio.plotly.com/~empet/15245/animation-rotating-a-scattergeo-with-or/#/

import plotly.graph_objs as go
import numpy as np


fig= go.Figure(go.Scattergeo(
            lat=[45.5017, 51.509865, 52.520008],
            lon=[-73.5673, -0.118092, 13.404954 ],
            mode='markers',
            marker_color='red'))

fig.update_layout(width=500, height=500,
        title_text='Your title',
        title_x=0.5,
        geo=dict(
            projection_type='orthographic',
            center_lon=-180,
            center_lat=0,
            projection_rotation_lon=-180,
            showland=True,
            showcountries=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)'
        ),
       updatemenus=[dict(type='buttons', showactive=False,
                                y=1,
                                x=1.2,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, 
                                                    dict(frame=dict(duration=50, 
                                                                    redraw=True),
                                                         transition=dict(duration=0),
                                                         fromcurrent=True,
                                                         mode='immediate')
                                                   ])
                                        ])
            ]
    )
lon_range = np.arange(-180, 180, 2)

frames = [go.Frame(layout=dict(geo_center_lon=lon,
                               geo_projection_rotation_lon =lon
                           )) for lon in lon_range]

fig.update(frames=frames)
fig.show()


# https://community.plotly.com/t/animate-rotating-orthographic-map-in-python-plotly/28812/6

from plotly.offline import download_plotlyjs, init_notebook_mode,  iplot, plot
init_notebook_mode(connected=True)
iplot(fig, auto_play=True)  #or plot(fig, filename='rotation.html', auto_play=True)

import plotly.graph_objs as go
import numpy as np

data=[go.Scattergeo(
            lat=[45.5017, 51.509865, 52.520008],
            lon=[-73.5673, -0.118092, 13.404954 ],
            mode='markers',
            marker_color='red')]

layout =go.Layout(width=500, height=500,
        title_text='Your title',
        title_x=0.5,
        geo=go.layout.Geo(
            projection_type='orthographic',
            center_lon=-180,
            center_lat=0,
            projection_rotation_lon=-180,
            showland=True,
            showcountries=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)'
        ))


lon_range = np.arange(-180, 180, 2)

frames = [go.Frame(layout=go.Layout(geo_center_lon=lon,
                                    geo_projection_rotation_lon =lon
                                   ),
                   name =f'fr{k+1}') for k, lon in enumerate(lon_range)]


sliders = [dict(steps = [dict(method= 'animate',
                              args= [[f'fr{k+1}'],                           
                                     dict(mode= 'immediate',
                                          frame= dict(duration=10, redraw= True),
                                          transition=dict(duration= 0))],
                              label=f'fr{k+1}'
                              ) for k in range(len(lon_range))], 
               
                transition= dict(duration= 0 ),
                x=0, # slider starting position  
                y=0,   
               len=1.0) #slider length
           ]
    


fig = go.Figure(data=data, layout=layout, frames=frames)
fig.update_layout(sliders=sliders)
fig.show()

