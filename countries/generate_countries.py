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
    c=(c[0],c[1].split('\t'))
    if len(c[1][16]):
        data=download('http://sws.geonames.org/%s/about.rdf'%(c[1][16],))
        sys.stderr.write("[%s](%db)"%(c[1][16],len(data)))
        g.parse(data=data)
        sys.stderr.write(".")    

sys.stderr.write("\n")

data=download("http://sws.geonames.org/6295630/about.rdf")
g.parse(data=data)

g.serialize('geonames_countries.rdf')
g.serialize('geonames_countries.ttl',format='turtle')
