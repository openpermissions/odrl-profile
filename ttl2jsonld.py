import rdflib
import sys

g=rdflib.Graph()
g.parse(sys.argv[1],format="turtle")
g.serialize(sys.argv[1][:-4]+".json", format="json-ld")
