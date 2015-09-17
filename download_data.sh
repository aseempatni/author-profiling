
# make a directory for storing data
mkdir -p data
cd data

echo "Storing data in ./data"

## Pan 14 dataset

echo "Downloading PAN 14 dataset."
# download
wget http://www.uni-weimar.de/medien/webis/corpora/corpus-pan-labs-09-today/pan-14/pan14-data/pan14-author-profiling-training-corpus-2014-04-16.zip
# extract
tar -xvzf pan14-data/pan14-author-profiling-training-corpus-2014-04-16.zip -P PAN-14
# remove temporary zip file
rm pan14-data/pan14-author-profiling-training-corpus-2014-04-16.zip

## Koppel dataset

echo "Downloading Koppel dataset."
# download
wget http://www.cs.biu.ac.il/~koppel/blogs/blogs.zip
#extract
unzip blogs.zip -d ./koppel
rm blogs.zip
