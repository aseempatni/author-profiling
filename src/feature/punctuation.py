from xml.dom import minidom
from string import punctuation
from collections import Counter
import os
import csv
import re
import pandas as pd
from utils import *


directory = '../../data/pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'

def extract_from_xml(docs):
    res = dict.fromkeys(list(punctuation),0)
    res['vocabulary'] = 0
    vocabulary = set()
    for doc in docs:
        text = removeTag_CDATA_section(doc.strip())
        counts = Counter(text)
        for k,v in counts.iteritems():
            if k in punctuation:
                res[k] = res[k] + v

        vocabulary.update(text.split())
    res['vocabulary'] = len(vocabulary)
    return res


def main():

    authorFileNames = os.listdir(directory)

    author = {}
    for file in authorFileNames:
        if file.endswith(".xml"):
            author_id = file.split('.')[0]
            file_path = directory+"/"+file
            author[author_id] = extract_from_xml(file_path)

    author_info = get_author_info(directory+'/truth.txt')

    df = pd.DataFrame(data=0,index = author.keys(),columns = ['Gender','Age']+list(punctuation)+['Vocabulary'])

    for authorId,punctuations in author.items():
        df.loc[authorId,'Gender'] = author_info[authorId][0]
        df.loc[authorId,'Age'] = author_info[authorId][1]
        for punct,count in punctuations.items():
            df.loc[authorId,punct] = count

    df.fillna(0)

    df.to_csv('punctuation_distribution.csv')

