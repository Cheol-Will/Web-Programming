# 제어문 - 분기문
# if(조건)

# ex)1
score = int(input("input score: "))

if score >= 85:
    print("pass")
else:
    print("fail")

activity = input("what club: ")

if(activity == "멋사"):
    print("어 너도 멋사야?")
else:
    print("그...그래...")

money = int(input("how much money: "))

if money >= 5000:
    print("outback")
elif money >= 3000:
    print("school cafeteria")
elif money >= 1000:
    print("cup ramyeon")
else:
    print("rice")
