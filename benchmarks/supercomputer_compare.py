from os.path import exists
import matplotlib.pyplot as plt
from itertools import chain
import xml.etree.ElementTree as ET
import db_helpers as db
import api_helpers as api
import numpy as np

x = range(2000,2022)

def append_value(country, dictionary, i, value):
    if country not in dictionary:
        dictionary[country] = [None] * len(x)
    if dictionary[country][i] is None:
        dictionary[country][i] = []
    dictionary[country][i].append(value)

comp = dict()
i = 0
for year in x:
    for month in ['06', '11']:
        fp = 'compute_data/TOP500_' + str(year) + month + '_all.xml'
        if not exists(fp):
            print("File not found: " + fp)
            continue

        fh = open(fp)
        tree = ET.parse(fh)
        root = tree.getroot()
        ns = {'top500': 'http://www.top500.org/xml/top500/1.0'}

        for site in root:
            country = site.find('top500:country', ns).text
            rmax = float(site.find('top500:r-max', ns).text)
            append_value(country, comp, i, rmax)

    i += 1

total = dict()

for country, values in comp.items():
    total[country] = [0] * len(x)
    for i in range(len(x)):
        if values[i]:
            total[country][i] = sum(values[i])


topic_id = 19
keywords = db.get_keywords(topic_id)
title = db.get_topic(topic_id)[2]
token = 'Your Elsevier InstToken'
key = 'Your Elsevier API Key'

usa_papers = []
china_papers = []

for year in x:
    print(year)
    usa_papers.append(api.fetch_papers(keywords, token, key, year, 'United States'))
    china_papers.append(api.fetch_papers(keywords, token, key, year, 'China'))

print(usa_papers)
print(china_papers)
print(np.corrcoef(usa_papers, total['United States']))
print(np.corrcoef(china_papers, total['China']))


fig, ax1 = plt.subplots() 

ax1.set_ylabel('Papers Published') 
ax1.plot(x, usa_papers, color = 'blue', label='United States')
ax1.plot(x, china_papers, color = 'red', label='China')
ax1.set_title(title)
ax1.legend()

ax2 = ax1.twinx()
  
ax2.set_ylabel('Power (MFlops)') 
ax2.plot(x, total['United States'], color = 'blue', linestyle='dashed')
ax2.plot(x, total['China'], color = 'red', linestyle='dashed')

plt.show()
