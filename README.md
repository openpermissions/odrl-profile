Open Licensing Ontology
=======================

This is an extension of the ODRL 2.1 Ontology to support the Open Licensing Platform.

Todo:
=====
* review how we version the ontology
* describe in this document the versioning naming convention
* remove ns1:
* Remove Countries from this ontology, select a suitable external ontology that specialises in this
* Monk ontology dependency, is this required?
* Language notation on descriptive strings
* Check all owl constraints used and limit them to remain at least with the RL profile
* There are some ASSET ID TYPES defined, needs reviewing, instance vs class
* some terms from ODRL have been 'deprecated', this needs reviewing and justification/decision detailed in this document.
* Many ODRL terms have been redefined in this ontology in order to support serialisation via Monk ... review this.
* Some ids are not valid, needs fixing
* the dependencies we have on other ontologies should be described and justified in this document
* some of the ontologies in our dependency folder have been modified (reduced in size) this should be documented in this document

Dependencies
============

Todo:
Required as ODRL implementation
-------------------------------


**Traditional dependencies**

- http://purl.org/dc/elements/1.1/
- http://purl.org/dc/terms/


**Taxonomies**

- http://www.w3c.org/2008/skos/


**ODRL**
Licensing ontology ontop of which openlicensing is built

- odrl: http://www.w3.org/ns/odrl/2/


Specific to OpenLicensing ODRL
------------------------------


**JSON Serialization dependency**

- http://digicat.io/ns/monk/0.3/ (Monk.embedded, Monk.multiple)


**Geographic names**

- http://www.w3.org/2003/01/geo/wgs84_pos# : core earth positioning type
- http://www.geonames.org/ontology# : region of the world


**Currencies**

- http://cvx.iptc.org/iso4217a/ : iso code based ontology for currencies

Versioning
==========

Todo:

ODRL Deprecations
=================

Todo:

Profiles
========

Todo:



