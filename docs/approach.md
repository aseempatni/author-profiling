# Approach

After obtaining the JSON files containing refined data from the both the corpora, we now start extracting features from this data-set. 
We shall be focusing our attention towards building two kinds of classifiers

1. Binary classifier for classification of gender and 
2. Multi-label classifier for classification of age into predefined class labels. 

Later, we will also consider the possibility of predicting the age by fitting regression models, by working under the assumptions that — 

1. There are enough data points for the model to fit accurately, and 
2. Age behaves like a continuous variable.

## Exhaustive Feature Set

In this study, we shall consider the following types of features for building our classifiers:

* Content-based Features viz. # of HTML links in the blog, # of named entities used, # of non-word errors, # of discourse relations within the text, # of quota-
tions used in the text, # of references to past or future within the text, # of facts & figures used, # of times
opinions are expressed, list of topics talked about in the blog, overall sentiment of the blog, whether the author
sticks to particular theme throughout his blogs, # of figures of speech the author uses (like metaphor, al-
literation), # of words having character flooding (like ’hellooooo’).

* Style-based Features viz. distribution of POS tags, dis-
tribution of punctuation tags, readability measure of
the blog (SMOG & Fischer), # of co-references (usage
of pronouns), average sentence length, usage of figures
of speech by the author (like metaphor, alliteration).

* Semantic Features: Latent Semantic Analysis (LSA)
of the blogs to identify set of topics authors, belonging
to a particular gender or age group, blog about.
These features will be extracted for both the corpora.

These features will be extracted for both the corpora.

## Extracting Feature Vectors

Methodology to extract feature vectors from the Blog Au-
thorship Corpus is described below:

### Content-based Features:

1. # of HTML links: count the occurrence of ’urlLink’
in the body of the blog.
2. # of named entities: Using Stanford NLTK APIs to
tokenize blog text into sentences, perform POS Tag-
ging and then extract named entities (NE) from the
tagged sentences.
3. # of non-word errors: Using Stanford NLTK’s word
corpus nltk.corpus.words.words() to keep a count of
non-word errors in the blog.
4. # of discourse relations within the text: Using a
Java-based end-to-end PDTB-styled Discourse Parser
to identify implicit & explicit discourse relations and
keeping a count of each of them.
5. # of quotations used in the text: Checking for oc-
currences of ’”’ in the blog text.
6. # of references to past or future: Checking for oc-
currences of the following set of words and phrases -
[’years ago’,’years from now’,’in the past’,’in future’,’once
upon a time’,’ˆ\d{4}$’]. The last entry is a regex for
detecting reference to a year.
7. # of facts & figures used: To be decided.
8. # of times opinions are expressed:

## Feature Subset Selection (FS)

Dimensionality reduction (DR) and Feature Subset Selec-
tion (FS) are two techniques for reducing the attribute space
of a feature set. The main idea of FS is to remove redundant
or irrelevant features from the data set as they can lead to
a reduction of the classification accuracy and to an unneces-
sary increase of computational cost. The advantage of FS is
that no information about the importance of single features
is lost. For now, we will focus our attention on using FS
over DR because DR can decrease the size of the attribute
space strikingly. Another important disadvantage of DR is
the fact that the linear combinations of the original features
are usually not interpretable and the information about how
much an original attribute contributes is often lost. If pos-
sible, we might also try using DR technique (PCA) to our
feature set and evaluate the improvement in the accuracy of
the resulting classifier, if any.

There are three types of feature subset selection approaches:

### Filters:

Filters are classifier agnostic pre-selection methods which
are independent of the later applied machine learning
algorithm. . Besides some statistical filtering methods
like Fisher score or Pearson correlation, information
gain is often used to find out how well each single fea-
ture separates the given data set.
The overall entropy I of a given dataset S is defined as:

I(S) := −C∑p i log 2 p i(1)i=1

where C denotes the total number of classes and p i the
portion of instances that belong to class i. The reduc-
tion in entropy or the information gain is computed
for each attribute according to:

∑ |S A,v |IG(S, A) = I(S) −I(S A,v )(2)|S|v∈A

where v is a value of A and S A,v is the set of instances
where A has value v.

### Wrappers:

Wrappers are feedback methods which incorporate the
ML algorithm in the FS process, i.e. they rely on
the performance of a specific classifier to evaluate the
quality of a set of features. Wrapper methods search
through the space of feature subsets and calculate the
estimated accuracy of a single learning algorithm for
each feature that can be added to or removed from the
feature subset.

We shall focus our attention towards using Filters to perform
FS in this study.
