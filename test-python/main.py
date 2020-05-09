import kml2geojson

from zipfile import ZipFile
from lxml import html


filename = '/home/rmrf/Downloads/v1.kmz'

kmz = ZipFile(filename, 'r')
kml = kmz.open('doc.kml', 'r').read()
 
doc = html.fromstring(kml)
coords = []
for x in doc.xpath('/html/body/kml/document/folder/region/latlonaltbox')[0]:
    coords.append(x.text)

print(type(kml))
