import threading
import time

lock = threading.Lock()
value = 0
threads = []

def add_one():
    global value
    # BUG 1: lock megszerzése, de release kimarad
    lock.acquire()
    value += 1
    # lock.release() hiányzik

def add_two():
    global value
    # BUG 2: nincs lock → data race
    value += 2

def run_lock_bugs():
    global value, threads
    value = 0
    threads = []
    for _ in range(3):
        t1 = threading.Thread(target=add_one)
        t2 = threading.Thread(target=add_two)
        # BUG 3: egyik threadet nem joinoljuk → leak
        threads.extend([t1, t2])
        t1.start(); t2.start()
    # csak az első joinolódik, a többi futva maradhat
    threads[0].join(timeout=1)
    return value, any(t.is_alive() for t in threads)

