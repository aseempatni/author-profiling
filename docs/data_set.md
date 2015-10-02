# DATA-SET

## Corpus

We have used the following two corpora for this study:

### Blog Authorship Corpus

The Blog Authorship Corpus consists of the collected
posts of 19,320 bloggers gathered from blogger.com
in August 2004. The corpus incorporates a total of
681,288 posts and over 140 million words or approxi-
mately 35 posts and 7250 words per person. All blog-
gers included in the corpus fall into one of three age
groups — ”10s” [13-17], ”20s” [23-27], ”30s” [33-47]. For
each age group there are an equal number of male and
female bloggers.

### PAN’14 Corpus

As a part of the Author Profiling Shared Task in PAN
’14, this corpus was made available for use during the
competition. This data-set originally consists of blog
posts, tweets and social media texts written in both
English and Spanish as well as hotel reviews in En-
glish. We have considered only the subset which con-
tains blog posts. All bloggers included in the corpus
fall into one of these age groups: [18-24], [25-34], [35-
49], [50-64], [65-xx]. The corpus incorporates a total
of 2278 posts, 148 authors or on an average 15 blogs
per author.

We split ourselves into two groups, one for extracting fea-
tures from the Blog Authorship Corpus (Pranay, Shubham
& Soham) and the other from the PAN ’14 Corpus (Aayush,
Aseem & Bhushan).

## Data Cleaning & Extraction

### Blog Authorship Corpus

The corpus contains 19,320 XML files, each pertaining
to a particular author, identified by the unique file-
names. Each XML file contains date when the blog was
posted followed by the post itself. All the HTML links
in the post are replaced by a unique tag ’urlLink’ to
mark their presence. We cleaned the data by discard-
ing empty blog posts and ignoring posts which contain
only HTML links and no text. We then exported this
refined data to a JSON file, on which further analysis
will be carried out.

### PAN ’14 Corpus

This corpus contains 148 XML files, each pertainingto a particular author. Each XML file contains the
Author’s unique ID and blogs written by the Author.
The blog text is present in CDATA section. To parse
this text, we wrote a regular expression to remove the
HTML tags, translated HTML entities like ’&amp;’,
’&ldquo;’ to their usual textual counter-parts like
’&’,’”’. We then dumped this data as to a JSON file,
on which further analysis will be carried out.

