from os import path
import json
from string import Template
from functools import reduce

model_dir = path.dirname(__file__)

with open(path.join(model_dir, 'henry_iv.json')) as json_file:
    henry_json = json.load(json_file)


henry_text = reduce(lambda a, b: Template('$lines $line').substitute(lines=a, line=b['text_entry']), henry_json, '')
