import nltk
from xml.dom import minidom
import os
import re
from utils import *
from string import punctuation

directory = 'pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'


def get_POS_Tags(docs):
    tagList = []
    for doc in docs:
        text = doc.strip()
        text = removeTag_CDATA_section(text)
        tokens = nltk.word_tokenize(text)
        tagList.append(nltk.pos_tag(tokens))
    return tagList

def distribution(tagged_data):
    tag_dict = {}
    for i in range(len(tagged_data)):
        for tag in range(len(tagged_data[i]))
    		if tag[1] not in punctuation and tag[1]!="''" and tag[1]!="``":
    			if tag_dict.has_key(tag[1])==False:
    				tag_dict[tag[1]]=1
    			else:
    				tag_dict[tag[1]]=tag_dict[tag[1]]+1
    return tag_dict


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
