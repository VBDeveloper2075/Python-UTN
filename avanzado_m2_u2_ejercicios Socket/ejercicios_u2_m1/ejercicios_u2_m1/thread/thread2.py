import queue
import threading
import time

def agregar_item(q):
    while True:
        print("inicio del hilo")
        q.put(4)
        time.sleep(2)
        print(list(q.queue))
        print("Ejecución antes del break")
        break

q=queue.Queue()
t=threading.Thread(target=agregar_item, args=(q,))
t.start()

q.put(3)
q.join()
print(list(q.queue))