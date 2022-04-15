
import plotly.graph_objects as go
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 415.5, domain = {'x': [0, 1], 'y': [0, 1]},))
# Title
offset_top=0.12
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=offset_top+1.22,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Fugaku, the fastest supercomputer in the world"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=offset_top+1.08,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="At RIKEN Center for Computational Science (R-CCS) in Kobe, Japan"))

# Text
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=0.55,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=13,color='grey'),showarrow=False,
  text="Boasting nearly 7.3 million cores"))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=0.5,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=13,color='grey'),showarrow=False,
  text="and a speed of 415.5 petaFLOPS,"))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=0.45,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=13,color='grey'),showarrow=False,
  text="Fugaku far outperforms previous"))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=0.4,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=13,color='grey'),showarrow=False,
  text="#1 Summit’s 148.6 PetaFLOPS"))

fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=0.06,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="1 PetaFLOP = 1 quadrillion floating-point operations per second"))

# Footer
offset_bottom=0.065 
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - pictogram - 2021/04/02'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0.06),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='https://sciencenode.org/feature/the-5-fastest-supercomputers-in-the-world.php'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0.15),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr'))
fig.show()




#####################
#### Unused code ####
#####################
from plotly.subplots import make_subplots
fig = make_subplots(rows=2, cols=2,
    shared_xaxes=True, vertical_spacing=0.25, horizontal_spacing=0.2,
    specs=[[{"type": "indicator"}, {"type": "indicator"}],
           [{"type": "indicator"}, {"type": "indicator"}]])
    #subplot_titles=("Plot 1", "Plot 2"))
fig.add_trace(go.Indicator(mode = "gauge+number", value = 250, 
    domain = {'x': [0, 1], 'y': [0, 1]}), row=1, col=1,)
fig.add_trace(go.Indicator(mode = "gauge+number", value = 220, 
    domain = {'x': [0, 1], 'y': [0, 1]}), row=2, col=1)
fig.add_trace(go.Indicator(mode = "gauge+number", value = 240, 
    domain = {'x': [0, 1], 'y': [0, 1]}), row=1, col=2)
fig.add_trace(go.Indicator(mode = "gauge+number", value = 230, 
    domain = {'x': [0, 1], 'y': [0, 1]}), row=2, col=2)

# Title
offset_top=0.12
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=offset_top+1.22,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Share of Indian movies on Netflix"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=offset_top+1.08,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Netflix Movies and TV Shows Dataset"))
# Footer
offset_bottom=0.05 
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - pictogram - 2021/04/02'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0.06),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Dataset from Kaggle: https://www.kaggle.com/shivamb/netflix-shows'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0.15),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr'))
fig.show()


