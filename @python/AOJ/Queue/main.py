from collections import deque

N, Q = map(int, input().split())
procs = deque([name, int(time)] for name, time in [input().split() for _ in range(N)])


def queue(dq, q) -> None:
    time = 0
    while dq:
        [name, val] = dq.popleft()
        if val - q > 0:
            dq.append([name, val - q])
            time += q
        else:
            time += val
            print(name, time)


if __name__ == '__main__':
    queue(procs, Q)
