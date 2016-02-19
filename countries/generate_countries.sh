#!/bin/bash
curl http://download.geonames.org/export/dump/countryInfo.txt | awk -F '\t' '(!/^#/){if ($17!="") { printf("curl http://sws.geonames.org/%s/about.rdf > %s.rdf \n"   , $17
,$17);}}' |bash
curl http://sws.geonames.org/6295630/about.rdf > 6295630.rdf
python merge_all_rdf.py
