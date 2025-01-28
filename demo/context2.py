import logging
import time

logging.basicConfig(level=logging.DEBUG)


class ExecutionTime:
    begin: float
    end: float

    def __enter__(self):
        self.begin = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        logging.info(f"execution time: {self.end - self.begin:.3f} sec")


with ExecutionTime() as exec_time:
    total = sum(range(10_000_000))
    print(f"{total=}")
