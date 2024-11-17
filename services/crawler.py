import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import time
from dotenv import load_dotenv
import os


load_dotenv()  # take environment variables from .env.

maxPages = os.environ.get("MAX_PAGES_TO_CRAWL")

def crawlSite(url: str):
    textResults = []

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers)
    if(response.status_code != 200):
        print(url + " : failed")

    soup = BeautifulSoup(response.content, 'html.parser')

    counter = 0

    text = extractText(url)
    textResults.append(text)
    time.sleep(1)
    print(url)
    print(text, "\n", "\n")
    counter += 1

    for atag in set(soup.find_all('a', href=True)):
        link = str(atag.get('href'))
        if url in link or (link.startswith("./") and link != "./") or (link.startswith("/") and link != "/"):
            if link.startswith("./"):
                link = url + "/" + link[2:]
            elif link.startswith("/"):
                link = url + link
            text = extractText(link)
            textResults.append(text)
            time.sleep(1)
            print(link)
            print(text, "\n", "\n")
            counter += 1
            if counter >= int(maxPages):
                break
    return textResults

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def extractText(url: str):
    res = ""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers)
    if(response.status_code != 200):
        print(url + " : failed to hit")
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = soup.findAll(string=True)
    visible_texts = filter(tag_visible, texts)

    for text in set(visible_texts):
        if len(text.split(" ")) > 4:
            res += "\n " + text
    return res