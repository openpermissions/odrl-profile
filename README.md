Open Licensing Ontology
=======================

This is an extension of the ODRL 2.1 Ontology to support the Open Licensing Platform.

OpenLicensing vision
====================

The vision of OpenLicensing is to be a restricted set of ODRL2
who allows to write well-defined, simple ODRL offers and agreements.




Todo:
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
* IdTypes as IRI ? [WARNING ON CONSEQUENCES / ] 

* Monk ontology dependency, is this required? 
* Many ODRL terms have been redefined in this ontology in order to support serialisation via Monk ... review this.
* some terms from ODRL have been 'deprecated', this needs reviewing and justification/decision detailed in this document. [wip]
* some of the ontologies in our dependency folder have been modified (reduced in size) this should be documented in this document [wip]
* document host constraints (ck dene)
* review how we version the ontology
* describe in this document the versioning naming convention

Dependencies
============

Required as ODRL implementation
-------------------------------


**Traditional dependencies**

- <http://purl.org/dc/elements/1.1/>
- <http://purl.org/dc/terms/>


**Taxonomies**

- <http://www.w3c.org/2008/skos/>


**ODRL**
Licensing ontology ontop of which openlicensing is built

- <http://www.w3.org/ns/odrl/2/>


Specific to OpenLicensing ODRL
------------------------------
**JSON Serialization dependency**

- <http://digicat.io/ns/monk/0.3/> (Monk.embedded, Monk.multiple)


**Geographic names**

- <http://www.w3.org/2003/01/geo/wgs84_pos#> : core earth positioning type
- <http://www.geonames.org/ontology#> : region of the world


**Currencies**

- <http://cvx.iptc.org/iso4217a/> : iso code based ontology for currencies

** Units **

- or ISO code
- <http://purl.obolibrary.org/obo/uo#>
- QUTD ? (pixels, viristor per month)
unit:JouleSecond
Property	Value
qudt:abbreviation	J s
qudt:code	2036
qudt:conversionMultiplier	1.0e0
qudt:conversionOffset	0.0
qudt:quantityKind	quantity:AngularMomentum
qudt:symbol	J s

- OM ?
http://www.wurvoc.org/vocabularies/om-1.8/

<rdf:Description rdf:about="http://www.wurvoc.org/vocabularies/om-1.6/becquerel">
	<rdf:type rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/Singular_unit"/>
	<rdfs:comment xml:lang="en">The becquerel is a unit of activity defined as the activity of a quantity of radioactive material in which one nucleus decays per second. Algebraically it is defined as 1 divided by second.</rdfs:comment>
	<rdfs:label xml:lang="en">becquerel</rdfs:label>
	<om:definition rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/reciprocal_second-time"/>
	<om:symbol rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Bq</om:symbol>
	<om:dimension rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/frequency_or_activity-dimension"/>
	<om:longcomment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The becquerel is a unit of activity defined as the activity of a quantity of radioactive material in which one nucleus decays per second. Algebraically it is defined as 1 divided by second. The becquerel is a derived unit in the International System of Units.</om:longcomment>
</rdf:Description>

<rdf:Description rdf:about="http://www.wurvoc.org/vocabularies/om-1.6/reciprocal_second-time">
	<rdf:type rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/Unit_exponentiation"/>
	<rdfs:label xml:lang="en">reciprocal second (time)</rdfs:label>
	<om:symbol rdf:datatype="http://www.w3.org/2001/XMLSchema#string">s-1</om:symbol>
	<om:dimension rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/frequency_or_activity-dimension"/>
	<om:base rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/second-time"/>
	<om:exponent rdf:datatype="http://www.w3.org/2001/XMLSchema#float">-1</om:exponent>
</rdf:Description>

<rdf:Description rdf:about="http://www.wurvoc.org/vocabularies/om-1.6/kelvin">
	<rdf:type rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/Singular_unit"/>
	<rdfs:comment xml:lang="en">The kelvin is a unit of temperature defined as 1/273.16 of the thermodynamic temperature of the triple point of water.</rdfs:comment>
	<rdfs:label xml:lang="en">kelvin</rdfs:label>
	<om:definition rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/_1_273_16_of_the_thermodynamic_temperature_of_the_triple_point_of_water"/>
	<om:symbol rdf:datatype="http://www.w3.org/2001/XMLSchema#string">K</om:symbol>
	<om:dimension rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/thermodynamic_temperature-dimension"/>
	<om:longcomment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The kelvin is a unit of temperature defined as 1/273.16 of the thermodynamic temperature of the triple point of water. The kelvin is a base unit in the International System of Units.</om:longcomment>
</rdf:Description>

