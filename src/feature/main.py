import os
from utils import *
import json
from config import *
import extract

authorFileNames = os.listdir(directory)

# Given a file extract all the truth data and features and dump it to a json
def process(file):
    ofilePath = outdir+file.split('.')[0]+".json"

    # process only if not already processed
    if os.path.isfile(ofilePath) == False:
        print file
        authorInfo = get_author_info(file)
        author_id = authorInfo['Id']
        author = {}
        file_path = directory+"/"+file
        docs = getDocs(file_path)
        author[author_id] = extract.features_from(docs)
        author[author_id]['Gender'] = authorInfo['Gender']
        author[author_id]['Age'] = authorInfo['Age']

        with open(ofilePath,'w') as fp:
            json.dump(author[author_id],fp, indent=4)

    # skip if already present
    else:
        print file+":skip"


def main():
    index = 1

    for file in filter_xml(authorFileNames):

        # task done
        if index>ending_index:
            break

        # need to process
        if index >= starting_index:
            process(file)

        index = index + 1


if __name__ == "__main__":
    main()

