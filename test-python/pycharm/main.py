import Cadastral
import asyncio

cadastral = Cadastral.Cadastral('/home/rmrf/Downloads/v1.kmz')
cadastral.getCoords(fixX=0.00300000000, fixY=0.00170000000)
asyncio.get_event_loop().run_until_complete(cadastral.getScreenOfCadastralMapByCoords_BetaVersion(headless=True, imagesavename='example.png', enablejavascreept=True, viewresolution={'width': 900, 'height': 600}, scalepageparameter=17))
image = cadastral.scaleScreen('i-want-to-die.png')
