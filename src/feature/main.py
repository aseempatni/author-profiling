import os
import csv
import punctuation as punctu
from string import punctuation
from utils import *
import pandas as pd
from collections import Counter
import pprint as pp
import NER_tagger
import pos_tagging
import html_links

directory = '../../data/pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'
outdir = 'output/'

author = get_author_info(directory+'/truth.txt')
authorFileNames = os.listdir(directory)

def links():

    ofile = open(outdir+'output.csv','w')

    writer = csv.writer(ofile)
    writer.writerow(['',"Gender","Age","#Hyperlinks","#Sentences"])

    males = 0
    females = 0
    links_from_males = 0
    links_from_females = 0

    for file in filter_xml(authorFileNames):
        hyperlinks_info = html_links.get_hyperlink_info(directory+'/'+file)
        author_id = os.path.basename(file).split('.')[0]
        writer.writerow([author_id,author_truth[author_id][0],author_truth[author_id][1],hyperlinks_info[0],hyperlinks_info[1]])
        if author_truth[author_id][0] == "MALE":
            males = males+1
            links_from_males = links_from_males+hyperlinks_info[0]
        else:
            females = females+1
            links_from_females = links_from_females+hyperlinks_info[0]

    ofile.close()

    print males,links_from_males
    print females,links_from_females


def punc(author):

    for file in filter_xml(authorFileNames):
        author_id = file.split('.')[0]
        file_path = directory+"/"+file
        author[author_id]['punctuation'] = punctu.extract_from_xml(file_path)
        # This part is incomplete

    df = pd.DataFrame(data=0,index = author.keys(),columns = ['Gender','Age']+list(punctuation)+['Vocabulary'])

    for authorId,punctuations in author.items():
        df.loc[authorId,'Gender'] = author_truth[authorId][0]
        df.loc[authorId,'Age'] = author_truth[authorId][1]
        for punct,count in punctuations.items():
            df.loc[authorId,punct] = count

    df.fillna(0)

    df.to_csv(outdir+'punctuation_distribution.csv')


def main(author):

    for file in filter_xml(authorFileNames):
        author_id = file.split('.')[0]
        file_path = directory+"/"+file

        # Get features
        author[author_id]['punctuation'] = punctu.extract_from_xml(file_path)
        author[author_id]['hyperlinks_info'] = html_links.get_hyperlink_info(file_path)
        author[author_id]['pos'] = pos_tagging.distribution(pos_tagging.get_POS_Tags(file_path))
        author[author_id]['NER'] = NER_tagger.get_NER_tags(file_path)
        break
    pp.pprint(author['d2a64c8cda3ca7eb0a29f38a9ee59a71'])

main(author)
