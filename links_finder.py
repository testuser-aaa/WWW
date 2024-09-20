#!/usr/bin/env python3
#scrapping fo links from the given URL

from io import BytesIO
import requests
from lxml import etree
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="url to scan for")
    parser.add_argument('url',type=str,help="enter ip of the target ")
    
    args=parser.parse_args()
    return args

def main():
    args = get_arguments()
    url = args.url
    r = requests.get(url) # GET
    parser=etree.HTMLParser()
    #print(response.text) # response.text = string; response.content = bytestring
    content=r.content
    content = etree.parse(BytesIO(content), parser=parser)
    for link in content.findall('.//a'): # находим все ссылки (элементы "a")
        print(f"{link.get('href')} -> {link.text}")

if __name__ == "__main__":
    main()
