import nltk
from xml.dom import minidom
import os
import re
from utils import *
from string import punctuation

directory = 'pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'


def get_POS_Tags(file_path):
    author = {}
    xmldoc = minidom.parse(file_path)
    rawdocuments = xmldoc.getElementsByTagName('document')
    documents = []
    for document in rawdocuments:
        doc = {}
        text = document.firstChild.nodeValue.strip()
        text = removeTag_CDATA_section(text)
        tokens = nltk.word_tokenize(text)
        doc["pos_tags"] = nltk.pos_tag(tokens)
        documents.append(doc)
    author['documents'] = documents
    return author

def distribution(tagged_data):
    #with open('POStags.txt') as data_file:
    # 	data = json.load(data_file)

    #i=0
    data = tagged_data
    #vocabulary={}
    #vocabFile = open('NER_distribution.csv')
    #reader = csv.reader(vocabFile)
    #for row in reader:
    #	if i==0:
    #		i=1
    #	else:
    #		vocabulary[row[0]] = int(row[4])
    #vocabFile.close()


    #list of all tags
    tagList = []

    #dictionary with author id as key and pos distribution as value
    pos_distribution = {}
    values = data.values()
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
    return tag_dict


    #for i in range(len(data)):
    #	values = data[i].values()
    #	tag_dict = {}
    #	for j in range(len(values[0])):
    #		tags = values[0][j]['pos_tags']
    #		for tag in tags:
    #			if tag[1] not in punctuation and tag[1]!="''" and tag[1]!="``":
    #				if tag_dict.has_key(tag[1])==False:
    #					tag_dict[tag[1]]=1
    #				else:
    #					tag_dict[tag[1]]=tag_dict[tag[1]]+1
    #				if tag[1] not in tagList:
    #					tagList.append(tag[1])
    #    return tag_dict
    #	pos_distribution[values[1]] = tag_dict

    #return pos_distribution

    #ifile = open('truth.txt')
    #truth_data = ifile.readlines()
    #author_info = {}
    #for line in truth_data:
    #    element = line.strip().split(":::")
    #    author_info[element[0]] = [element[1],element[2]]
    #ifile.close()


    ##creating a dataframe with author id as index and tags as columns
    #df = pd.DataFrame(data=0,index = pos_distribution.keys(),columns = ['Gender','Age']+tagList+['Vocabulary'])

    #for authorId,tags in pos_distribution.items():
    #	df.loc[authorId,'Gender'] = author_info[authorId][0]
    #	df.loc[authorId,'Age'] = author_info[authorId][1]
    #	df.loc[authorId,'Vocabulary'] = vocabulary[authorId]
    #	for tag,count in tags.items():
    #		df.loc[authorId,tag] = count

    #df.fillna(0)

    #df.to_csv('pos_distribution.csv')


def main():
    authorFileNames = os.listdir(directory)

    authors = []
    for file in authorFileNames:
        if file.endswith(".xml"):
            author = get_POS_Tags(file)
            authors.append(author)

    import json
    with open('POStags.txt', 'w') as outfile:
        json.dump(authors, outfile)
