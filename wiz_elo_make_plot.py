#-- Generate interactive plot --#

# Import 'bokeh' for plotting and interactive features
import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource, save
from bokeh.models import HoverTool

# Import data source
wiz = pd.read_csv("wiz_elo_2017_2018.csv")

# Convert datetime column from string to datetime
wiz["datetime"] = pd.to_datetime(wiz["date"], format="%Y-%m-%d")

# User inputs plot_width and plot_height
width = int(input("plot_width (pixels): "))
height = int(input("plot_height (pixels): "))

# User set output file name
html = input("html output filename: ")

output_file(html, title="Infographic: Washington Wizards 2017-18 Elo Ratings")

# RGB color codes for Washington Wizards' branding
navy = (0,43,92)
red = (227,24,55)
silver = (196,206,212)

# Pass data to the viz
source = ColumnDataSource(data=dict(
    x=wiz["datetime"],
    y=wiz["wiz_elo"],
    date=wiz["date"],
    score1=wiz["score1"],
    score2=wiz["score2"],
    HOME=wiz["team1"],
    AWAY=wiz["team2"],
    RESULT=wiz["result"]
))

# Customize HoverTool display
hover = HoverTool(
    tooltips=[
        ("Elo rating", "@y{0}"),
        ("Wiz Result", "@RESULT"),
        ("Date","@date"),
        ("Home", "@HOME, @score1"),
        ("Away", "@AWAY, @score2")
    ],
    mode='vline' # HoverTool displays when mouse is at same x-location as a data point (vline)
)

# Configure toolbar
TOOLS = [hover,"save"]

# Create plot figure object
p = figure(x_axis_type="datetime",tools=TOOLS, plot_width=width, plot_height=height,
           #y_axis_label="Elo Rating",
           #x_axis_label="Time",
          y_range=(1450,1600),
           #toolbar_location = "above",
           title="Infographic: Washington Wizards 2017-18 Elo Ratings"
          )

# Label axes
p.xaxis.axis_label_text_color = navy
p.xaxis.axis_label_text_font_style = "bold"

p.yaxis.axis_label_text_color = navy
p.yaxis.axis_label_text_font_style = "bold"

# Configure Title
p.title.text_font_style = "bold"
p.title.text_color = navy
p.title.align = "center"

# Remove gridlines
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# Remove minor tick lines
p.xaxis.minor_tick_line_color = None
p.yaxis.minor_tick_line_color = None

# Render line
p.line(wiz["datetime"], wiz["wiz_elo"], line_width=2, color=navy)

# Circle markers
p.circle('x', 'y', color=red, size=5, source=source)

save(p) # Export plot