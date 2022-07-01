
import logging
from queue import Queue
from threading import Thread
from time import sleep, time

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
            link, name = self.queue.get()
            try:
                pipeline(link, name)
            finally:
                self.queue.task_done()


def threads(path: str, offset: int):
    ts = time()
    links = read_file(path)
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
    for link in links:
        sleep(10)
        count += 1
        name = count + offset
        logger.info('Queueing {}'.format(link))
        queue.put((link, f"{name}_seriya"))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    logging.info('Took %s', time() - ts)
