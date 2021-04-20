import requests
from bs4 import BeautifulSoup
import os

def main():


    url = 'https://www.udemy.com/'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    image_list = []
    dir = "C:/Users/kazuh/PycharmProjects/edabit/img/"

    for img in soup.find_all('img'):
        print(img.get("src"))
        if 'jpg' in img.get("src"):
            image_list.append(img.get("src"))

    for image in image_list:
        req = requests.get(image)
        file_name = image.split('/')[-1]
        with open(dir + file_name, 'wb') as f:
            f.write(req.content)

if __name__ == '__main__':
    main()


