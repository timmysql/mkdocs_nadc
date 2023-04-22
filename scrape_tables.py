# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from rich import print, inspect


# https://nebraskalegislature.gov/senators/picture_list.php

# https://nebraskalegislature.gov/senators/senator_list.php

def get_descendents():
    url = 'https://nebraskalegislature.gov/senators/picture_list.php'# Create object page
    html = requests.get(url).content

    # creating soup object
    data = BeautifulSoup(html, 'html.parser')

    # finding parent <ul> tag
    parent = data.find("body").find("ul")

    # finding all <li> tags
    text = list(parent.descendants)

    inspect(text)

    # printing the content in <li> tag
    # print(text)
    # for i in range(2, len(text), 2):
    #     print(text[i], end=" ")
def get_find_all():    
    url = 'https://nebraskalegislature.gov/senators/senator_list.php'    
    req = requests.get(url)
    class_is_multi= { '*' : 'class'}
    # creating soup object
    # soup = BeautifulSoup(req.text, 'html.parser').find_all('ul')
    soup = BeautifulSoup(req.text,'xml.parser', multi_valued_attributes=class_is_multi)
    # print(soup.b)
    
    for i in soup:
        # inspect(i,methods=True)
        input('stop.....................')
        print(i.li.a.text)
        
    #     input('stop')


        
    # soup = BeautifulSoup("<ul><li></li></ul>",'html.parser')
    # print(soup)
    # print(soup.head)
    # print(soup.title)
    # print(soup.body.b)
    # for i in soup:
        
    
    # print(soup.get_text())
    # print(soup.prettify())    
    # print(soup.title)
    # print(soup.title.name)
    # print(soup.title.string)
    # print(soup.title.parent.name)
    # print(soup.p)
    # print(soup.p['class'])
    

    
    # ul = soup.contents[0]
    # print(ul)
    # ul.contents[0]
    
    
    # for i in ul:
    #     i.contents[0]
    #     print(i)
    #     input('stop')
                

    # finding all li tags in ul and printing the text within it
    # data1 = data.find('ul')
    
    # inspect(data1)
    # print(data1.find('list-group list-group-flush name_list'))
    # for li in data1.find_all("li"):
        # inspect(li)
        # print(li.text, end=" ")   
        
        
if __name__ == "__main__":
    get_find_all()
    # get_descendents()