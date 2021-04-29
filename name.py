import plotly.express as px
import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
print(mean)
std_dv = statistics.stdev(data)
print(std_dv)

def random_set_of_mean(counter):
    data_set = []
    
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    return mean

mean_list = []

for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

std_dv = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print('Mean of the data is ' , mean)
print('Std_dv of the data is ', std_dv)

first_std_dv_start,first_std_dv_end = mean-std_dv,mean+std_dv
second_std_dv_start,second_std_dv_end = mean-(2*std_dv),mean+(2*std_dv)
third_std_dv_start,third_std_dv_end = mean-(3*std_dv),mean+(3*std_dv)


fig = ff.create_distplot([mean_list],["Students Marks"], show_hist = False)
fig.add_trace(go.Scatter(x =[mean,mean],y=[0,0.17],mode="lines",name = "MEAN"))

fig.add_trace(go.Scatter(x=[first_std_dv_start,first_std_dv_start],y=[0,0.017],mode="lines",name ="Standard Deviation 1 Start"))
fig.add_trace(go.Scatter(x=[first_std_dv_end,first_std_dv_end],y=[0,0.017],mode="lines",name ="Standard Deviation 1 End"))

fig.add_trace(go.Scatter(x=[second_std_dv_start,second_std_dv_start],y=[0,0.017],mode="lines",name ="Standard Deviation 2 Start"))
fig.add_trace(go.Scatter(x=[second_std_dv_end,second_std_dv_end],y=[0,0.017],mode="lines",name ="Standard Deviation 2 End"))

fig.add_trace(go.Scatter(x=[third_std_dv_start,third_std_dv_start],y=[0,0.017],mode="lines",name ="Standard Deviation 3 Start"))
fig.add_trace(go.Scatter(x=[third_std_dv_end,third_std_dv_end],y=[0,0.017],mode="lines",name ="Standard Deviation 3 End"))

fig.show()