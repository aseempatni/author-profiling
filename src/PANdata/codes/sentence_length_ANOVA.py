import csv
import pandas as pd


#dictionary with author id as key and pos distribution as value
sentence_gender = {}
sentence_age = {}


column = {}
columnList = []
column['MALE']=[]
column['FEMALE']=[]
column['18-24']=[]
column['25-34']=[]
column['35-49']=[]
column['50-64']=[]
column['65-xx']=[]

ifile = open('sentence_length.csv')
reader = csv.reader(ifile)
i=0
for row in reader:
	if i==0:
		i=1
	else:
		value = float(row[3])/max(float(row[5]),1)
		column[row[1]].append(value)
		column[row[2]].append(value)

ifile.close()





no_of_rows = max([len(column['MALE']),len(column['FEMALE']),len(column['18-24']),len(column['25-34']),len(column['35-49']),len(column['50-64']),len(column['65-xx'])])
#creating a dataframe with author id as index and tags as columns
df = pd.DataFrame(data=0,index=[i+1 for i in range(no_of_rows)], columns=['MALE','FEMALE','18-24','25-34','35-49','50-64','65-xx'])
for key,value in column.items():
	df[key] = value+([0]*(no_of_rows-len(value)))

df.to_csv('sentenceLength_ANOVA.csv')
