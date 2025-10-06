from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

front_element = queue.popleft()
print(front_element)
print(queue)