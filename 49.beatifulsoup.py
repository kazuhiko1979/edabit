import requests
import pprint
import re

from bs4 import BeautifulSoup


def main():

    url = "https://www.yahoo.co.jp/"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # img = soup.find_all("img")
    # pprint.pprint(img[0], width=40)
    # print(img[0].get("src"))

    # for i in soup.find_all("td", href=re.compile("http.*yahoo")):
    #     print(i)
    #     print("-------------------")

    print(soup.select("#p"))
    print(soup.prettify())

    return

if __name__ == '__main__':
    main()

