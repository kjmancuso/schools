import json
import os

from jinja2 import Environment, FileSystemLoader

# Get relative directory
DIR = os.path.dirname(os.path.abspath(__file__))
# Path to schools.json
sjson = DIR + '/data/schools.json'
out_file = DIR + '/index.html'

# Load school data
with open(sjson, 'r') as fp:
    schools = json.load(fp)

env = Environment(loader=FileSystemLoader(DIR + '/templates'))

template = env.get_template('index.html')

with open(out_file, 'w') as fp:
    fp.write(template.render(schools=schools))
