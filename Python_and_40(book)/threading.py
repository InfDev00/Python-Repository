import threading

def sum(name, value):
    for i in range(0, value):
        print(f"{name} : {i}")

t1 = threading.Thread(target=sum, args=('first thread', 10))
t2 = threading.Thread(target=sum, args=('second thread', 10))

t1.start()
t2.start()

print("main thread")