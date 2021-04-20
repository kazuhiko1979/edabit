from multiprocessing import Pool
from multiprocessing import Process, Lock, Queue, Pipe
import time


def func(i, conn):

    # with lock:

    conn.send(['hello world', i])
    time.sleep(1)
    conn.close()


def main():

    # for num in range(10):
    #     proc = Process(target=func, args=(num,))
    #     proc.start()

    # with Pool(3) as proc:
    #     print(proc.map(func, [1, 2, 3]))

    # lock = Lock()

    # queue = Queue()
    # time.sleep(1.5)
    # [print(queue.get()) for _ in range(queue.qsize())]

    parent_conn, child_conn = Pipe()

    for num in range(5):
        proc = Process(target=func, args=(num, child_conn))
        proc.start()

    for _ in range(5):
        time.sleep(1)
        print(parent_conn.recv())

    return


if __name__ == "__main__":
    main()