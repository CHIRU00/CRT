import queue
a=queue.Queue()
b=queue.Queue()
for i in range(5):
    b.put(i)
print(a.empty())
print(b.empty())


l=queue.Queue()
l.put(10)
l.put(20)
print(type(l))
print(l.get())
print(l.get())
print(a)
