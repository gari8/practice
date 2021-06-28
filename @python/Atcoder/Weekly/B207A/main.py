a,b,c = map(int, input().split())

if __name__ == '__main__':
    l = list([a,b,c])
    m = min(l)
    l.remove(m)
    print(sum(l))