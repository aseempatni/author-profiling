import re
from xml.dom import minidom
import os
from bs4 import  BeautifulSoup
def removeTag_CDATA_section(text):
    processedText = re.sub(r'<[^>]*>','',text,0)
    processedText = re.sub(r'&amp;','&',processedText,0)
    processedText = re.sub(r'&ldquo;','"',processedText,0)
    processedText = re.sub(r'&rdquo;','"',processedText,0)
    processedText = re.sub(r'&rsquo;',"'",processedText,0)
    processedText = re.sub(r'&nbsp;','',processedText,0)
    return processedText


def get_author_info(filename):
    # ifile = open(filename)
    # truth_data = ifile.readlines()
    # author = {}
    # for line in truth_data:
    #     element = line.strip().split(":::")
    #     author[element[0]] = {'Gender':element[1],'Age':element[2]}
    # ifile.close()
    author = {}
    components = filename.split('.')
    author['Id'] = components[0]
    author['Gender'] = components[1]
    author['Age'] = components[2]
    return author

def filter_xml(list):
    author_files = []
    for file in list:
        if file.endswith(".xml"):
            author_files.append(file)
    return author_files

def getDocs(file_path):
    blogger = parseXMLtoDict(file_path)
    return blogger['Posts']
	# xmldoc = minidom.parse(file)
	# rawdocuments = xmldoc.getElementsByTagName('document')
	# ans=[]
	# for document in rawdocuments:
	# 	ans.append(removeTag_CDATA_section(document.firstChild.nodeValue.strip()))
	# return ans


def parseXMLtoDict(path):
    blogger_dict = {}
    blogger_id,gender,age,industry, sign = path.split(os.path.sep)[-1].split(".xml")[0].split(".")
    blogger_dict["ID"] = blogger_id
    blogger_dict["Sex"] = gender
    blogger_dict["Age"] = int(age)
    blogger_dict["Dates"] = []
    blogger_dict["Posts"] = []
    s = file(path,"r").read().replace("&nbsp;", " ")
    s = s.replace("<Blog>", "").replace("</Blog>", "").strip()
    for e in s.split("<date>")[1:]:
        date_and_post = e.split("</date>")
        blogger_dict["Dates"].append(date_and_post[0].strip())
        post = date_and_post[1].replace("<post>","").replace("</post>","").strip()
        post = BeautifulSoup(post).get_text()
        blogger_dict["Posts"].append(post.encode('ASCII','ignore'))
    return blogger_dict
