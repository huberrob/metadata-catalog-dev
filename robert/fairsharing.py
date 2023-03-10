import yaml
import re
import os
import json

yamldir='../db/metadata-schemes'
files = os.listdir(yamldir)
with open('subject_mapping.json') as fs:
    fields_of_science = json.load(fs)

#yamlfile='../db/metadata-schemes/abcd-access-biological-collection-data.yml'
yamlfile='../db/metadata-schemes/datacite-metadata-schema.yml'
standards = dict()
for yamlfile in files:
    if yamlfile.endswith('.yml'):
        #print(yamlfile)
        with open(yamldir+'/'+yamlfile, 'r') as stream:
            yamlstr = stream.read()
            try:
                id=None
                data = yaml.safe_load(yamlstr)
                identifiers = data.get('identifiers')
                hasfairsharing = False
                for identifier in identifiers:
                    if identifier.get('scheme') == 'FAIRsharing':
                        id = identifier.get('id')
                        hasfairsharing = True
                if not hasfairsharing:
                    print(yamlfile)
            except Exception as e:
                print('Error: ',e, yamlfile)