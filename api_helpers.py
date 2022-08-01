from time import sleep
from pybliometrics.scopus import AbstractRetrieval
from pybliometrics.scopus import ScopusSearch

def fetch_keywords(seeds, min_sup, token, key):
    keyword_freq = {}
    keywords = []

    for seed in seeds:
        if not seed[1]:
            continue
        ab = AbstractRetrieval(identifier=seed[1], id_type='doi', view='FULL', refresh=True, insttoken=token, apiKey=key)
        terms = []
        if ab.authkeywords:
            terms += ab.authkeywords
        if ab.idxterms:
            terms += ab.idxterms
        terms = list(dict.fromkeys(terms))
        if terms:
            for term in terms:
                if term in keyword_freq:
                    keyword_freq[term] += 1
                else:
                    keyword_freq[term] = 1
                
    for keyword, freq in keyword_freq.items():
        if freq >= min_sup:
            keywords.append(keyword)

    return keywords
    
def fetch_papers(keywords, token, key, year, country):
    if not keywords:
        return 0
    query = "KEY(\"" + keywords[0][1] + "\""
    for keyword in keywords[1:]:
        query = query + " OR \"" + keyword[1]+ "\""
    query += ") AND AFFILCOUNTRY(" + country
    query += ") AND PUBYEAR IS " + str(year)
    
    try:
        s = ScopusSearch(query=query, view="STANDARD", download=False, subscriber=True, insttoken=token, apiKey=key)
    except:
        sleep(10)
        s = ScopusSearch(query=query, view="STANDARD", download=False, subscriber=True, insttoken=token, apiKey=key)

    return s.get_results_size()

