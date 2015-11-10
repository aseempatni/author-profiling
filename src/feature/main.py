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
import countQuote
import topics_mean_stdev

from readability import readability as r

directory = '../../data/pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'
outdir = 'output/'

author = get_author_info(directory+'/truth.txt')
authorFileNames = os.listdir(directory)

def main(author):

    for file in filter_xml(authorFileNames):
        author_id = file.split('.')[0]
        file_path = directory+"/"+file

        # change to doc for Koppel
        docs = gettext(file_path)

        # Extract features and add them to the author object

        # change to send docs instead of filename
        author[author_id]['punctuation'] = punctu.extract_from_xml(file_path)
        author[author_id]['pos'] = pos_tagging.distribution(pos_tagging.get_POS_Tags(file_path))
        author[author_id]['NER'] = NER_tagger.get_NER_tags(file_path)

        author[author_id]['hyperlinks_info'] = html_links.get_hyperlink_info(file_path)
        author[author_id]["topic_var"] = topics_mean_stdev.getTopics(docs)
        author[author_id]["quotes"] = countQuote.getquotes(docs)
        text = """We are close to wrapping up our 10 week Rails Course. This week we will cover a handful of topics commonly encountered in Rails projects. We then wrap up with part 2 of our Reddit on Rails exercise!  By now you should be hard at work on your personal projects. The students in the course just presented in front of the class with some live demos and a brief intro to to the problems their app were solving. Maybe set aside some time this week to show someone your progress, block off 5 minutes and describe what goal you are working towards, the current state of the project (is it almost done, just getting started, needs UI, etc.), and then show them a quick demo of the app. Explain what type of feedback you are looking for (conceptual, design, usability, etc.) and see what they have to say.  As we are wrapping up the course you need to be focused on learning as much as you can, but also making sure you have the tools to succeed after the class is over."""
        # Readability scores
        rd = r.Readability(text)
        read = {}
        read["ARI"] = rd.ARI()
        read["FleschReadingEase"] = rd.FleschReadingEase()
        read['FleschKincaidGradeLevel'] = rd.FleschKincaidGradeLevel()
        read['GunningFogIndex'] = rd.GunningFogIndex()
        read['SMOGIndex'] = rd.SMOGIndex()
        read['ColemanLiauIndex'] = rd.ColemanLiauIndex()
        read['LIX'] = rd.LIX()
        read['RIX'] = rd.RIX()

        author[author_id]["readability"] = read

        # doing a break jsut to save testing time
        break

    # printing a sample
    pp.pprint(author['d2a64c8cda3ca7eb0a29f38a9ee59a71'])

main(author)



#def links():
#
#    ofile = open(outdir+'output.csv','w')
#
#    writer = csv.writer(ofile)
#    writer.writerow(['',"Gender","Age","#Hyperlinks","#Sentences"])
#
#    males = 0
#    females = 0
#    links_from_males = 0
#    links_from_females = 0
#
#    for file in filter_xml(authorFileNames):
#        hyperlinks_info = html_links.get_hyperlink_info(directory+'/'+file)
#        author_id = os.path.basename(file).split('.')[0]
#        writer.writerow([author_id,author_truth[author_id][0],author_truth[author_id][1],hyperlinks_info[0],hyperlinks_info[1]])
#        if author_truth[author_id][0] == "MALE":
#            males = males+1
#            links_from_males = links_from_males+hyperlinks_info[0]
#        else:
#            females = females+1
#            links_from_females = links_from_females+hyperlinks_info[0]
#
#    ofile.close()
#
#    print males,links_from_males
#    print females,links_from_females
#
#
#def punc(author):
#
#    for file in filter_xml(authorFileNames):
#        author_id = file.split('.')[0]
#        file_path = directory+"/"+file
#        author[author_id]['punctuation'] = punctu.extract_from_xml(file_path)
#        # This part is incomplete
#
#    df = pd.DataFrame(data=0,index = author.keys(),columns = ['Gender','Age']+list(punctuation)+['Vocabulary'])
#
#    for authorId,punctuations in author.items():
#        df.loc[authorId,'Gender'] = author_truth[authorId][0]
#        df.loc[authorId,'Age'] = author_truth[authorId][1]
#        for punct,count in punctuations.items():
#            df.loc[authorId,punct] = count
#
#    df.fillna(0)
#
#    df.to_csv(outdir+'punctuation_distribution.csv')
#
#
#
