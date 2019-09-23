import datetime
from time import *

import requests

v1 = None
v2 = None
url = "http://homepages.wmich.edu/~kaminski/cs1110/index.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

while True:
    v1 = v2
    if v1 is None:
        v1 = requests.get(url, headers=headers)
    v2 = requests.get(url, headers=headers)
    if v1.content != v2.content:
        print("Change Detected!", datetime.datetime.now())
    sleep(60)