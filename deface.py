import requests
import re
import pytesseract
from PIL import Image

def getPage(baseUrl):
    r = requests.get(baseUrl)

    if r.status_code != 200:
        print("Page does not seem to be online. Could you double check it?")

    return r.text

def searchHackWords(content):
    comp = re.compile('h[a4]ck[e3]d', re.IGNORECASE)
    res = comp.findall(content)

    if bool(res):
        return res

    return None

def checkTextDefacement(baseUrl):
    content = getPage(baseUrl)
    res = searchHackWords(content)

    return res

def checkImgDefacement(baseUrl):
    im = Image.open("/home/valle/Downloads/4.jpg")
    text = pytesseract.image_to_string(im)
    res = searchHackWords(text)

    return res

def checkDefacement(baseUrl):
    resTxt = checkTextDefacement(baseUrl)
    resImg = checkImgDefacement(baseUrl)

    if resTxt or resImg:
        print("### Possibly hacked ###")
        print("Matched terms:")
        if resTxt:
            for t in resTxt:
                print("\t"+t)
        if resImg:
            for t in resImg:
                print("\t"+t)
    else:
        print("This page seems to be clean")
