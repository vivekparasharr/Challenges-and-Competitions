
import pandas as pd
import numpy as np

employed = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-23/employed.csv')
earn = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-23/earn.csv')


df.pivot(index='year',columns='industry',values='employed_pct')

employed.columns
df=employed[['industry', 'major_occupation', 'minor_occupation', 'race_gender', 'employed_pct']]
px.parallel_categories(employed)


import plotly.express as px
df = px.data.tips()
fig = px.box(df, x="race_gender", y="employed_pct")
fig.show()



############################################################################

import plotly.graph_objects as go

country = ['Switzerland (2011)', 'Chile (2013)', 'Japan (2014)',
           'United States (2012)', 'Slovenia (2014)', 'Canada (2011)',
           'Poland (2010)', 'Estonia (2015)', 'Luxembourg (2013)', 'Portugal (2011)']
voting_pop = [40, 45.7, 52, 53.6, 54.1, 54.2, 54.5, 54.7, 55.1, 56.6]
reg_voters = [49.1, 42, 52.7, 84.3, 51.7, 61.1, 55.3, 64.2, 91.1, 58.9]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=voting_pop,
    y=country,
    name='Percent of estimated voting age population',
    marker=dict(
        color='rgba(156, 165, 196, 0.95)',
        line_color='rgba(156, 165, 196, 1.0)',
    )
))
fig.add_trace(go.Scatter(
    x=reg_voters, y=country,
    name='Percent of estimated registered voters',
    marker=dict(
        color='rgba(204, 204, 204, 0.95)',
        line_color='rgba(217, 217, 217, 1.0)'
    )
))

fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=16))

fig.update_layout(
    title="Votes cast for ten lowest voting age population in OECD countries",
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(102, 102, 102)',
        tickfont_color='rgb(102, 102, 102)',
        showticklabels=True,
        dtick=10,
        ticks='outside',
        tickcolor='rgb(102, 102, 102)',
    ),
    margin=dict(l=140, r=40, b=50, t=80),
    legend=dict(
        font_size=10,
        yanchor='middle',
        xanchor='right',
    ),
    width=800,
    height=600,
    paper_bgcolor='white',
    plot_bgcolor='white',
    hovermode='closest',
)
fig.show()


####################### customized line plot function ###########################

def vp_line_plot(df, x_axis_field, y_axis_field, value_field, title_field):
    import plotly.graph_objects as go
    import numpy as np
    # sort the data in ascending order
    df = df.sort_values(by=[x_axis_field, y_axis_field]).reset_index(drop=True)
    # extract labels, categorical variable levels, y axis values
    x_axis_labels = df[x_axis_field].unique() 
    y_axis_labels = df[y_axis_field].unique() 
    y_axis_levels=y_axis_labels.size
    x_data = np.vstack((x_axis_labels,)*y_axis_levels) 
    y_data=[]
    for i in range(0, y_axis_levels):
        y_data.append(df[df[y_axis_field]==y_axis_labels[i]][value_field].values.tolist())
    y_data = np.array(y_data)
    # select colors to be used and line thickness of plot
    colors = ['firebrick','olive','dodgerblue','blueviolet','dimgrey','tomato','sienna','darkorange','forestgreen','steelblue','royalblue','orchid']
    selected_colors = colors[:y_axis_levels]
    mode_size = [8]*y_axis_levels
    line_size = [2]*y_axis_levels
    # create the plot
    fig = go.Figure()
    # Add lines to plot
    for i in range(0, y_axis_levels):
        fig.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
            name=y_axis_labels[i],
            line=dict(color=colors[i], width=line_size[i]),
            connectgaps=True,
        ))
        # endpoints
        fig.add_trace(go.Scatter(
            x=[x_data[i][0], x_data[i][-1]],
            y=[y_data[i][0], y_data[i][-1]],
            mode='markers',
            marker=dict(color=colors[i], size=mode_size[i])
        ))
    # update layout of chart
    fig.update_layout(
        xaxis=dict(showline=True, showgrid=False, 
            linecolor='rgb(204, 204, 204)', linewidth=2, 
            showticklabels=True, ticks='outside', 
            tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)',),),
        yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False,),
        autosize=False, showlegend=False, plot_bgcolor='white', 
        margin=dict(autoexpand=False, l=100, r=20, t=110,),
    )
    # Title
    fig.update_layout(title=title_field, title_x=0.5,)
    # Annotate
    annotations = []
    # Adding labels
    for y_trace, label, color in zip(y_data, y_axis_labels, colors):
        # labeling the left_side of the plot
        annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                    xanchor='right', yanchor='middle',
                                    text=label + ' {}%'.format(y_trace[0]),
                                    font=dict(family='Arial', size=12),
                                    showarrow=False))
        # labeling the right_side of the plot
        annotations.append(dict(xref='paper', x=0.95, y=y_trace[y_data.size-1],#change
                                    xanchor='left', yanchor='middle',
                                    text='{}%'.format(y_trace[y_data.size-1]),
                                    font=dict(family='Arial', size=12),
                                    showarrow=False))
    # Footnote
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.22,
                            xanchor='center', yanchor='top',
                            text='#TidyTuesday - 2021/02/09 | twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com/',
                            font=dict(family='Arial', size=12, color='grey'),
                            showarrow=False))
    fig.update_layout(annotations=annotations)
    # display chart
    fig.show()
    # End of vp_line_plot plotting function

# round the y data value 
employed['employed_pct']=round(employed.employ_n/employed.industry_total,2)

# call the plotting funciton
vp_line_plot(employed, 'year', 'race_gender', 'employed_pct', 'title')

employed.groupby[['year','industry']].mean()

employed.groupby('industry').count()['year']
employed[employed.industry=='Agriculture and related']\
    [employed.race_gender=='Asian'].employ_n.sum()

employed.groupby([['']])

