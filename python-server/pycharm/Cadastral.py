import asyncio
from pyppeteer import launch

import os

from PIL import Image
from pathlib import Path

from zipfile import ZipFile
from lxml import html
from pyvirtualdisplay import Display


class Cadastral:
    filename = ''
    doc = ''
    x, y = 0, 0

    def __init__(self, pwdtokmz):
        self.filename = pwdtokmz
        #self.getKmlFromKmz()
        #self.getCoords(fixX=0.00300000000, fixY=0.00170000000)
        #asyncio.get_event_loop().run_until_complete(self.getScreenOfCadastralMapByCoords_BetaVersion(headless=True, imagesavename='example.png', enablejavascreept=True, viewresolution={'width': 900, 'height': 600}, scalepageparameter=17))

    def getKmlFromKmz(self):
        kmz = ZipFile(self.filename, 'r')
        kml = kmz.open('doc.kml', 'r').read()
        self.doc = html.fromstring(kml)

    def getCoords(self, x1, x2, y1, y2, fixX, fixY):
        coords = []
        for x in self.doc.xpath('/html/body/kml/document/folder/region/latlonaltbox')[0]:
            coords.append(x.text)

        self.x = (float(coords[0]) + float(coords[1])) / 2 + fixX
        self.y = (float(coords[2]) + float(coords[3])) / 2 + fixY

        return self.x, self.y

    def setAndGetCoords(self, x1, x2, y1, y2, fixX, fixY):
        self.x = (x1 + x2) / 2 + fixX
        self.y = (y1 + y2) / 2 + fixY

        return self.x, self.y

    # async def getScreenOfCadastralMapByCoords_BetaVersion(self, headless=True, imagesavename='example.png', enablejavascreept=True, viewresolution={'width': 900, 'height': 600}, scalepageparameter=17):
    #     browser = await launch({"headless": headless, "args": ['--no-sandbox']})
    #     page = await browser.newPage()
    #     await page.setViewport(viewport=viewresolution)
    #     await page.setJavaScriptEnabled(enabled=enablejavascreept)
    #     await page.goto('https://pkk.rosreestr.ru/#/search/{},{}/{}'.format(str(self.y), str(self.x), str(scalepageparameter)))
    #     await asyncio.sleep(2)
    #     await page.screenshot({'path': imagesavename})
    #     await browser.close()
    def getScreenOfCadastralMapByCoords_BetaVersion(self, url):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from PIL import Image
        import time
        #from pyvirtualdisplay import Display
        from selenium import webdriver

        #display = Display(visible=1, size=(1200, 800))
        #display.start()
        # take screenshot
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        #chrome_options.set_headless(False)
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument('headless')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-plugins-discovery");
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.delete_all_cookies()
        driver.set_window_size(900, 600)
        driver.set_window_position(0, 0)

        driver.get(url)
        time.sleep(3)
        driver.save_screenshot("pageImage.png");

        driver.quit()
        #display.stop()

        img = Image.open('pageImage.png')
        os.remove('./pageImage.png')

        return img

    def scaleScreen(self, image):
        wsize = 1500
        #imgfile = Path('/home/rmrf/Dev/Avio_Hackaton/test-python/pycharm/example.png')
        #imgfile = Path('./example.png')
        #img = Image.open(imgfile)
        img = image
        #os.remove('/home/rmrf/Dev/Avio_Hackaton/test-python/pycharm/example.png')
        #os.remove('./example.png')
        width = img.size[0]
        height = img.size[1]
        img3 = img.crop((100, 90, width - 20, height - 200))
        hsize = int((float(img3.size[1]) * float((wsize / float(img3.size[0])))))
        img3 = img3.resize((wsize, hsize), Image.ANTIALIAS)
        #img3.save(savename)
        return img3
