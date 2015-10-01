from xml.dom import minidom
import os
import csv
import re
import pandas as pd
import nltk
from utils import *

directory = 'pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'

authorFileNames = os.listdir(directory)


author = {}
for file in authorFileNames:
    if file.endswith(".xml"):
        file_path = directory+"/"+file
        xmldoc = minidom.parse(file_path)
        rawdocuments = xmldoc.getElementsByTagName('document')
        length = 0
        vocabulary = set()
        text=""
        no_of_sentences=0
        for document in rawdocuments:
            text = removeTag_CDATA_section(document.firstChild.nodeValue.strip())
            sentences = nltk.tokenize.sent_tokenize(text)
            for sentence in sentences:
                length = length + len(sentence.split())
            if vocabulary:
                vocabulary.update(set(text.split()))
            else:
                vocabulary = set(text.split())
            no_of_sentences = no_of_sentences+len(sentences)
        if vocabulary:
            author[file.split('.')[0]] = [length,len(vocabulary),no_of_sentences]
        else:
            author[file.split('.')[0]] = [length,0,no_of_sentences]



ifile = open('truth.txt')
truth_data = ifile.readlines()
author_info = {}
for line in truth_data:
    element = line.strip().split(":::")
    author_info[element[0]] = [element[1],element[2]]
ifile.close()



df = pd.DataFrame(data=0,index = author.keys(),columns = ['Gender','Age Group','Total Length of sentences','Vocabulary','No of sentences'])

for authorId,sentence_info in author.items():
    df.loc[authorId,'Gender'] = author_info[authorId][0]
    df.loc[authorId,'Age Group'] = author_info[authorId][1]
    df.loc[authorId,'Total Length of sentences'] = author[authorId][0]
    df.loc[authorId,'Vocabulary'] = author[authorId][1]
    df.loc[authorId,'No of sentences'] = author[authorId][2]

df.fillna(0)

df.to_csv('sentence_length.csv')
