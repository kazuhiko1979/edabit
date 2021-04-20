import threading
import time

lock = threading.RLock()
condition = threading.Condition()
semaphore = threading.Semaphore(3)
event = threading.Event()

barrier = threading.Barrier(2)


def hello(name, timing):

    # lock.acquire()
    #
    # for i in range(5):
    #     print(str(i)+":Hello "+name+" San!!")
    #     time.sleep(timing)
    #
    #     lock.acquire()
    #     lock.release()
    #
    # lock.release()

    # time.sleep(1)
    # condition.acquire()

    # semaphore.acquire()

    for i in range(5):
        print(str(i)+":Hello "+name+" San!!")
        time.sleep(timing)

    # event.set()

    # condition.notify()
    # condition.release()
    # semaphore.release()


def hello2(name, timing):

    barrier.wait()

    for i in range(5):
        print(str(i)+":Hello "+name+" San!!")
        time.sleep(timing)


def main():

    threading.Thread(target=hello2, args=("Tanaka", 1)).start()

    print("I am main")
    hello("Main", 1)

    threading.Thread(target=hello2, args=("Sato", 1)).start()

    # event.wait()

    # threading.Thread(target=hello, args=("Aoki", 1)).start()
    #
    # thread_2 = threading.Thread(target=hello, args=("Sato", 2))
    # thread_2.start()
    # thread_2.join()
    # print("finish")



    # condition.acquire()
    # print("waiting")
    # condition.wait()
    # # condition.release()
    #
    # print("finish!")

    # thread_2 = threading.Thread(target=hello, args=("Sato", 2))
    # thread_2.start()
    # thread_2.join()
    # print("finish")

    return


if __name__ == '__main__':
    main()