import json
import urllib.request


url = input("Enter Url : ")
handle = urllib.request.urlopen(url)
data = handle.read()

info = json.loads(data)

comments = info['comments']

totalCount = 0
for item in comments:
  totalCount += item['count']
print(totalCount)

    