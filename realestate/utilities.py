import pandas as pd
import requests
import json

url = "https://data.lacounty.gov/resource/csig-gtr7.json"

response = requests.get(url)
if response.status_code != reqests.codes.ok:
    raise ValueError("There is no data from this url")

results = json.loads(response.text)
