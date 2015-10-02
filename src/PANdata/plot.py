# Plot graph for various statistics

import numpy as np
import csv
import matplotlib.pyplot as plt

def distribute_age(data):
    age_1 = []
    age_2 = []
    age_3 = []
    age_4 = []
    for row in data:
        if row[2]=='25-34':
            age_1.append(row)
        elif row[2]=='35-49':
            age_2.append(row)
        elif row[2]=='50-64':
            age_3.append(row)
        elif row[2]=='65-xx':
            age_4.append(row)

    return age_1,age_2,age_3,age_4

def getdist(data,col):
    dict = {}
    #dict = {"25-34":[].
    for row in data:
        if row['Age'] in dict:
            dict[row['Age']].append(int(row[col]))
        else :
            dict[row['Age']] = [int(row[col])]
    return dict


def distribute_gender(data):
    male = []
    female = []
    for row in data:
        if row['Gender']=='MALE':
            male.append(row)
        elif row['Gender']=='FEMALE':
            female.append(row)
    return male,female

def extract_i_col(arr,i):
    return [int(x[i]) for x in arr]

def get_mean_var(arr):
    return np.mean(arr),np.var(arr)
with open('StructuredData/NER_distribution.csv', 'rb') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    male, female = distribute_gender(spamreader)
    dist =  getdist(male,'# NER')
    menMeans =[np.mean(dist[key])for key in dist]
    menStd =[np.std(dist[key])for key in dist]

    dist2 =  getdist(female,'# NER')
    womenMeans =[np.mean(dist2[key])for key in dist2]
    womenStd =[np.std(dist2[key])for key in dist2]

#exit()

N = 5
#menMeans   = (20, 35, 30, 35,1)
#womenMeans = (25, 32, 34, 20,1)
#menStd     = (2, 3, 4, 1,1)
#womenStd   = (3, 5, 2, 3,1)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans,   width, color='r', yerr=womenStd)
p2 = plt.bar(ind, womenMeans, width, color='y',
                     bottom=menMeans, yerr=menStd)
#p1 = plt.bar(ind, mean,   width, color='r', yerr=std)
#p2 = plt.bar(ind, mean2, width, color='y',
#                     bottom=menMeans, yerr=std2)

plt.ylabel('Non vocab words')
plt.title('NER')
plt.xticks(ind+width/2., ('18-25','25-34', '35-49', '50-64', '65-xx') )
#plt.yticks(np.arange(0,81,10))
plt.legend( (p1[0], p2[0]), ('Men', 'Women') )
plt.savefig('tnp')
plt.show()



N = 5
#menMeans = (20, 35, 30, 35, 27)
#menStd =   (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

#womenMeans = (25, 32, 34, 20, 25)
#womenStd =   (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)

# add some text for labels, title and axes ticks
ax.set_ylabel('NER')
ax.set_title('NER')
ax.set_xticks(ind+width)
ax.set_xticklabels(dist.keys() )

ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
            ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.savefig('bar.eps')
plt.show()
