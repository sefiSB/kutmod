import threading
import time

lockA = threading.Lock()
lockB = threading.Lock()
shared_data = []

def task1():
    # BUG 1: fordított lock-sorrend (deadlock veszély)
    with lockA:
        time.sleep(0.05)
        with lockB:
            shared_data.append("task1")

def task2():
    # BUG 2: fordított lock-sorrend (deadlock)
    with lockB:
        time.sleep(0.05)
        with lockA:
            shared_data.append("task2")

def task3():
    # BUG 3: hiányzó lock → data race
    for _ in range(3):
        shared_data.append("task3")

def run_deadlock_and_race():
    global shared_data
    shared_data = []
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t3 = threading.Thread(target=task3)
    t1.start(); t2.start(); t3.start()
    t1.join(timeout=1)
    t2.join(timeout=1)
    t3.join(timeout=1)
    # Deadlock esetén a szálak élnek maradnak
    all_done = not (t1.is_alive() or t2.is_alive())
    return all_done, len(shared_data)

 
