import nltk
from xml.dom import minidom
import os

directory = '../data/pan15-author-profiling-training-dataset-2015-04-23/pan15-author-profiling-training-dataset-english-2015-04-23'

def get_processed_author(authorFileName):
    author = {}
    file = directory+"/"+authorFileName
    xmldoc = minidom.parse(file)
    rawdocuments = xmldoc.getElementsByTagName('document')
    documents = []
    for document in rawdocuments:
        doc = {}
        doc["text"] = document.firstChild.nodeValue.strip()
        tokens = nltk.word_tokenize(doc["text"])
        doc["pos_tags"] = nltk.pos_tag(tokens)
        documents.append(doc)
    author['documents'] = documents
    author['id'] = authorFileName[:-4]
    print author['id']
    return author

authorFileNames = os.listdir(directory)

authors = []
for file in authorFileNames:
    if file.endswith(".xml"):
        author = get_processed_author(file)
        authors.append(author)

import json
with open('../data/data.txt', 'w') as outfile:
    json.dump(authors, outfile)

