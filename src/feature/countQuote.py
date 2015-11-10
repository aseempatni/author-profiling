import sys
import os
import numpy as np
from xml.dom import minidom
import re
import codecs
import nltk
#from readability import Readability

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
	xmldoc = minidom.parse(file)
	rawdocuments = xmldoc.getElementsByTagName('document')
	ans=""
	for document in rawdocuments:
		ans=ans+removeTag_CDATA_section(document.firstChild.nodeValue.strip())
		ans=ans+" "
	#print ans
	return ans[:-1]

def count_sents_in_quotes(text):
	v=len(nltk.tokenize.sent_tokenize(text))
	if v>1 or v==0:

		return v
	if text[-1]=='.' or text[-1]=='!' or text[-1]=='.' :
		return 1
	return 0

def countQuotes():
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

	for i in range(len(authors)):
		sf=texts[i]
		no_of_sents=len(nltk.tokenize.sent_tokenize(sf))
		sents.append(no_of_sents)
		l=re.findall(r'"[^"]*"',sf)
		no_of_quoted_sents=sum([count_sents_in_quotes(i) for i in l])
		quote.append(no_of_quoted_sents)

	f=open('quote.csv','w')
	f.write('ID,Gender,Age,Quotes,Sentences\n')
	for i in range(len(authors)):
		f.write(authors[i]+','+truth[authors[i]][0]+','+truth[authors[i]][1]+','+str(quote[i])+','+str(sents[i])+'\n')
	f.close()


def getquotes (filename) :
        sf = gettext(filename)
	no_of_sents=len(nltk.tokenize.sent_tokenize(sf))
	l=re.findall(r'"[^"]*"',sf)
	no_of_quoted_sents=sum([count_sents_in_quotes(i) for i in l])
        return (no_of_sents, no_of_quoted_sents)




def main():
	countQuotes()

if __name__=="__main__":
	main()
