import logging
from logging import getLogger, StreamHandler, Formatter


def init():

    global logger
    logger = getLogger("SomeApp")
    logger.setLevel(logging.DEBUG)

    # handler = StreamHandler()
    handler = logging.FileHandler('some.log')
    format  = Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(format)

    logger.addHandler(handler)


def main():

    init()

    # logging.basicConfig(filename='some.log',
    #                     level=logging.WARNING)
    #
    logger.critical("This is log Message ")
    logger.error("This is log Message ")
    logger.warning("This is log Message ")
    logger.info("This is log Message ")
    logger.debug("This is log Message ")


    return


if __name__ == '__main__':
    main()