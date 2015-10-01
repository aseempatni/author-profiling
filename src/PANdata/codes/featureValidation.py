import csv
from scipy import stats
import pandas as pd

ofile = open('ANOVA_result.csv','w')
writer = csv.writer(ofile)
writer.writerow(['Feature','Category1','Category2','f_Value','p_Value'])

def ANOVA(file,feature):
	df = pd.read_csv(file)
	f_value = 0.0 
	p_value = 0.0
	columns = df.columns
	for i in range(1,len(columns),7):
		f_value, p_value = stats.f_oneway(df[columns[i]],df[columns[i+1]])
		writer.writerow([feature,columns[i],columns[i+1],f_value,p_value])
		for j in range(i+2,i+7):
			for k in range(j+1,i+7):
				f_value, p_value = stats.f_oneway(df[columns[j]],df[columns[k]])
				writer.writerow([feature,columns[j],columns[k],f_value,p_value])
	writer.writerow([])
	writer.writerow([])
	writer.writerow([])




files = [('hyperLinks_ANOVA.csv','HyperLinks'),('sentenceLength_ANOVA.csv','Sentence Length'),('ner_ANOVA.csv','NER'),('pos_ANOVA.csv','POS'),('punctuation_ANOVA.csv','Punctuation')]

for file in files:
	ANOVA(file[0],file[1])

ofile.close()