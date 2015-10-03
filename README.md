# Author Profiling

Predicting Gender and Age of the author using semantic features

This project involves predicting personal information of authors like gender, age etc by training classifiers using content based and semantic features extracted from a KB like
Wikipedia. There is a lot of contextual difference between blogs written by different people. This project will explore those contextual differences to predict age and gender of an author of a text. It
basically consists of two phases:

1. Semantic representation of documents. This can be done by linking the entities to
Wikipedia and mapping semantically related words to Wikipedia Category Network

2. Age and Gender prediction. This can be done by using any ML classifiers like SVM or
KNN.

## [Report](docs/README.md)

## Document Features 

* Count of HTML links in the blog
* Distribution of various POS tags across different gender
* More usage of pronouns than actual referral to someone/something (coreferencing)
* Count of discourse relations present within the blog text
* Average length of sentences 
* Count of named entities within the blog text
* Distribution of various punctuation tags
* Opinion scores for the blog
* Readability score for the blog (SMOG and Fischer)
* Common topics talked about in the blogs
* Non-topical words distribution across different gender and age brackets
* Count of non-dictionary words used
* Count of direct quotations used in the text
* References to different chronological times within the text
* Count of facts vs # of opinions used in the text
* Usage of Capital letters
* Character flooding like hellooooo
* LSA of the blogs for a particular user - as a measure of his/her behavior to be either focussed or diverse.
* Quality of words used in the text (relative frequency of words in corpus: less frequent more important)
* Average # of mis-spelled words in the texts
* Repetition of words by a particular blogger across blogs written by him/her

## Data

* [PAN 2015 Dataset](http://www.uni-weimar.de/medien/webis/events/pan-15/pan15-web/author-profiling.html)
* [PAN 2014 Dataset](http://www.uni-weimar.de/medien/webis/events/pan-14/pan14-web/author-profiling.html)
* [Koppel Blog Corpus](http://u.cs.biu.ac.il/~koppel/BlogCorpus.htm)

## Reference Papers

* [Author Profiling: Predicting Age and Gender from Blogs](http://ceur-ws.org/Vol-1179/CLEF2013wn-PAN-SantoshEt2013.pdf)
* [Author profiling using LDA and Maximum Entropy](http://ceur-ws.org/Vol-1179/CLEF2013wn-PAN-PavanEt2013.pdf)
* [Recurrent Convolutional Neural Networks for Text Classification](http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/9745/9552)
* [Gender Classification with Deep Learning](http://cs224d.stanford.edu/reports/BartleAric.pdf)

