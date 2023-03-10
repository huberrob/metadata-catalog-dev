import yaml
import re
import os
import json

yamldir='../db/metadata-schemes'
files = os.listdir(yamldir)
subjects = []
for yamlfile in files:
    #print(yamlfile)
    if yamlfile.endswith('.yml'):
        with open(yamldir+'/'+yamlfile, 'r') as stream:
            yamlstr = stream.read()
            try:
                data = yaml.safe_load(yamlstr)
                if data.get('keywords'):
                    print(yamlfile, data.get('keywords'))
                    subjects.extend(data.get('keywords'))
            except Exception as e:
                print(e, yamlfile)
print(sorted(list(set(subjects))))