The OpenLicensing Ontology
==========================

- URI : http://openlicensing.org/ns/ol/1.1/
- Download : [rdf]( http://openlicensing.org/ontologies/ol-1.1.rdf), [xml]( http://openlicensing.org/ontologies/ol-1.1.xml)
- Version : 1.1
- Release date: Febuary 2016, the 22nd
- Authors : Digital Catapult 


This is an extension of the ODRL 2.1 Ontology to support the Open Licensing Platform.


OpenLicensing vision
====================

The vision of OpenLicensing is to be a restricted set of ODRL2
who allows to write well-defined, simple ODRL offers and agreements.

Well-defined terms for licensing
--------------------------------
  - OpenLicensing removes terms that are loosely defined from ODRL2.1.
  - OpenLicensing specifies ontologies to be used for monetary and geographical data.
  
Simple, simple, simple
-----------------------
  - OpenLicensing supports only a limited the scope of licenses supported by ODRL which we think is more likely to be well supported by software.
  - OpenLicensing removes from ODRL terms that are domain specific
  - OpenLicensing provide shortcut to ODRL construct that simplify the definition of common Policies (such as Creative Commons)

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


Specific to OpenLicensing ODRL
------------------------------

**Geographic names**

- <http://www.w3.org/2003/01/geo/wgs84_pos#> : core earth positioning type
- <http://www.geonames.org/ontology#> : region of the world


**Currencies**

- <http://cvx.iptc.org/iso4217a/> : iso code based ontology for currencies


** Units **

- Units should be simple to reference according to established standard
  Units are referenced using string


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
- It also contains a datatime information which allows to know when the ontology was last compiled and modified.

Presence version of the URI 
---------------------------

A release version will generally have the format:

- `Release.Major.Minor.patch`

Only the part that are related to breaking changes will be present in the URL

```
http://openlicensing.org/ns/ol/<Release>.<Major>/ 
```

Release is part of the ontology URL
-----------------------------------
Denotes a global vision of the ontology. 

Major version is part of the ontology URL
-----------------------------------------
Major are meant to denote incompatible usage of the ontology.
Note that major version update can occur as result of what users may think as minor 
changes.

Minor is not part of the ontology URL
-------------------------------------
Addition of features in a way that do not break existing features.

Patch is not part of the ontology URL
-------------------------------------

It is also fairly consensual that patch level which are not meant to signify change
in features shall not be present as part of the namespace URL. 

 


OpenLicensing Additions to ODRL
===============================

** Policy level shared duties **
You are allowed to specify shared duty at the level of the policy.
Openlicensing does not recommend to have multiple sets of duties attached to one policy.
As much as possible OpenLicensing recommends to split different permissions with different polcies.

** Policy level default assignees**
OpenLicensing provides ways to specify a default assigner for all the permissions at the level of the policy.
The usage of this field is recommended as it decreases verbosity.



Definition of "Sets"
====================

In ODRL, there is no standard to discuss about sets of assets.

OpenLicensing introduce primitives to discuss about sets.

- **TODO: COMPLETE THIS SECTION**
- **TODO: COMPLETE THIS SECTION**
- **TODO: COMPLETE THIS SECTION**


OpenLicensing Deprecations
==========================

** Some ODRL Constraints : Towards data-aligned use-case driven **
We have deprecated many terms used in the "constraint" as RightOperand in `ODRL` due to the fact
that these terms to be useful need to be aligned with domain data. For instance,
RelativePosition and RelativeSize as a scalar did not seem us to make sense when talking about 2d/3d assets.
Also we recommend to use the same properties in metadata assets and in constraints. 
Adding a triple specifying that these properties are rightOperand to make things clearer.

** OpenLicensing Units **
OpenLicensing does encourage re-using standard units for each property and discourage the absence of standard
on representation of units on each constraint.
(property must indicate their unit using monk:expressedIn)
OR 
(we reuse same as ODRL) but UNIT have to be expressed ...
OR 
(we tolerate ODRL notes, but recommend specifications of units via additional labels)


OpenLicensing Specialisations with respect to ODRL
==================================================

We have specified further the ontologies that have to be used to refer to:
   *  Spatial regions
   *  Currencies
   *  Parties


Profiles
========
Additional profiles can be added on top of OpenLicensing to license assets within specific domains.

Currently the following OpenLicensing profile exist:
   * CREATIVE - Creative copyrights.
   * SW - A demo profile for software licensing


<!--
=====

* Remove Countries from this ontology, select a suitable external ontology that specialises in this [waiting for review]
* Each element should have a description [done: comment -> description]
* remove ns1:[done / waiting for review]
* Some ids are not valid, needs fixing [done]
* Check all owl constraints used and limit them to remain at least with the RL profile [done - http://mowl-power.cs.man.ac.uk:8080/validator/]
* Language notation on descriptive strings [ck: if other fields needed]
* the dependencies we have on other ontologies should be described and justified in this document [ stripped version?? why? ]

* Move items between OLEX and OL 

In grep olex BAPLA :
'''
prefix olex: <http://digicat.io/ns/olex/0.1/> .
<https://www.copyrighthub.org/s0/hub1/creation/chub/uuid/abd11b12d53d48a09698edb43cb1b2db> a olex:Asset,
        olex:IncomingLinksOnObjects,
        olex:SPARQLSet,
    olex:elementType ol:Asset ;
    olex:predicate olex:explicitOffer ;
    olex:sparql "SELECT ?s {WHERE ?s <http://digicat.io/ns/olex/0.1/explicitOffer> <https://www.copyrighthub.org/s0/hub1/offer/chub/4corners-offerid/12> .}"^^xsd:string ;
    olex:target_object <https://www.copyrighthub.org/s0/hub1/offer/chub/4corners-offerid/12> ;
<https://www.copyrighthub.org/s0/hub1/creation/chub/uuid/feb9b868378f4904898d7a3bc0a4313f> a olex:Asset,
        olex:PurposeInfo,
        olex:WildcardSet,
    olex:elementType ol:Asset ;
    olex:purpose ol:commercial_purpose ;

'''

* There are some ASSET ID TYPES defined, needs reviewing, instance vs class [James Review]
* IdTypes as IRI ? [WARNING ON CONSEQUENCES] 

* Monk ontology dependency, is this required?  [removed]
* Removed actions as same as ODRL [done]
* Many ODRL terms have been redefined in this ontology in order to support serialisation via Monk ... review this. [removed]
* some terms from ODRL have been 'deprecated', this needs reviewing and justification/decision detailed in this document. [wip]
* some of the ontologies in our dependency folder have been modified (reduced in size) this should be documented in this document [wip]
* document host constraints (ck dene) | CONSTRAINT: (...)
* review how we version the ontology | [wip]
* describe in this document the versioning naming convention | [wip]
* * term host !!
-->

