import asyncio
from pyppeteer import launch

import os

from PIL import Image
from pathlib import Path

from zipfile import ZipFile
from lxml import html


class Cadastral:
    filename = ''
    doc = ''
    x, y = 0, 0

    def __init__(self, pwdtokmz):
        self.filename = pwdtokmz
        self.getKmlFromKmz()
        #self.getCoords(fixX=0.00300000000, fixY=0.00170000000)
        #asyncio.get_event_loop().run_until_complete(self.getScreenOfCadastralMapByCoords_BetaVersion(headless=True, imagesavename='example.png', enablejavascreept=True, viewresolution={'width': 900, 'height': 600}, scalepageparameter=17))

    def getKmlFromKmz(self):
        kmz = ZipFile(self.filename, 'r')
        kml = kmz.open('doc.kml', 'r').read()
        self.doc = html.fromstring(kml)

    def getCoords(self, fixX, fixY):
        coords = []
        for x in self.doc.xpath('/html/body/kml/document/folder/region/latlonaltbox')[0]:
            coords.append(x.text)

        self.x = (float(coords[0]) + float(coords[1])) / 2 + fixX
        self.y = (float(coords[2]) + float(coords[3])) / 2 + fixY

    async def getScreenOfCadastralMapByCoords_BetaVersion(self, headless=True, imagesavename='example.png', enablejavascreept=True, viewresolution={'width': 900, 'height': 600}, scalepageparameter=17):
        browser = await launch({"headless": headless, "args": ['--no-sandbox']})
        page = await browser.newPage()
        await page.setViewport(viewport=viewresolution)
        await page.setJavaScriptEnabled(enabled=enablejavascreept)
        await page.goto('https://pkk.rosreestr.ru/#/search/{},{}/{}'.format(str(self.y), str(self.x), str(scalepageparameter)))
        await asyncio.sleep(2)
        await page.screenshot({'path': imagesavename})
        await browser.close()

    def scaleScreen(self, savename):
        wsize = 1500
        imgfile = Path('/home/rmrf/Dev/Avio_Hackaton/test-python/pycharm/example.png')
        img = Image.open(imgfile)
        os.remove('/home/rmrf/Dev/Avio_Hackaton/test-python/pycharm/example.png')
        width = img.size[0]
        height = img.size[1]
        img3 = img.crop((100, 90, width - 20, height - 200))
        hsize = int((float(img3.size[1]) * float((wsize / float(img3.size[0])))))
        img3 = img3.resize((wsize, hsize), Image.ANTIALIAS)
        img3.save(savename)
        return img3
