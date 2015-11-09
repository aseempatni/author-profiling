import nltk
from xml.dom import minidom
import os
import re
import csv
import pandas as pd
from utils import *


directory = 'pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'


def get_NER_tags(filename):
    xmldoc = minidom.parse(filename)
    rawdocuments = xmldoc.getElementsByTagName('document')
    ner_length = 0
    vocabulary = set()
    for document in rawdocuments:
        rawText = removeTag_CDATA_section(document.firstChild.nodeValue.strip())
        sent1 = nltk.word_tokenize(rawText)
        sent2 = nltk.pos_tag(sent1)
        sent3 = nltk.ne_chunk(sent2, binary=True)
        for item in sent3:
            if hasattr(item,'node'):
                ner_length = ner_length+len(item)
        if vocabulary:
            vocabulary.update(set(rawText.split()))
        else:
            vocabulary = set(rawText.split())
    if vocabulary:
        return (ner_length,len(vocabulary))
    else:
        return (ner_length,0)




def getAuthorInfo():
    ifile = open('truth.txt')
    truth_data = ifile.readlines()
    author_info = {}
    for line in truth_data:
        element = line.strip().split(":::")
        author_info[element[0]] = [element[1],element[2]]
    ifile.close()
    return author_info



def main():
    authorFileNames = os.listdir(directory)

    author = {}
    author_info = getAuthorInfo()

    for file in authorFileNames:
        if file.endswith(".xml"):
            key = file.split('.')[0]
            author[key] = get_NER_tags(file)


    df = pd.DataFrame(data=0,index = author.keys(),columns = ["Gender","Age",'#NER','Vocabulary'])
    for authorId,tagInfo in author.items():
        df.loc[authorId,'Gender'] = author_info[authorId][0]
        df.loc[authorId,'Age'] = author_info[authorId][1]
        df.loc[authorId,'#NER'] = author[authorId][0]
        df.loc[authorId,'Vocabulary'] = author[authorId][1]


    df.fillna(0)

    df.to_csv('NER_distribution.csv')

