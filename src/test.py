import sys
from feature import extract

# read doc
ifile = sys.argv[1]
with open(ifile,'r') as text:
    doc = text.read()

# extract feature
extract.features_from([doc])

# convert to csv

# TODO
# code to convert extracted features from json to CSV.
# Write csv to outfile.
