from bokeh.plotting import figure, show, output_file
from bokeh.models import tickers, HoverTool, ColumnDataSource
import pandas
import datetime

#dtypes = {'motion_start' : datetime, 'montion_stop' : datetime}

# NOTE - get dataFrame as datetime object rather than generic object, otherwise the quad will not generate
df = pandas.read_csv(r'..\..\Motion_detection_app\logs\times.csv', parse_dates=['motion_start', 'motion_stop']) 
# create figure
fig = figure(x_axis_type='datetime', height=100, width=500, sizing_mode='scale_both', title='Motion Plot')
fig.yaxis.minor_tick_line_color=None
fig.yaxis.ticker.desired_num_ticks=1

# Format the str from the df to be more legable
df['Start_string']=df['motion_start'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['Stop_string']=df['motion_stop'].dt.strftime('%Y-%m-%d %H:%M:%S')
# Implement hovertools
cds = ColumnDataSource(df)
# Define the tooltips [('str to display', '@column name in df)]
hover = HoverTool(tooltips=[('Start', '@Start_string'), ('End', '@Stop_string')])
fig.add_tools(hover)

# Need to use quad to create sections
fig.quad(left='motion_start', right='motion_stop', bottom=0, top=1, color='red', source=cds)

output_file('motion_plot.html')
show(fig)
