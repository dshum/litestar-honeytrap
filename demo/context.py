import logging
import time
from contextlib import contextmanager

logging.basicConfig(level=logging.DEBUG)


@contextmanager
def execution_time():
    begin = time.time()
    yield
    end = time.time()
    logging.info(f"execution time: {end - begin:.3f} sec")


with execution_time():
    total = sum(range(10_000_000))
    print(f"{total=}")
