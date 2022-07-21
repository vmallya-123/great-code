import os
import re
import requests
from PIL import Image
from bs4 import BeautifulSoup


def extract_image_name(url):
    image_name = str(url).split("/")[-1]
    return image_name


if __name__ == "__main__":
    home = os.getcwd()
    url = input("Enter URL with images : ")
    sitename = str(url).split("/")[2]
    os.mkdir(sitename)
    os.chdir(sitename)
    print("\nShould we can scan entire site or just home page ?")
    option = int(input("1. Entire site\n2.Just this page\nOption : "))
    if option == 1:
        links = [url]
        link_html = requests.get(url).text
        all_links = BeautifulSoup(link_html, "html.parser").findAll("a")
        for link in all_links:
            href = link.get("href")
            if href:
                if href.startswith("http") or href.startswith("https"):
                    links.append(href)
        all_avaialble_links = links
    else:
        all_avaialble_links = [url]

    for link in all_avaialble_links:
        print(link)
        links = [url]
        link_html = requests.get(url).text
        all_links = BeautifulSoup(link_html, "html.parser").findAll("a")
        for link in all_links:
            href = link.get("href")
            if href:
                if href.startswith("http") or href.startswith("https"):
                    links.append(href)
        Image_links = links
        for link in Image_links:
            raw_image = requests.get(link, stream=True).raw
            img = Image.open(raw_image)
            image_name = extract_image_name(link)
            img.save(image_name)
