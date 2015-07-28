#!/usr/bin/env python
from math import ceil
import requests

# make GET request to API and bind response to 'resp'
resp = requests.get('http://www.expertise.com/api/v1.0/jobs/text')

# bind value of JSON object's 'text' to list 'text' split on whitespace
text = resp.json()['text'].split()

# print estimated time to read text, assuming average of 200wpm
# text/200.0 returns float, which is rounded up and converted to an int
print "about {time} minutes".format(time=int(ceil(len(text)/200.0)))
