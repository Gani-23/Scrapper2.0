import urllib.request
import urllib.parse 
import urllib.error
import urllib.response 
import sys 
from bs4 import BeautifulSoup

if len(sys.argv)<2:
    print("Invalid argument")
    sys.exit(0)

url = sys.argv[1]

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,'html.parser')

tags = soup('a')

for tag in tags: 
    print(url+tag.get('href',None))

