import queue

q = []
q.append(10)
q.append(60)
q.append(20)
q.append(80)
print(q)
q.append(40)
q.append(30)
q.sort()
print(q)
q.pop(0)
q.pop(0)
print(q)
q.pop(0)
q.pop(0)
print(q)


que = queue.PriorityQueue()
que.put(10)
que.put(20)
que.put(50)
que.put(40)
que.put(30)
que.get()
que.get()
for i in range(que.qsize()):
    print(que.get())


r = []
r.append((1,"Shubham"))
r.append((2,"Apurv"))
r.append((5,"Omkaar"))
r.append((8,"Lokesh"))
print(r)
r.append((3,"Bhavesh"))
r.append((6,"Gaurav"))
r.sort()
print(r)
r.pop(0)
r.pop(0)
print(r)
r.pop(0)
print(r)
