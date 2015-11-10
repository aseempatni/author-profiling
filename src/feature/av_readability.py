from collections import Counter
from readability import readability as r
def av_readability(docs):
    c = Counter()
    for doc in docs:
        rd = r.Readability(doc.encode('ascii','ignore'))
        read = {}
        read["ARI"] = rd.ARI()
        read["FleschReadingEase"] = rd.FleschReadingEase()
        read['FleschKincaidGradeLevel'] = rd.FleschKincaidGradeLevel()
        read['GunningFogIndex'] = rd.GunningFogIndex()
        read['SMOGIndex'] = rd.SMOGIndex()
        read['ColemanLiauIndex'] = rd.ColemanLiauIndex()
        read['LIX'] = rd.LIX()
        read['RIX'] = rd.RIX()
        c.update(read)
    for key, value in c.iteritems():
        c[key] = value/len(docs)
    return dict(c)


