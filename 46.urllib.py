import urllib.request

def main():

    # url = "https://www.google.com/search"
    # params = {"q":"学習", "tbm":"nws"}
    # headers = {"User-Agent": "Mozilla / 5.0"}
    #
    # full_url = "{}?{}".format(url, urllib.parse.urlencode(params))
    # print(full_url)
    #
    # request = urllib.request.Request(full_url, headers=headers)
    # with urllib.request.urlopen(request) as response:
    #     print(response.read())


    # request = urllib.request.Request(url)
    # print(request.full_url)
    # print(request.type)
    # print(request.host)
    # print(request.selector)
    # print(request.get_method())
    # response = urllib.request.urlopen(url)
    # print(response.getcode())
    # print(response.read())
    # response.close()
    #
    # with urllib.request.urlopen(request) as response:
    #     print(response.read())


    url = "https://shopping.c.yimg.jp/lib/haptic/7121-5144-1.jpg"
    urllib.request.urlretrieve(url, "7121-5144-1.jpg")

    return



if __name__ == '__main__':

    main()