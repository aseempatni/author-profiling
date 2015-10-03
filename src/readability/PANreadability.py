import re
import codecs
import nltk
import sys
import os
from readability import Readability
from sklearn.feature_extraction.text import TfidfVectorizer
import lda
import numpy as np
from xml.dom import minidom
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
	#print ans
	return ans[:-1]

def getReadability():
	authorFileNames = os.listdir(directory)
	texts=[]
	authors=[]
	truth={}
	quote=[]
	sents=[]

	for file in authorFileNames:
		if file.endswith(".xml"):
			te=gettext(file)
			te.encode('ascii','ignore')
			texts.append(te)
			authors.append(file[:-4])
		else:
			fgh=open(directory+"/"+file,'r')
			fg=fgh.read().split('\n')[:-1]
			for r in fg:
				df=r.split(':::')[1:]
				truth[r.split(':::')[0]]=df
			fgh.close()

	f=open('PANreadibility.csv','w')
	f.write('ID,Gender,Age,ARI,FleschReadingEase,FleschKincaidGradeLevel,GunningFogIndex,SMOGIndex,ColemanLiauIndex,LIX,RIX\n')
	for i in range(len(authors)):
		sf=texts[i]
		rd = Readability(sf.encode('ascii','ignore'))
		f.write(authors[i]+','+truth[authors[i]][0]+','+truth[authors[i]][1]+','+str(rd.ARI())+','+str(rd.FleschReadingEase())+','+str(rd.FleschKincaidGradeLevel())+','+str(rd.GunningFogIndex())+','+str(rd.SMOGIndex())+','+str(rd.ColemanLiauIndex())+','+str(rd.LIX())+','+str(rd.RIX())+'\n')

	f.close()

def main():
	getReadability()

if __name__=="__main__":
	main()
