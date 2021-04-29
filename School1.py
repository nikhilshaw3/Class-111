import plotly.express as px
import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go


df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()

mean_list = []

mean_of_sample_2 = statistics.mean(data)
print(mean_of_sample_2)

std_dv = statistics.stdev(data)
print(std_dv)

fig = ff.create_distplot([mean_list],["Students Marks"], show_hist = False)
fig.add_trace(go.Scatter(x =[mean,mean],y=[0,0.17],mode="lines",name = "MEAN"))

fig.add_trace(go.Scatter(x=[first_std_dv_end,first_std_dv_end],y=[0,0.017],mode="lines",name ="Standard Deviation 1 End"))
fig.add_trace(go.Scatter(x=[second_std_dv_end,second_std_dv_end],y=[0,0.017],mode="lines",name ="Standard Deviation 2 End"))

fig.show()