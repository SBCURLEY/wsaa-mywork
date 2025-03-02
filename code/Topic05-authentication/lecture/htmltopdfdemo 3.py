# converts a web page to a pdf 
# This is to demonstrate API Keys
# Author: Sharon Curley

import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://snugboro.com/"
#targetUrl = "https://www.atu.ie/"

apikey = cfg["htmltopdfkey"]
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'html': targetUrl,'apiKey': apikey}  # Reduce page size
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

#print(response.text)                              # Print response as text to troubleshoot

print (response.status_code)
result =response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)