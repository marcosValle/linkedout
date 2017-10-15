from bs4 import BeautifulSoup
import requests
from termcolor import colored
import re

def prepareUrl(baseUrl):
    if not re.match("^https?://.*", baseUrl):
        baseUrl="http://"+baseUrl
    if baseUrl[-1] == "/":
        baseUrl = baseUrl[:-1]

    return baseUrl

def prettifyLinks(links, baseUrl):
    baseUrlSplit = baseUrl.rsplit('/',1)
    if '.' in baseUrlSplit[1]:
        baseUrl = baseUrlSplit[0]

    for idx,l in enumerate(links):
        if l[0]=='#':
            links[idx] = baseUrl+'/'+l
        elif l[0]=='/':
            links[idx] = baseUrl+l
        elif not re.match("^https?://.*", l):
            links[idx] = baseUrl+"/"+l

    return links

def getRawLinks(baseUrl):
    result = requests.get(baseUrl)
    content = result.content

    soup = BeautifulSoup(content, "lxml")

    links=[]
    for a in soup.find_all("a", href=True):
            links.append(a.get("href"))
    for a in soup.find_all("area", href=True):
            links.append(a.get("href"))
    for a in soup.find_all("base", href=True):
            links.append(a.get("href"))
    for a in soup.find_all("link", href=True):
            links.append(a.get("href"))

    for a in soup.find_all("audio", src=True):
            links.append(a.get("src"))
    for a in soup.find_all("embed", src=True):
            links.append(a.get("src"))
    for a in soup.find_all("iframe", src=True):
            links.append(a.get("src"))
    for a in soup.find_all("img", src=True):
            links.append(a.get("src"))
    for a in soup.find_all("input", src=True):
            links.append(a.get("src"))
    for a in soup.find_all("script", src=True):
            links.append(a.get("src"))
    for a in soup.find_all("source", src=True):
            links.append(a.get("src"))
    for a in soup.find_all("track", src=True):
            links.append(a.get("src"))
    for a in soup.find_all("video", src=True):
            links.append(a.get("src"))

    for l in links:
        if(re.match("[^@]+@[^@]+\.[^@]+", l)):
            links.remove(l)

    links = list(set(links))
    print("Total links: {}".format(len(links)))
    return links

def testLinks(links):
    total = len(links)
    for idx,l in enumerate(links):
        print("[{}/{}] Testing {}".format(idx+1,total,l))
        if requests.get(l).status_code != 200:
            links.remove(l)
        else:
            print(colored("OK", 'green'))
    return links

if __name__ == "__main__":
    baseUrl = "http://www.eb.mil.br" # No trailing '/'
    links = getRawLinks(baseUrl)
    prettyLinks = prettifyLinks(links, baseUrl)
    ok = testLinks(prettyLinks)
    notOk = prettyLinks - ok

    for l in ok:
        print(l)
