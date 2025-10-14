import re
from dataclasses import field

import abspipeline

path = 'fileExplorer/Task/Asset/Character/Model'
pattern = 'fileExplorer/Task/Asset/(?P<asset_type>.*)/(?P<asset_name>.*)'

r = re.compile(pattern)

found = None
for match in r.finditer(path):
    found = match.groupdict()

# list comprehension
found = [match.groupdict() for match in r.finditer(path)]

if found:
    result = found[0]
    print(f"match: {result}")



print("_"*50)

def resolve (entity_type, path):
    return "test"