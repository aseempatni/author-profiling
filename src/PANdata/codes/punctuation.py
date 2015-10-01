from xml.dom import minidom
from string import punctuation
from collections import Counter
import os
import csv
import re
import pandas as pd
from utils import *


directory = 'pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'

authorFileNames = os.listdir(directory)


author = {}
for file in authorFileNames:
    if file.endswith(".xml"):
    	author_id = file.split('.')[0]
        file_path = directory+"/"+file
        xmldoc = minidom.parse(file_path)
        rawdocuments = xmldoc.getElementsByTagName('document')
        author[author_id] = dict.fromkeys(list(punctuation),0)
        author[author_id]['vocabulary'] = 0
        vocabulary = set()
        for document in rawdocuments:
            text = removeTag_CDATA_section(document.firstChild.nodeValue.strip())
            counts = Counter(text)
            for k,v in counts.iteritems():
                if k in punctuation:
                    author[author_id][k] = author[author_id][k] + v

            if vocabulary:
                vocabulary.update(set(text.split()))
            else:
                vocabulary = set(text.split())
        if vocabulary:
            author[author_id]['vocabulary'] = len(vocabulary)
        else:
            author[author_id]['vocabulary'] = 0



ifile = open('truth.txt')
truth_data = ifile.readlines()
author_info = {}
for line in truth_data:
    element = line.strip().split(":::")
    author_info[element[0]] = [element[1],element[2]]
ifile.close()



df = pd.DataFrame(data=0,index = author.keys(),columns = ['Gender','Age Group']+list(punctuation)+['vocabulary'])

for authorId,punctuations in author.items():
    df.loc[authorId,'Gender'] = author_info[authorId][0]
    df.loc[authorId,'Age Group'] = author_info[authorId][1]
    for punct,count in punctuations.items():
        df.loc[authorId,punct] = count

df.fillna(0)

df.to_csv('punctuation_distribution.csv')



