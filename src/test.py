import sys
from feature import extract
import combine

# read doc
ifile = sys.argv[1]
with open(ifile,'r') as text:
    doc = text.read()

# extract feature
features = extract.features_from([doc])

# convert to csv

# TODO
df = combine.feature_to_csv(features)
df.to_csv(ifile+'.out')
# code to convert extracted features from json to CSV.
# Write csv to outfile.
