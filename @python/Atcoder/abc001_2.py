m = int(input())

km = m / 1000

if km < 0.1:
    print("00")
elif km < 1:
    print(f"0{int(km*10)}")
elif km <= 5:
    print(f"{int(km*10)}")
elif km <= 30:
    print(f"{int(km+50)}")
elif km <= 70:
    print(f"{int(((km-30)/5)+80)}")
else:
    print(89)