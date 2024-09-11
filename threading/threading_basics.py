import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting -5", name)
    time.sleep(2)
    logging.info("Thread %s: finishing -6", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread -1")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread -2 ")
    x.start()
    logging.info("Main    : wait for the thread to finish -3")
    # x.join() 
    logging.info("Main    : all done -4")