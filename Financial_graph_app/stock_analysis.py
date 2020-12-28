import datetime
from pandas_datareader import data
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.embed import components # to import to a website html file
from bokeh.resources import CDN # to dynamicaly generate needed version info

def status_set(opened, closed):
    if opened > closed:
        value = 'Decreased'
    elif opened < closed:
        value = 'Increased'
    else:
        value = 'Equal'
    return value

# file
f = r'result.html'


# Gets data from supported sites (yahoo, etc)
start = datetime.datetime(2019, 12, 1) # inclusive
end = datetime.datetime.now()
# returns a pandas data frame 
stock = 'AAPL'
df = data.DataReader(name=stock, data_source='yahoo', start=start, end=end)

# Set up graph
p = figure(x_axis_type='datetime', width=1000, height=500, sizing_mode='scale_width')
p.title.text = stock
p.xaxis.axis_label = 'Time'
p.yaxis.axis_label = '$ US'
p.grid.grid_line_alpha = 0.3

# Plot the line segment for the delta between high and low
# (upper left point on x, upper left point on y, bottom right point on x, bottom right point on y)
p.segment(x0=df.index, y0=df.High, x1=df.index, y1=df.Low, color='grey')

# add a new colum to df for status
df["Status"] = [status_set(o, c) for o, c in zip(df.Open, df.Close)]
# add new column to hold the average/middle value - mid between open and close
df["Mid"] = (df.Open + df.Close) / 2
# calculate hight and add to dataframe
df['Height'] = abs(df.Close - df.Open)

# Can perform a search based on value comparisons, ex. finding all dates where the close value was more than open
increased = df.index[df.Close > df.Open]
decreased = df.index[df.Close < df.Open]
# Can build the candle graph using quadrants or rectangles
# Using quad

# Using rect
    #plot.rect(x=[1, 2, 3], y=[1, 2, 3], width=10, height=20, color="#CAB2D6",
    #width_units="screen", height_units="screen")
hours_12 = 12 * 60 * 60 * 1000 # 12h in ms
# NOTE FIXME Create rectangles for days the value went up
p.rect(x=increased, y=df.Mid[df.Status == 'Increased'], width=hours_12, height=df.Height[df.Status == 'Increased'], color='green')
# Create rect for the days that went down
p.rect(x=decreased, y=df.Mid[df.Status == 'Decreased'], width=hours_12, height=df.Height[df.Status == 'Decreased'], color='red')

#output_file(f)
# add to other html file
# get the js script info and html script
script1, div1 = components(p) # returns a tuple
# get the specific file from host
cdn_js = CDN.js_files[0] # only need first, other is for more advanced func
cdn_css = CDN.css_files[0]

