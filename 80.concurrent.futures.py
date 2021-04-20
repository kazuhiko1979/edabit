import concurrent.futures as cf
import urllib.request
import pprint

from logging import StreamHandler, Formatter, INFO, getLogger


def init_logger():

    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(
        Formatter("[%(asctime)s][%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)

URLS = ['http://www.foxnews.com/',
       'http://www.cnn.com/',
       'http://europe.wsj.com/',
       'http://www.google.com/',
       'http://www.bbc.co.uk/',]


def load_url(url):

    getLogger().info("start:%s", url)

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }

    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as conn:
        getLogger().info("end  :%s", url)
        return len(conn.read())


def main():

    init_logger()

    # with cf.ThreadPoolExecutor(max_workers=3,
    #                            thread_name_prefix="thread")\
    #                            as executor:
    #
    #     for url in URLS:
    #         executor.submit(load_url, url)

    with cf.ProcessPoolExecutor(max_workers=3) as executor:

        future_ret_list = executor.map(load_url, URLS)
        pprint.pprint(list(future_ret_list))


        # future_list = []
        # for url in URLS:
        #     future = executor.submit(load_url, url)
        #     future_list.append(future)

        # pprint.pprint(["length:"+str(future.result()) for future in future_list])
        # pprint.pprint([future for future in future_list])

    return

if __name__ == '__main__':
    main()