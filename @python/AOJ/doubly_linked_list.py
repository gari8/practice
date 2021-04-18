from collections import deque

n = int(input())

lis = deque()


def execution(cmd, num):
    if cmd == 'insert':
        lis.appendleft(num)
    elif cmd == 'delete':
        if len(lis) > 0:
            try:
                lis.remove(num)
            except:
                pass
    elif cmd == 'deleteFirst':
        if len(lis) > 0:
            lis.popleft()
    elif cmd == 'deleteLast':
        if len(lis) > 0:
            lis.pop()


for _ in range(n):
    in_cmd = input()
    if in_cmd == 'deleteFirst':
        execution(in_cmd, 0)
    elif in_cmd == 'deleteLast':
        execution(in_cmd, 0)
    else:
        cmd, num = in_cmd.split()
        execution(cmd, num)

print(*lis)
