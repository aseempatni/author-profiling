import truth
import json

from bs4 import BeautifulSoup

f = open("config.json",'r')
config = json.load(f)
path = config["path_to_blogs"]

truth = truth.read_truth_data()

authors = [x[0] for x in truth]

def get_doc_for(author):
    with open(path+"/"+author+".xml",'r') as docs:
        doc = BeautifulSoup(docs)
        x = doc.findAll("document")
        clean_docs = [x.text.strip() for x in doc.findAll("document")]
        return clean_docs

def get_docs_for_all(authors):
    author_docs = {}
    for author in authors:
        docs = get_doc_for(author)
        author_docs[author] = docs
    return author_docs

if __name__ == "__main__":
    author_docs = get_docs_for_all(authors)