<rdf:Description rdf:about="http://www.wurvoc.org/vocabularies/om-1.6/thermodynamic_temperature-dimension">
	<rdf:type rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/Dimension"/>
	<rdfs:label xml:lang="en">thermodynamic temperature dimension</rdfs:label>
	<om:symbol rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Θ</om:symbol>
	<om:SI_length_dimension_exponent rdf:datatype="http://www.w3.org/2001/XMLSchema#float">0</om:SI_length_dimension_exponent>
	<om:SI_mass_dimension_exponent rdf:datatype="http://www.w3.org/2001/XMLSchema#float">0</om:SI_mass_dimension_exponent>
	<om:SI_time_dimension_exponent rdf:datatype="http://www.w3.org/2001/XMLSchema#float">0</om:SI_time_dimension_exponent>
	<om:SI_electric_current_dimension_exponent rdf:datatype="http://www.w3.org/2001/XMLSchema#float">0</om:SI_electric_current_dimension_exponent>
	<om:SI_thermodynamic_temperature_dimension_exponent rdf:datatype="http://www.w3.org/2001/XMLSchema#float">1</om:SI_thermodynamic_temperature_dimension_exponent>
	<om:SI_amount_of_substance_dimension_exponent rdf:datatype="http://www.w3.org/2001/XMLSchema#float">0</om:SI_amount_of_substance_dimension_exponent>
	<om:SI_luminous_intensity_dimension_exponent rdf:datatype="http://www.w3.org/2001/XMLSchema#float">0</om:SI_luminous_intensity_dimension_exponent>
</rdf:Description>

<rdf:Description rdf:about="http://www.wurvoc.org/vocabularies/om-1.6/degree_Fahrenheit">
	<rdf:type rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/Singular_unit"/>
	<rdfs:comment xml:lang="en">The degree Fahrenheit is a unit of temperature defined as 5.555556e-1 kelvin.</rdfs:comment>
	<rdfs:label xml:lang="en">degree Fahrenheit</rdfs:label>
	<om:definition rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/_5.555556e-1_kelvin"/>
	<om:symbol rdf:datatype="http://www.w3.org/2001/XMLSchema#string">°F</om:symbol>
	<om:dimension rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/thermodynamic_temperature-dimension"/>
</rdf:Description>

<rdf:Description rdf:about="http://www.wurvoc.org/vocabularies/om-1.6/_5.555556e-1_kelvin">
	<rdf:type rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/Measure"/>
	<om:numerical_value rdf:datatype="http://www.w3.org/2001/XMLSchema#string">5.555556e-1</om:numerical_value>
	<om:unit_of_measure_or_measurement_scale rdf:resource="http://www.wurvoc.org/vocabularies/om-1.6/kelvin"/>
</rdf:Description>

Versioning
==========

The ontology uses a semantic versionning.


- Minor changes that are fully compatible should involve a patch increment.
- Addition of features in a backward compatible way should least to increase of the minor version number.
- Incompatible changes should lead to a change of major version number ( it would lead to migration of data )
- Major changes in design lead to an increment of the version number ( it would lead to an increment of the release number ) 

Accessing information about the version of the ontology
-------------------------------------------------------

All terms must have a link "rdfs:definedBy" referencing the ontology in which they are defined.
The Ontology itself contains a field version info which shall be updated on each version.
It also contains a datatime information which allows to know when the ontology was last compiled and modified.

Presence version of the URI 
---------------------------

Release.Major.Minor.Patch

** Release is part of the ontology URL** 
Denotes a global vision

** Major version is part of the ontology URL **
It is generally asssumed that major version should be present in ontologies URL
as marjor are meant to denote incompatible usage of the ontology.


** Minor is not part of the ontology URL **
Bugfixes

** Patch is not part of the ontology URL **
* It is also fairly consensual that patch level which are not meant to signify change
in features shall not be present as part of the namespace URL. 


What to do when the ontology is updated in a backward compatible manner ?
-------------------------------------------------------------------------

1. Increment the patch number of the ontology


OpenLicensing Additions to ODRL
===============================

** Policy level shared duties **
You are allowed to specify shared duty at the level of the policy.
Openlicensing does not recommend to have multiple sets of duties attached to one policy.
As much as possible OpenLicensing recommends to split different permissions with different polcies.

** Policy level default assignees**
OpenLicensing provides ways to specify a default assigner for all the permissions at the level of the policy.
The usage of this field is recommended as it decreases verbosity.


OpenLicensing Deprecations
==========================

** Some ODRL Constraints : Towards data-aligned use-case driven **
We have deprecated many terms used in the "constraint" as RightOperand in ODRL due to the fact
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
   * OLEX - Creative copyrights.
   * SW - A demo profile for software licensing

