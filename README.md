The OpenPermissions ODRL Profile
================================

- URI : http://openpermissions.org/ns/op/1.1/
- Download : [rdf]( http://openpermissions.org/ontologies/ol-1.1.rdf), [xml]( http://openpermissions.org/ontologies/ol-1.1.xml)
- Version : 1.1
- Release date: Febuary 2016, the 22nd
- Authors : Open Permissions Platform Coalition

This is an ODRL 2.1 profile used in conjunction with the Open Permissions Platform.

- OpenPermissions supports only a limited subset of ODRL 2.1 which meets our requirements.
- OpenPermissions contains additional recommendations that help building consistent ontologies.

Future
======

The intention is that this will be a compliant [POE]() profile.
Tweaks made to the use of ODRL 2.1 to support our work will hopefully be reflected in the outcome of the W3C working group.

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

OpenPermissions ontology is built on top of ODRL2.1, and can be considered as an ODRL2.1 profile

- <http://www.w3.org/ns/odrl/2/>

Recommendations
===============


**Currencies**

- <http://cvx.iptc.org/iso4217a/> : iso code based ontology for currencies


Versioning
==========

The ontology uses a release version, followed by  traditional semantic versioning with following format : `Release.Major.Minor.patch`

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
http://openpermissions.org/ns/op/<Release>.<Major>/ 
```

Compiling files from components
-------------------------------

To keep the ontology manageable, the OpenPermissions ontology and its profiles have been split into different components, located
in the components folder. The resulting ontology is formed by concatenating all the files together and serialising it in different
ways. 

The helper script `build_onto.sh` compiles OpenPermissions. To recompile another ontology the path to the ontology needs to be
set as an environment variable. For instance to recompile the OPEX profile, run `./build_onto.sh profiles/olex` .

Note that `rdflib` is required to transform the ontologies from `turtle` format to the `rdfxml` format.
Before running this script, ensure to have installed  the required dependencies ( `pip install -r requirements.txt`  )


OpenPermissions ODRL Profile
============================

Definition of "Sets" and "Samples"
----------------------------------

In ODRL, there is no standard to discuss about sets of assets or license to set of assets,
no simple way to say that an Offer is linked to a set of Assets nor to clarify how many can
be picked from the set of Asset.

OpenPermissions is introducing primitives to discuss about sets of Assets and picking elements
from sets.


Definition of "IdTypes"
-----------------------

IdTypes refers to the type of an identifier, such as ISBN.
OpenPermissions platform assumes generally that `IdType` instances have semantic IRI and 
are defined as a `skos` taxonomy in single centrally-governed hub-specific namespace.
It is the responsibility of the hub owner to ensure the consistency of the taxonomy.


Shared Duty, default targets, assignee and assigner.
----------------------------------------------------

Open Permissions allows odrl:duty to be stated at the level of the policy.
Some Duties such as those related to one off payments shall preferably be expressed at the level of the Policy.
The duties expressed at the level of the policy apply to all the permissions.

Target, assignee, assigner are also recommended at the level of the policy.
They are considered as default target, assignee, and assigner for all Rules.

Offer Expiry data
-----------------

Open Permissions provides a special term to indicate when an Offer is going to be expired.


Limitation of ODRL expressivity by the OpenPermissions Platform
---------------------------------------------------------------

  * Policies with inheritance are not supported;
  * Policies with `conflict` term different from `prohibit` are not supported;
  * Policies with `undefined` term different from `invalid` are not recommended;
  * Policies with no `Permission` are not supported;
  * Policies using ODRL 2.1 experimental features are not supported;
  * `nextPolicy` constraint are currently not enforced and we recommend currently using the Open Permissions Platform only with policies that 
    that do not rely on this constraint;
  * Policies with types : `Set`, `Ticket` are not supported;
  * Policies with different set of duties for each permissions are supported however the set of duties that can be expressed at the permission level 
    is restricted to non-payment.
  * Profile should be set to the most specialised profile.

Profiles                            
========
Additional profiles can be added on top of OpenPermissions to license assets within specific domains.

Currently the following OpenPermissions profile exist:

   * OPEX - Support of creative content licensing.  This is a minimal specifications which was used for the development of the Copyright Hub.


Best practices when building a Profile and managing a Hub
=========================================================

* make all the predicates used by your Asset a subproperty of the `odrl:rightOperand` property so that the constraint defined in the policy match with your asset definition;
* on all numerical property whenever possible specify the unit in which the value has to be expressed as part of the ontology definition as it avoids all the other parties to have to deal with interoperability issues later on.
* It is strongly recommended not to reuse Permission or Duties across different Policies.
 
