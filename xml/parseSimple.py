import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET



if __name__ == "__main__":
    url = input('Enter location: ')

    uh = urllib.request.urlopen(url)

    data = uh.read()

    tree = ET.fromstring(data)

    print(tree)

    # for ch in tree:
    #     print (ch.tag)
    counts = tree.findall('.//count')

    print(type(counts))
    print(sum([int(c.text) for c in counts]))

    