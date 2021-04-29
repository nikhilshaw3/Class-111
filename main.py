import plotly.express as px
import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data],["Math Score"],show_hist = False)
fig.show()

mean = statistics.mean(data)
std_dv = statistics.stdev(data)

print('Mean of the data is ',mean)
print('Std_dv of the data is' , std_dv)