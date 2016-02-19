#!/usr/bin/env python
import sys
import glob
import urllib
import rdflib
g=rdflib.Graph()

def download(x,n=None):
    content=urllib.urlopen(x).read()
    if n:
        file(n,"wb").write(content)
    return content

COUNTRIES_URL="http://download.geonames.org/export/dump/countryInfo.txt"
countries=filter(lambda l:len(l) and l[0]!='#',urllib.urlopen(COUNTRIES_URL).read().split('\n'))
for c in enumerate(countries):
    sys.stderr.write("\r%d/%d"%(1+c[0],len(countries)))
    g.parse(data=download('http://sws.geonames.org/%s/about.rdf'%(c[1][16],)))
sys.stderr.write("\n")
#for x in glob.glob("[0-9]*.rdf"):
#    g.parse(x)
    
# add the earth 
g.parse(download("http://sws.geonames.org/6295630/about.rdf"))

g.serialize('geonames_countries.rdf')
g.serialize('geonames_countries.ttl',format='turtle')
