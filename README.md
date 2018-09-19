# Interactive Data Visualization

## Author
Chris Kendall

## Description
Python script to create a browser-based, interactive, data visualization featuring hover-over tooltips. The input is the CSV file. The output is an html file, which may be embedded.

## Example
This interactive may be viewed embedded on my webpage: https://www.chriskdata.com/portfolio/interactive

## Contents
- Python script to generate visualiation: wiz_elo_make_plot.py
- Cleaned data set: wiz_elo_2017_2018.csv

## Tools Used
- Python
  - Version: 3.6.5
  - Libaries: Bokeh, Pandas
- Development Environment
  - Jupyter Lab
  
## Original Data Source
The data is originally from FiveThirtyEight's NBA Elo dataset. The dataset featured in this repository is a subset of the FiveThirtyEight dataset with some columns added and changed column names.

## Data Description
Each row represents a different game played by the Washington Wizards in the 2017-18 NBA season (including playoffs).

The data has the following features:
- date: Date game played in YYYY-MM-DD (string)
- season: Year in which the NBA season ended. All values in this column are "2018".
- team1: Abbreviation for home team in the game played. (ex. "WAS" = Washington, "MIA" = Miami)
- team2: Abbreviation for visiting team in the game played.
- elo1_post: Elo rating for team1 calculated at the end of the game played.
- elo2_post: Elo rating for team2 calculated at the end of the game played.
- score1: Total points scored by team1.
- score2: Total points scored by team2.
- wiz_elo: Elo ratings only for Washington. If team1 is "WAS", wiz_elo corresponds to elo1_post. If "WAS" is team2, wiz_elo corresponds to elo2_post.
- result: Game outcome for the Wizards, denoted by "Win" or "Loss".
- datetime: This is a copy of the date column, the script converts this column's values from string to datetime (used to plot the x-axis)
