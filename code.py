import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)
standard_deviation = statistics.stdev(data)

print("Mean:" , mean)
print("Mode:" , mode)
print("Median:" , median)
print("Standard Deviation:" , standard_deviation)

dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)


mean1 = statistics.mean(dataset)
standard_deviation1 = statistics.stdev(dataset)
print("Mean of random data:", mean1)
print("Standard Deviation of random data:", standard_deviation1 )

def random_set_of_mean(counter):
    dataset = []
    for a in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1.4],mode = "lines", name= "mean"))
    fig.show()
    
def setup():
    mean_list = []
    for b in range(1,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    std = statistics.stdev(mean_list)
    print("Mean of the sampling distribution:",mean)
    print("Standard Deviation of sampling data:", std)
setup()

