#!/bin/bash

function section {
echo
echo "# -----------------------------------------------------------------------"
echo "# $1"
echo "# -----------------------------------------------------------------------"
echo
}

function create_ontology {
cat openlicensing_prefix.ttl | sed -e "s/|compiledate|/$(date --iso-8601=seconds)/g" |sed -e "s/+0000/Z/g"

section "Ids"
cat openlicensing_ids.ttl
section "Assets"
cat openlicensing_asset.ttl
section "Parties"
cat openlicensing_party.ttl


section "Actions"
cat openlicensing_action.ttl
section "Constraints"
cat openlicensing_constraint.ttl
section "Rules"
cat openlicensing_rule.ttl

section "Policies"
cat openlicensing_policy.ttl

section "Asset sets"
cat openlicensing_set.ttl

}

create_ontology > openlicensing.ttl
python ttl2xml.py openlicensing.ttl
