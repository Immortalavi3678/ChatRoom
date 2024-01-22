import threading as th
import time
def fun1():
    for i in range(10):
        print(f"{i} in fun 1  ,")
        time.sleep(1)

def fun2():
    for i in range(5):
        print(f"{i} in fun 2  ,")
        time.sleep(1)
        
start = time.perf_counter()
##fun1()
##fun2()
t1 = th.Thread(target=fun1)
t2 = th.Thread(target=fun2)
t1.start()
t2.start()
t1.join()
t2.join()

print("ETA: ",time.perf_counter()-start)
