import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
import pandas as pd
import math
import matplotlib.dates as mdates
import datetime
import os

path = os.getcwd() + "/"
csv_file_name = path + "Spanish Time Log.csv"

title = "Spanish Study Time"
xlabel = "Date"
ylabel = "Cumulative Time in hours"
plt.style.use('ggplot')

# Read File
data = pd.read_csv(csv_file_name)
data["total_time"] = data["time_out"] - data["time_in"]
data = data.drop("task_out", axis=1)
data = data.rename(columns={'task_in' : 'task'})

######## Matplotlib ###########

# Pie Chart
cols = ['task', 'total_time']
categories = data[cols].groupby('task').sum().sort('total_time')
categories["total_time_hours"] = categories['total_time']/3600.0
categories["total_time_hours"].plot(kind='pie', subplots="True", figsize=(8,8))
##plt.show()
plt.savefig(path + "study_time_pie.png")
print categories

# Line Plot
time_out = data['time_out'].tolist()
time_in = data['time_in'].tolist()
times = time_in + time_out
times.sort()
total_time = data['total_time'].tolist()
cum_time = []
last_time = 0
time_hours = 0
for i in range(len(total_time)):
    cum_time.append(time_hours) # Time in
    time_hours = (last_time) + total_time[i]/3600.0
    cum_time.append(time_hours) # Time out
    last_time = time_hours

print "Total hours studied:", cum_time[-1]

dates = mdates.epoch2num(times)


days = mdates.DayLocator(interval = 4)
#weeks = mdates.WeekLocator()
##daysFmt = mdates.DateFormatter('%d')
daysFmt = mdates.DateFormatter('%Y-%m-%d')

##plt.plot(time_out, cum_time)
fig, ax = plt.subplots()
ax.plot(dates, cum_time)
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(daysFmt)
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
fig.autofmt_xdate()
plt.show()
#plt.savefig(path + "cumulative_study_time.png")

####### Plot.ly ##########
