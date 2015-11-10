# Get features related to hyperlink
import nltk
from xml.dom import minidom
import os
import csv
import re
from utils import *

directory = '../../data/pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'

def get_hyperlink_feature(document):
    for document in rawdocuments:
        no_of_hyperlinks = no_of_hyperlinks + document.firstChild.nodeValue.count("<a href=")
        text = removeTag_CDATA_section(document.firstChild.nodeValue.strip())
        temp = text.replace('?','.')
        sentences = temp.split('.')
        total_sentence = total_sentence + len(sentences)
    if total_sentence<no_of_hyperlinks:
            total_sentence = no_of_hyperlinks
    return (no_of_hyperlinks,total_sentence)


def get_hyperlink_info(docs):
    no_of_hyperlinks = 0
    total_sentence = 0 
    for doc in docs:
        no_of_hyperlinks = no_of_hyperlinks + doc.count("urlLink")
        text = removeTag_CDATA_section(doc.strip())
        total_sentence = total_sentence + len(nltk.tokenize.sent_tokenize(text))
    if total_sentence<no_of_hyperlinks:
            total_sentence = no_of_hyperlinks
    return (no_of_hyperlinks,total_sentence)


def main():
    authorFileNames = os.listdir(directory)

    ofile = open('hyperlinks.csv','w')
    ifile = open(directory+'/truth.txt','r')
    truth_data = ifile.readlines()
    author = {}
    for line in truth_data:
        element = line.strip().split(":::")
        author[element[0]] = [element[1],element[2]]


    writer = csv.writer(ofile)
    writer.writerow(['',"Gender","Age","#Hyperlinks","#Sentences"])


    males = 0
    females = 0
    links_from_males = 0
    links_from_females = 0


    for file in authorFileNames:
        if file.endswith(".xml"):
            hyperlinks_info = get_hyperlink_info(file)
            author_id = os.path.basename(file).split('.')[0]
            writer.writerow([author_id,author[author_id][0],author[author_id][1],hyperlinks_info[0],hyperlinks_info[1]])
            if author[author_id][0] == "MALE":
                males = males+1
                links_from_males = links_from_males+hyperlinks_info[0]
            else:
                females = females+1
                links_from_females = links_from_females+hyperlinks_info[0]


    ifile.close()
    ofile.close()

    print males,links_from_males
    print females,links_from_females

if __name__ =="__main__":
    main()
