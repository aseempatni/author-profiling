import pandas as pd
import csv

def normalized_csv(incsv, outcsv):

	df = pd.read_csv(incsv,index_col=0)

	df1 = df[['Age','Gender','Quotes','#Sentences','#NER','FleschKincaidGradeLevel','SMOGIndex','RIX','FleschReadingEase','ColemanLiauIndex','GunningFogIndex','ARI','LIX','#Hyperlinks','vocabulary','LengthSentences','FunctionWords']]

	cols = df.columns - df1.columns

	df.Quotes = df.Quotes/df['#Sentences']
	df['#NER'] = df['#NER']/df['vocabulary']


	df['FleschKincaidGradeLevel'] /= max(df['FleschKincaidGradeLevel'])
	df['SMOGIndex'] /= max(df['SMOGIndex'])
	df['RIX'] /= max(df['RIX'])
	df['FleschReadingEase'] /= max(df['FleschReadingEase'])
	df['ColemanLiauIndex'] /= max(df['ColemanLiauIndex'])
	df['GunningFogIndex'] /= max(df['GunningFogIndex'])
	df['ARI'] /= max(df['ARI'])
	df['LIX'] /= max(df['LIX'])




	for col in cols:
		df[col]/=df['#Sentences']
	df['#Hyperlinks'] /= df['#Sentences']
	df['FunctionWords'] /= df['vocabulary']
	df['LengthSentences'] /= df['#Sentences']
	df['#Sentences'] /= max(df['#Sentences'])
	df['vocabulary'] /= max(df['vocabulary'])

	# df.loc[df['Gender']=='female','Gender'] = 0
	# df.loc[df['Gender']=='male','Gender'] = 1

	for i in range(49):
		if i>=13 and i<=17:
			df.loc[df['Age']==i,'Age'] = 'a'
		elif i>=23 and i<=27:
			df.loc[df['Age']==i,'Age'] = 'b'
		elif i>=33 and i<=48:
			df.loc[df['Age']==i,'Age'] = 'c'


	df.to_csv(outcsv)
