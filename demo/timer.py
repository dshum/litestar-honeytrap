import time


def infinite_timer():
    counter = 0
    while True:
        counter += 1
        time.sleep(1)
        yield counter


for i in infinite_timer():
    print(i)
