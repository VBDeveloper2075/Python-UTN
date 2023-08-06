import queue

q=queue.LifoQueue()
#LIFO
for x in range(3):
    q.put(x)

print(list(q.queue))
while not q.empty():
    print(q.get(), end="\t")