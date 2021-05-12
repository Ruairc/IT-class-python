import statistics
from matplotlib import pyplot
import numpy as np

data=[]
file = open("crime_2004 - copy.csv","r")
data_1 = file.read()
file.close()

data=[]
file = open("crime_2005 - copy.csv","r")
data_2 = file.read()
file.close()

data=[]
file = open("crime_2006 - copy.csv","r")
data_3 = file.read()
file.close()

data=[]
file = open("crime_2014 - copy.csv","r")
data_4 = file.read()
file.close()

data=[]
file = open("crime_2015 - copy.csv","r")
data_5 = file.read()
file.close()

data=[]
file = open("crime_2016 - copy.csv","r")
data_6 = file.read()
file.close()



def cal(first):
    data_split=first.split("\n")

    data_split.remove(data_split[-1])
    data = [int(item) for item in data_split]


    mean_val=statistics.mean(data)
    print('The mean value is: ',mean_val)

    median_val=statistics.median(data)
    print('The median value is: ',median_val)

    value=[]
    valueCount=[]
    for item in data:
        if item not in value:
            value.append(item)

    for item in value:
        total=value.count(item)
        valueCount.append(total)
        
    maxFrequency=max(valueCount)
    maxFrequencyIndex=valueCount.index(maxFrequency)
    mode=value[maxFrequencyIndex]
    print("the mode is: ", mode)

    max_val=max(data)
    print('The max value is: ',max_val)

    min_val=min(data)
    print('The min value is: ',min_val)

print("2004's data is")
cal(data_1)

print("2005's data is")
cal(data_2)

print("2006's data is")
cal(data_3)

print("2014's data is")
cal(data_4)

print("2015's data is")
cal(data_5)

print("2016's data is")
cal(data_6)



mean_data = {'2004': 23.580071174377224,
            '2005': 24.2864768683274,
            '2006': 27.45373665480427,
            '2014': 26.95017793594306,
            '2015': 30.158362989323845,
            '2016': 6.862989323843417}
mean_data_1 = list(mean_data.values())
names = list(mean_data.keys())
group_mean = np.mean(mean_data_1)
fig, ax = plt.subplots()
ax.barh(names, mean_data)
plt.style.use('fivethirtyeight')
plt.show()



median_data = {'2004': 8.0,
        '2005': 8.0,
        '2006': 8.0,
        '2014': 7.0,
        '2015': 10.0,
        '2016': 2.0}
median_data_1 = list(median_data.values())
names = list(median_data.keys())
group_median = np.median(median_data_1)
fig, ax = plt.subplots()
ax.barh(names, median_data)
plt.style.use('fivethirtyeight')
plt.show()



mode_data = {'2004': 9,
        '2005': 12,
        '2006': 14,
        '2014': 12,
        '2015': 13,
        '2016': 4}
mode_data_1 = list(mode_data.values())
names = list(mode_data.keys())
fig, ax = plt.subplots()
ax.barh(names, mode_data)
plt.style.use('fivethirtyeight')
plt.show()



min_data = {'2004': 0,
        '2005': 0,
        '2006': 0,
        '2014': 0,
        '2015': 0,
        '2016': 0}
min_data_1 = list(min_data.values())
names = list(min_data.keys())
fig, ax = plt.subplots()
ax.barh(names, min_data)
plt.style.use('fivethirtyeight')
plt.show()



max_data = {'2004': 429,
        '2005': 391,
        '2006': 484,
        '2014': 520,
        '2015': 635,
        '2016': 158}
max_data_1 = list(max_data.values())
names = list(max_data.keys())
fig, ax = plt.subplots()
ax.barh(names, max_data)
plt.style.use('fivethirtyeight')
plt.show()

