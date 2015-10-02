# Plot graph for Punctuations and POS 

import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def distribute_age(data):
    age_1 = []
    age_2 = []
    age_3 = []
    age_4 = []
    age_5 = []
    for row in data:
        if row['Age']=='18-24':
            age_1.append(row)
        elif row['Age']=='25-34':
            age_2.append(row)
        elif row['Age']=='35-49':
            age_3.append(row)
        elif row['Age']=='50-64':
            age_4.append(row)
        elif row['Age']=='65-xx':
            age_5.append(row)

    return age_1,age_2,age_3,age_4,age_5

def getdist(data,col):
    dict = {}
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

def extract_i_col(arr,i,normaliseBy=None):
    if normaliseBy:
        return [(float(x[i])*100)/max(int(x[normaliseBy]),1) for x in arr]
    else:
        return [int(x[i]) for x in arr]

def get_mean_var(arr):
    return np.mean(arr),np.var(arr)


def getCDF(data):
    ageCDF = dict.fromkeys(['18-24','25-34','35-49','50-64','65-xx'],[])
    skip = ['','Gender','Age','Vocabulary']
    i=0
    for row in data:
        if i==0:
            i=1
        else:
            count=0
            if len(ageCDF[row['Age']])==0:
                ageCDF[row['Age']] = [0]*(len(row)-len(skip)+1)
            for key,value in row.items():
                if key not in skip and int(value)>0:
                    count=count+1
            for i in range(count+1):
                ageCDF[row['Age']][i] = ageCDF[row['Age']][i]+1

    return ageCDF







feature = 'Punctuation'
tagList = []

with open('../StructuredData/'+feature+'.csv') as csvfile:
    spamreader = csv.DictReader(csvfile)

    male, female = distribute_gender(spamreader)

    tagList = spamreader.fieldnames[3:len(spamreader.fieldnames)-1]

    menMean =[np.mean(extract_i_col(male,tag,'Vocabulary')) for tag in tagList]
    menStd =[np.std(extract_i_col(male,tag,'Vocabulary')) for tag in tagList]

    womenMean =[np.mean(extract_i_col(female,tag,'Vocabulary')) for tag in tagList]
    womenStd =[np.std(extract_i_col(female,tag,'Vocabulary')) for tag in tagList]

    csvfile.seek(0)
    ageDist = distribute_age(spamreader)

    csvfile.seek(0)
    ageCDF = getCDF(spamreader)    






ind = np.arange(len(tagList))
width = 0.4      # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMean,   width, color='r')
p2 = plt.bar(ind+width, womenMean,   width, color='y')




plt.ylabel(feature)
plt.title(feature)
plt.xticks(ind+width, tagList )
plt.legend( (p1, p2), ('Men', 'Women') )
plt.show()


# ageMeans = [[np.mean(extract_i_col(age,tag,'Vocabulary')) for tag in tagList] for age in ageDist]
# ageStd = [[np.std(extract_i_col(age,tag,'Vocabulary')) for tag in tagList] for age in ageDist]

# ind = np.arange(len(tagList))  # the x locations for the groups
# width = 0.4       # the width of the bars


# fig, ax = plt.subplots()
# rects = [0]*5
# color = ['b','g','r','k','y']
# for i in range(len(ageDist)):
#     if i==0:
#         rects[i] = ax.bar(ind, ageMeans[i], width, color=color[i])
#     else:
#         rects[i] = ax.bar(ind, ageMeans[i], width, color=color[i], bottom = ageMeans[i-1])



# # add some text for labels, title and axes ticks
# ageLabels = ['18-24','25-34','35-49','50-64','65-xx']
# ax.set_ylabel(feature)
# ax.set_title(feature)
# ax.set_xticks(ind+width/2.0)
# ax.set_xticklabels(tagList)
# plt.legend( rects, ageLabels )
# # plt.savefig(feature+'_Age.png')
# plt.show()


ind = np.arange(len(tagList))  # the x locations for the groups

fig, ax = plt.subplots()

plots = dict.fromkeys(ageCDF.keys())
color = {'18-24':'r','25-34':'y','35-49':'g','50-64':'b','65-xx':'k'}
legend_line = []
legend_label = []

for key,value in ageCDF.items():
    y = [float(value[i])/max(value[0],1) for i in range(0,len(value))]
    plots[key], = ax.plot([x for x in range(len(value))],y,color = color[key],linewidth=2.0,label=key)
    legend_line.append(plots[key])
    legend_label.append(key)




# add some text for labels, title and axes ticks
plt.legend(legend_line,legend_label)
ax.set_ylabel('CDF of types of punctuations used')
ax.set_xlabel('#Types of punctuations used')
ax.set_title('CDF '+feature)

plt.savefig(feature+' CDF.png')
plt.show()
