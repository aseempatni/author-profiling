import os
from os import path
from pprint import pprint
import json

f = open("config.json",'r')
config = json.load(f)
path = config["path_to_blogs"]

def read_truth_data():
    with open(path+'/truth.txt','r') as truth_file:
        authors = []
        for author in truth_file:
            author_data = author.split(":::")
            authors.append(author_data)
    return authors

truth_data = read_truth_data()

if __name__ == "__main__":
    print pprint(truth_data)
