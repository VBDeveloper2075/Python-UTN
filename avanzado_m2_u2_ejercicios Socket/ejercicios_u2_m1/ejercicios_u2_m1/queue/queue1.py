import queue

q=queue.Queue()
q.put(5)
print(list(q.queue))
print(q.empty())
print(q.get())
print(list(q.queue))

#FIFO
for x in range(3):
    q.put(x)

print(list(q.queue))
while not q.empty():
    print(q.get(), end="\t")