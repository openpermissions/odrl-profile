#!/usr/bin/env python
import glob
import urllib
import rdflib
g=rdflib.Graph()

for x in glob.glob("[0-9]*.rdf"):
    g.parse(x)
    
g.serialize('geonames_countries.rdf')
g.serialize('geonames_countries.ttl',format='turtle')
