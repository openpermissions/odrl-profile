The OpenLicensing Ontology
==========================

- URI : http://openlicensing.org/ns/ol/1.1/
- Download : [rdf]( http://openlicensing.org/ontologies/ol-1.1.rdf), [xml]( http://openlicensing.org/ontologies/ol-1.1.xml)
- Version : 1.1
- Release date: Febuary 2016, the 22nd
- Authors : Digital Catapult

This is an ODRL 2.1 profile used in conjunction with the Open Licensing Platform.

- OpenLicensing supports only a limited the scope of licenses supported by ODRL.  
  This subset correspond is also what we think is currently likely to be well supported by software.
- OpenLicensing contain additional recommendations that help building consistent ontologies.

Dependencies
============

Required as ODRL implementation
-------------------------------
**Traditional dependencies**

- <http://purl.org/dc/elements/1.1/>
- <http://purl.org/dc/terms/>


**Taxonomies**

- <http://www.w3c.org/2008/skos/>


**ODRL 2.1**

OpenLicensing ontology is built ontop of ODRL2.1, and can be considered as an ODRL2.1 profile

- <http://www.w3.org/ns/odrl/2/>

Recommendations
===============


**Currencies**

- <http://cvx.iptc.org/iso4217a/> : iso code based ontology for currencies


Versioning
==========

The ontology uses a release version, followed by  traditional semantic versionning with following format : `Release.Major.Minor.patch`

- Major changes impacting the globally design/vision should lead to an increment of the release version number. 
- Incompatible changes still based on the same vision of the ontolgy should lead to a change of major version number.
- Addition of features in a backward compatible way should least to increase of the minor version number.
- Minor changes that are fully compatible should involve a patch increment.

Accessing information about the version of the ontology
-------------------------------------------------------

- All terms must have a link "rdfs:definedBy" referencing the ontology in which they are defined.
- The ontology itself contains a field version info which shall be updated on each version.
- It also contains a date and time information which allows to know when the ontology was last modified.

Presence of Release and Major version of the URI 
------------------------------------------------

A release version will generally have the format:

- `Release.Major.Minor.patch`

Only the part that are related to breaking changes will be present in the URL.
Incompatible changes would mean that the same term could be interpreted differently and this need to be identified.

```
http://openlicensing.org/ns/ol/<Release>.<Major>/ 
```

Definition of "Sets" and "Samples"
==================================

In ODRL, there is no standard to discuss about sets of assets or license to set of assets,
no simple way  to saythat an offer is linked to a set of asset nor to clarify how many can 
be picked from the asset.

OpenLicensing is introducing primitives to discuss about sets of assets and picking elements 
from sets.


Definition of "IdTypes"
=======================

OpenLicensing platform assumes generally that `IdType` instances have semantic IRI and 
are defined as a `skos` taxonomy in single centrally-governed hub-specific namespace.
It is the responsiblity of the hub owner to ensure the consistency of the taxonomy.


ODRL syntaxes not supported by the OpenLicensing Platform
=========================================================
 
  * `nextPolicy`;
  * policies with different set of duties for each permission;
  * policies with inheritance;
  * policies with non default behaviour on `undefined` and `conflict`.

Profiles
========
Additional profiles can be added on top of OpenLicensing to license assets within specific domains.

Currently the following OpenLicensing profile exist:
   * CREATIVE - Creative copyrights.
   * SW - A demo profile for software licensing


