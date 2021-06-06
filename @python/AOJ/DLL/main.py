from collections import deque

ops = {"insert ": deque.appendleft,
       "delete ": lambda deq, x: deq.remove(x) if x in deq else None,
       "deleteF": deque.popleft,
       "deleteL": deque.pop}

deq = deque()
for _ in range(int(input())):
    op = input()
    if op[6] == " ":
        ops[op[:7]](deq, op[7:])
    else:
        ops[op[:7]](deq)
print(*deq)
