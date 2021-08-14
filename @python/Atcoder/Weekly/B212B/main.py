# import sys
# input = sys.stdin.readline
# xl = list(input().strip("\n"))
# if __name__ == '__main__':
#     if len(set(xl)) == 0:
#         print("Weak")
#         exit(0)
#     for i in range(3, 0, -1):
#         pre = i - 1
#         if i != 0 and int(xl[i]) - int(xl[pre]) == 1:
#             print("Weak")
#             exit(0)
#         if int(xl[pre]) == 0 and int(xl[i]) == 9:
#             print("Weak")
#             exit(0)
#     print("Strong")

a = input()
same,step = True,True
for i in range(3):
    print(a[i])
    if a[i]!=a[i+1]:
        same=False
    if (int(a[i])+1)%10!=int(a[i+1]):
        step=False
if(same or step):
    print("Weak")
else:
    print("Strong")

