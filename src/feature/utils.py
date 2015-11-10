import re
from xml.dom import minidom
def removeTag_CDATA_section(text):
    processedText = re.sub(r'<[^>]*>','',text,0)
    processedText = re.sub(r'&amp;','&',processedText,0)
    processedText = re.sub(r'&ldquo;','"',processedText,0)
    processedText = re.sub(r'&rdquo;','"',processedText,0)
    processedText = re.sub(r'&rsquo;',"'",processedText,0)
    processedText = re.sub(r'&nbsp;','',processedText,0)
    return processedText


def get_author_info(filename):
    ifile = open(filename)
    truth_data = ifile.readlines()
    author = {}
    for line in truth_data:
        element = line.strip().split(":::")
        author[element[0]] = {'Gender':element[1],'Age':element[2]}
    ifile.close()
    return author

def filter_xml(list):
    author_files = []
    for file in list:
        if file.endswith(".xml"):
            author_files.append(file)
    return author_files

def gettext(file):
	xmldoc = minidom.parse(file)
	rawdocuments = xmldoc.getElementsByTagName('document')
	ans=[]
	for document in rawdocuments:
		ans.append(removeTag_CDATA_section(document.firstChild.nodeValue.strip()))
	return ans


