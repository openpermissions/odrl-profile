import rdflib
import sys

g=rdflib.Graph()
for f in sys.argv[1:]:
    print f
    g.parse(f)
    
QUERY_ACTIONS="""
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
PREFIX dct: <http://purl.org/dc/terms/> 
PREFIX odrl: <http://www.w3.org/ns/odrl/2/> 
PREFIX op: <http://openpermissions.org/ns/op/1.1/> 


SELECT DISTINCT ?action_name ?parent_action ?term_status WHERE {
    ?action a skos:Concept .
    ?action rdfs:label ?action_name .
    OPTIONAL { ?action skos:broaderTransitive ?parent_action }
    OPTIONAL { ?action vs:term_status ?term_status }
   
}
"""

QUERY_CONSTRAINTS="""
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
PREFIX dct: <http://purl.org/dc/terms/> 
PREFIX odrl: <http://www.w3.org/ns/odrl/2/> 
PREFIX op: <http://openpermissions.org/ns/op/1.1/> 



SELECT DISTINCT ?constraint ?constraint_range ?parent_constraint ?term_status WHERE {

    VALUES (?propertyType ) {
    (rdf:Property)
    (owl:DatatypeProperty)
    (owl:ObjectProperty)
    }

    ?constraint a ?propertyType .
    ?constraint rdfs:subPropertyOf+ odrl:rightOperand .
    OPTIONAL { ?constraint rdfs:range ?constraint_range . }
    OPTIONAL { ?constraint rdfs:subPropertyOf ?parent_constraint }
    OPTIONAL { ?constraint vs:term_status ?term_status }

}
"""

actions=list(g.query(QUERY_ACTIONS))
constraints=list(g.query(QUERY_CONSTRAINTS))

print "action","parent","status"
for a in actions:
    print ",".join(map(lambda s:str(s).split('/')[-1],a))

print

print "constraint","range","parent","status"
for c in constraints:
    print ",".join(map(lambda s:str(s).split('/')[-1],c))
