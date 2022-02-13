import math

k = 1158

if __name__ == '__main__':
    print(math.floor(k/100)*100, k - math.floor(k/100)*100)
    for i in range(1, 10+1):
        print(i)