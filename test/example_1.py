import threading

counter = 0

def increment():
    global counter
    for _ in range(10000):
        counter += 1

def run_threads():
    global counter
    counter = 0
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)
    t1.start(); t2.start()
    t1.join(); t2.join()
    return counter

if __name__ == "__main__":
    print(run_threads())

 
 
