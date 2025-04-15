import threading
import time
count = 0
turn = 0
def soma1(valor):
    global count
    global turn
    for i in range(0,valor):
        a = 0
        while turn != 0:
            continue
        a = count
        time.sleep(0.01)
        count = a+1
        turn = 1

def soma2(valor):
    global count
    global turn
    for i in range(0,valor):
        a = 0
        while turn != 1:
            continue
        a = count
        time.sleep(0.01)
        count = a+1
        turn = 0
        
        
if __name__ == "__main__":
    t1 = threading.Thread(target=soma1(10))
    t2 = threading.Thread(target=soma2(10))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(count)