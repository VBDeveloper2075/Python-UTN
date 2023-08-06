import queue

q=queue.PriorityQueue()

q.put((13, "Este es el último"))
q.put((3, "Este va segundo"))
q.put((4, "Este va tercero"))
q.put((2, "Este va primero"))

for i in range(q.qsize()):
    print(q.get())