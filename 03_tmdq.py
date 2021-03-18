from tqdm import tqdm
import time
import random

def main():

    # for i in tqdm(range(100)):
    #     time.sleep(0.05)

    with tqdm(total=10) as pbar:
        time.sleep(random.randint(1, 10)*0.2)
        pbar.update(1)
        time.sleep(random.randint(1, 10) * 0.2)
        pbar.update(3)
        time.sleep(random.randint(1, 10) * 0.2)
        pbar.update(1)
        time.sleep(random.randint(1, 10) * 0.2)
        pbar.update(5)

    return

if __name__ == '__main__':
    main()
