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

    data = tagged_data

    #list of all tags
    tagList = []

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
