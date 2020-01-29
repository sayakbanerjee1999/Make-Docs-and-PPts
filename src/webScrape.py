import requests, webbrowser
from bs4 import BeautifulSoup
import re

def webScrap():
    user_input = input ("Enter Something to Search:")
    print("finding...")

    #Scrapping from Wikipedia
    wiki_search = requests.get("https://en.wikipedia.org/wiki/"+user_input)

    soup = BeautifulSoup(wiki_search.content, "lxml")

    #Adding and styling the text scrapped from Wikipedia
    text = ""
    for paragraph in soup.find_all('p'):
        text += paragraph.text

    text = re.sub(r'\[[0-9]*\]','',text)

    sentence = text.split(".") 

    return (sentence[0]+". "+sentence[1]+".")

result = webScrap()
print(result)