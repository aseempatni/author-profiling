import punctuation as punctu
from av_readability import av_readability
import NER_tagger
import pos_tagging
import html_links
import countQuote
import topics_mean_stdev
import sentence_length

# extract features given a list of documents3
def features_from(docs):
    feature = {}
    feature['punctuation'] = punctu.extract_from_xml(docs)
    feature['pos'] = pos_tagging.distribution(pos_tagging.get_POS_Tags(docs))
    feature['NER'] = NER_tagger.get_NER_tags(docs)
    feature['hyperlinks_info'] = html_links.get_hyperlink_info(docs)
    feature["topic_var"] = topics_mean_stdev.getTopics(docs)
    feature["quotes"] = countQuote.getquotes(docs)
    feature["readability"] = av_readability(docs)
    feature["sentence_length"] = sentence_length.extract(docs)
    return feature

