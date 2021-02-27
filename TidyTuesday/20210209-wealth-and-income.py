
import pandas as pd
import numpy as np

lifetime_earn = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/lifetime_earn.csv')
student_debt = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/student_debt.csv')
retirement = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/retirement.csv')
home_owner = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/home_owner.csv')
race_wealth = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/race_wealth.csv')
income_time = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/income_time.csv')
income_limits = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/income_limits.csv')
income_aggregate = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/income_aggregate.csv')
income_distribution = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/income_distribution.csv')
income_mean = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-09/income_mean.csv')

####################### parallel categories plot ###########################

import plotly.express as px
fig = px.parallel_categories(lifetime_earn, 
    color="lifetime_earn", color_continuous_scale=px.colors.sequential.Inferno,
    labels={'gender':'Gender', 'race':'Race', 'lifetime_earn':'Lifetime Earnings (US$)'})
fig.update_layout(
    #autosize=False,
    #width=950,
    #height=1100,
    #showlegend=False,
    #legend_title="Legend Title",
    title="Average lifetime earning by race/gender",
    #title_text='Your title', 
    title_x=0.5,
    #xaxis_title="Year",
    #yaxis_title="Percent of population (persons age 25 and over)",
    )
fig.update(
    #layout_showlegend=False,
    layout_coloraxis_showscale=False,
    )
annotations=[]
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                        xanchor='center', yanchor='top',
                        text='#TidyTuesday - 2021/02/09 | twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com/',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
fig.update_layout(annotations=annotations)
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
        y_data.append(df[df[y_axis_field]==y_axis_labels[i]].loan_debt_pct.values.tolist())
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
            name=labels[i],
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
    for y_trace, label, color in zip(y_data, labels, colors):
        # labeling the left_side of the plot
        annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                    xanchor='right', yanchor='middle',
                                    text=label + ' {}%'.format(y_trace[0]),
                                    font=dict(family='Arial', size=12),
                                    showarrow=False))
        # labeling the right_side of the plot
        annotations.append(dict(xref='paper', x=0.95, y=y_trace[9],
                                    xanchor='left', yanchor='middle',
                                    text='{}%'.format(y_trace[9]),
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
student_debt.loan_debt_pct = student_debt.loan_debt_pct.round(2)
# call the plotting funciton
vp_line_plot(student_debt, 'year', 'race', 'loan_debt_pct', 'Average family student loan debt for aged 25-55, by race')

######################## in-built line plot function ###########################

# Alternatively we could have used the inbuilt line plot with less customization
import plotly.express as px
fig = px.line(student_debt, x="year", y="loan_debt", color='race')
fig.show()

