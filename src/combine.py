import json
import os
import pandas as pd
from string import punctuation
import yaml

def feature_csv():
	directory = 'output/'
	files = os.listdir(directory)
	data = {}
	posTagSet = set()
	punctuationSet = set()
	for file in files:
		with open(directory+file) as fp:
			json_data = yaml.safe_load(fp)
		data[file.split('.')[0]] = json_data
		posTagSet.update(json_data['pos'].keys())
		punctuationSet.update(json_data['punctuation'].keys())
		print file

	df = pd.DataFrame(data=0,index = data.keys(),columns = ['Gender','Age','Quotes','#Sentences','SentenceLength','#NER','FleschKincaidGradeLevel','SMOGIndex','RIX','FleschReadingEase','ColemanLiauIndex','GunningFogIndex','ARI','LIX','#Hyperlinks']+list(punctuationSet)+list(posTagSet))
	for author_id,feature in data.items():

		df.loc[author_id,'Gender'] = feature['Gender']
		df.loc[author_id,'Age'] = feature['Age']
		df.loc[author_id,'Quotes'] = feature['quotes'][1]
		df.loc[author_id,'#Sentences'] = feature['quotes'][0]
		# df.loc[author_id,'TopicVariance'] = feature['topic_var']
		df.loc[author_id,'SentenceLength'] = feature['sentence_length']
		df.loc[author_id,'#NER'] = feature['NER'][0]
		df.loc[author_id,'#Hyperlinks'] = feature['hyperlinks_info'][0]
		df.loc[author_id,feature['readability'].keys()] = feature['readability'].values()
		df.loc[author_id,feature['punctuation'].keys()] = feature['punctuation'].values()
		df.loc[author_id,feature['pos'].keys()] = feature['pos'].values()

	df.to_csv('test.csv')
