n = int(input())
a_list = list(map(int, input().split()))

a_list.sort(reverse=True)

alice = 0
bob = 0

for i, a in enumerate(a_list):
    if i % 2 == 0:
        alice += a
    else:
        bob += a

if __name__ == '__main__':
    print(alice - bob)