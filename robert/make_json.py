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
                for identifier in identifiers:
                    if identifier.get('scheme') == 'RDA-MSCWG':
                        id = identifier.get('id')
                subjects= data.get('keywords')
                fos = []
                if subjects:
                    for subject in subjects:
                        if subject in fields_of_science:
                            fos.extend(fields_of_science.get(subject))
                fos = list(set(fos))
                title = data.get('title')
                acronym = data.get('acronym')
                urlmatch = re.findall(r"url:\s?(.*)$", yamlstr, re.MULTILINE)
                for uri in urlmatch:
                    standards[uri] = {'title': title,'identifier': id, 'subject_areas':subjects, 'field_of_science':fos, 'acronym':acronym}
                #standards[title] = {'identifier': id, 'urls': urlmatch, 'subject_areas':subjects, 'field_of_science':fos, 'acronym':acronym}

            except yaml.YAMLError as exc:
                print('ERROR: '+yamlfile+str(exc))
    else:
        print(yamlfile)
print(json.dumps(standards))