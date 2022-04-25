
import pandas as pd
import numpy as np

# df = pd.read_csv('Data/annual-working-hours-per-worker.csv')


# Alternative way of getting data
import sqlite3
con = sqlite3.connect(r'C:\Users\vivek\Documents\Code\local-items\30daychartchallenge-data\30daychartchallenge-data.sqlite3')
df = pd.read_sql_query("SELECT * from 'annual-working-hours-per-worker'", con)


# Preparing data
df2 = df.loc[df.Entity.isin(['China', 'India', 'United States', 'Brazil', 'Germany'])]
df2 = df2.loc[df2.Year>=1985]

# Plotting
import plotly.express as px
fig = px.line(df2, x="Year", y='Average annual working hours per worker', color="Entity", title='xxxxx')
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
#    fig.update_layout(title=title_field, title_x=0.5,)
    # Title
    fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.27,xanchor='center',yanchor='top', 
    font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
    text="Annual working hours per worker"))
    # Subtitle
    fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.14,xanchor='center',yanchor='top',
    font=dict(family='Arial',size=14,color='grey'),showarrow=False,
    text="Total hours worked in the economy as measured from primarily National Accounts data"))

    # Annotate
    annotations = []
    # Adding labels
    for y_trace, label, color in zip(y_data, y_axis_labels, colors):
        # labeling the left_side of the plot
        annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                    xanchor='right', yanchor='middle',
                                    text=label + ' {:,.0f}'.format(y_trace[0]),
                                    #text=label + ' {}%'.format(y_trace[0]),
                                    font=dict(family='Arial', size=12),
                                    showarrow=False))
        # labeling the right_side of the plot
        annotations.append(dict(xref='paper', x=0.95, y=y_trace[y_data[0].size-1],
                                    xanchor='left', yanchor='middle',
                                    text='{:,.0f}'.format(y_trace[y_data[0].size-1]),
                                    #text='{}%'.format(y_trace[y_data[0].size-1]),
                                    font=dict(family='Arial', size=12),
                                    showarrow=False))
    # Footnote
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.15,
                            xanchor='center', yanchor='top',
                            text='#30DayChartChallenge - historical - 2021/04/03 | https://ourworldindata.org/working-hours',
                            font=dict(family='Arial', size=12, color='grey'),
                            showarrow=False))
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.22,
                            xanchor='center', yanchor='top',
                            text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com/',
                            font=dict(family='Arial', size=12, color='grey'),
                            showarrow=False))
    fig.update_layout(annotations=annotations)
    # display chart
    fig.show()
    # End of vp_line_plot plotting function

vp_line_plot(df2, 'Year', 'Entity', 'Average annual working hours per worker', 'xxxxxx')


