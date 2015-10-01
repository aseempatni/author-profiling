import json
import csv
import pandas as pd
from string import punctuation


with open('POStags.txt') as data_file:
	data = json.load(data_file)

i=0

vocabulary={}
vocabFile = open('NER_distribution.csv')
reader = csv.reader(vocabFile)
for row in reader:
	if i==0:
		i=1
	else:
		vocabulary[row[0]] = int(row[4])
vocabFile.close()


#list of all tags
tagList = []

#dictionary with author id as key and pos distribution as value
pos_distribution = {}


for i in range(len(data)):
	values = data[i].values()
	tag_dict = {}
	for j in range(len(values[0])):
		tags = values[0][j]['pos_tags']
		for tag in tags:
			if tag[1] not in punctuation and tag[1]!="''" and tag[1]!="``":
				if tag_dict.has_key(tag[1])==False:
					tag_dict[tag[1]]=1
				else:
					tag_dict[tag[1]]=tag_dict[tag[1]]+1
				if tag[1] not in tagList:
					tagList.append(tag[1]) 
	pos_distribution[values[1]] = tag_dict


ifile = open('truth.txt')
truth_data = ifile.readlines()
author_info = {}
for line in truth_data:
    element = line.strip().split(":::")
    author_info[element[0]] = [element[1],element[2]]
ifile.close()


#creating a dataframe with author id as index and tags as columns
df = pd.DataFrame(data=0,index = pos_distribution.keys(),columns = ['Gender','Age']+tagList+['Vocabulary'])

for authorId,tags in pos_distribution.items():
	df.loc[authorId,'Gender'] = author_info[authorId][0]
	df.loc[authorId,'Age'] = author_info[authorId][1]
	df.loc[authorId,'Vocabulary'] = vocabulary[authorId]
	for tag,count in tags.items():
		df.loc[authorId,tag] = count

df.fillna(0)

df.to_csv('pos_distribution.csv')
