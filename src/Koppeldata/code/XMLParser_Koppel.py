import os
from bs4 import  BeautifulSoup
import json
fp = open('blogdata.json','w')
BASE_DIR = "/home/wayne/Documents/blogs"
    
def parseXMLToBloggerInfoDict(path):
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
        blogger_dict["Posts"].append(post)
    json.dump(blogger_dict,fp, indent=4)

for xmlfile in os.listdir(BASE_DIR):
    parseXMLToBloggerInfoDict("%s%s%s" % (BASE_DIR, os.path.sep, xmlfile))


        