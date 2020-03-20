import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% Unemployed")
    show(p)

links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

df_GDP = pd.read_csv(links['GDP'])
df_unemployment = pd.read_csv(links['unemployment'])

df_GDP.head()
df_GDP.shape
df_unemployment.head()
df_unemployment_up = df_unemployment[df_unemployment['unemployment']>=8.5]
df_unemployment_up.head()
x= df_GDP[['date']]
gdp_change = df_GDP[['change-current']]
unemployment = df_unemployment [['unemployment']]
title = 'US-Econimic'
file_name = "index.html"

make_dashboard(x=x, gdp_change=gdp_change, unemployment=unemployment, title=title, file_name=file_name)
