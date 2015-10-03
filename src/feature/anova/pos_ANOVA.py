import csv
import pandas as pd



column = {}
columnList = []

pList = []
no_of_row=0


ifile = open('pos_distribution.csv')
reader = csv.reader(ifile)
i=0
for row in reader:
	if i==0:
		pList = row[3:len(row)-1]
		for j in range(3,len(row)-1):
			columnList.append('MALE_'+row[j])
			columnList.append('FEMALE_'+row[j])
			columnList.append('18-24_'+row[j])
			columnList.append('25-34_'+row[j])
			columnList.append('35-49_'+row[j])
			columnList.append('50-64_'+row[j])
			columnList.append('65-xx_'+row[j])
			column['MALE_'+row[j]]=[]
			column['FEMALE_'+row[j]]=[]
			column['18-24_'+row[j]]=[]
			column['25-34_'+row[j]]=[]
			column['35-49_'+row[j]]=[]
			column['50-64_'+row[j]]=[]
			column['65-xx_'+row[j]]=[]
		i=1
	else:
		for j in range(3,len(row)-1):
			value = (float(row[j])*100)/max(float(row[len(row)-1]),1)
			column[row[1]+'_'+pList[j-3]].append(value)
			column[row[2]+'_'+pList[j-3]].append(value)
			no_of_row = max([no_of_row,len(column[row[1]+'_'+pList[j-3]]),len(column[row[2]+'_'+pList[j-3]])])

ifile.close()





#creating a dataframe with author id as index and tags as columns
df = pd.DataFrame(data=0,index=[i for i in range(no_of_row)], columns=columnList)

for key,value in column.items():
	df[key] = value+([0]*(no_of_row-len(value)))

df.to_csv('pos_ANOVA.csv')
