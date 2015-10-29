import sys
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import lda
import numpy as np
from xml.dom import minidom
import re
import codecs
import nltk
from alchemyapi import AlchemyAPI
import math

alchemyapi = AlchemyAPI()

if not sys.stdout.isatty():
	sys.stdout = codecs.getwriter('utf8')(sys.stdout)


directory='/home/bhushan/Documents/NLP_project/pan14-author-profiling-training-corpus-2014-04-16/blogs'

def removeTag_CDATA_section(text):
    processedText = re.sub(r'<[^>]*>','',text,0)
    processedText = re.sub(r'&amp;','&',processedText,0)
    processedText = re.sub(r'&ldquo;','"',processedText,0)
    processedText = re.sub(r'&rdquo;','"',processedText,0)
    processedText = re.sub(r'&rsquo;',"'",processedText,0)
    processedText = re.sub(r'&lsquo;',"'",processedText,0)
    processedText = re.sub(r'&nbsp;','',processedText,0)
    processedText = re.sub(r'[.][.]+',' ',processedText,0)
    return processedText

def gettext(file):
	file = directory+"/"+file
	xmldoc = minidom.parse(file)
	rawdocuments = xmldoc.getElementsByTagName('document')
	ans=""
	for document in rawdocuments:
		ans=ans+removeTag_CDATA_section(document.firstChild.nodeValue.strip())
		ans=ans+" "
	return ans[:-1]

def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers))
	return math.sqrt(variance)

def countQuotes():
	authorFileNames = os.listdir(directory)
	texts=[]
	authors=[]
	truth={}
	means=[]
	stdevs=[]

	for file in authorFileNames:
		if file.endswith(".xml"):
			te=gettext(file)
			texts.append(te.encode('ascii','ignore'))
			authors.append(file[:-4])
		else:
			fgh=open(directory+"/"+file,'r')
			fg=fgh.read().split('\n')[:-1]
			for r in fg:
				df=r.split(':::')[1:]
				truth[r.split(':::')[0]]=df
			fgh.close()

	for i in range(len(authors)):
		sf=texts[i]
		cx=[]
		response = alchemyapi.concepts('text', sf)
		if response['status'] == 'OK':
			for concept in response['concepts']:
				cx.append(float(concept['relevance']))
		if len(cx)==0:
			means.append(-1)
			stdevs.append(-1)
			continue
		means.append(mean(cx))
		stdevs.append(stdev(cx))

	f=open('topics_mean_stdev.csv','w')
	f.write('ID,Gender,Age,Mean,StDev\n')
	for i in range(len(authors)):
		f.write(authors[i]+','+truth[authors[i]][0]+','+truth[authors[i]][1]+','+str(means[i])+','+str(stdevs[i])+'\n')
	f.close()

def main():
	countQuotes()

if __name__=="__main__":
	main()
