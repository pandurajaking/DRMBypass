
import logging
from queue import Queue
from threading import Thread
from time import sleep, time

from parse_page import Driver
from pipeline import pipeline

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def read_file(path: str):
    file1 = open(path, 'r')
    Lines = file1.readlines()
    file1.close()
    return Lines


class PipelineWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            driver, url, name, max_speed = self.queue.get()
            try:
                pipeline(driver, url, name, max_speed)
            finally:
                self.queue.task_done()


def threads(driver: Driver, path: str, offset: int, max_speed: int):
    ts = time()
    urls = read_file(path)
    queue = Queue()
    # Create 4 worker threads
    num_worker_threads = 4
    for x in range(num_worker_threads):
        worker = PipelineWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    count = 0
    for url in urls:
        count += 1
        name = f"{count + offset}_seriya"
        logger.info('Queueing {}'.format(url))
        queue.put((driver, url, name, max_speed/num_worker_threads))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    logging.info('Took %s', time() - ts)
