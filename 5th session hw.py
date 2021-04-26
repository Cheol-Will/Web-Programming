str1 = "asdf asdf, asdf, fdsa fdsa"
str2 = "qwertyuio"
print(str1+str2)
print(str1*3)
print(str1[0])
print(str1[1:5])

# string 내장함수
# len()
print(len(str1))

# 특정 문자의 등장 횟수
print(str1.count("a"))

# 문자열을 특정 기준으로 나누자: str1.split() --> return list
print(str1.split())
print(str1.split(","))

# 특정 문자 인덱스 찾기
print(str1.index("f"))
print(str1.find("f"))


# list 내장함수
ml = [3, 1, "baebae", 4, "hungry", 6, 1]
mylist = [4, 5, 2, 3, 1, 3, 4, 5, 3, 2, 3, 4, 1]
print(ml)
print(mylist)

# list length
print(len(ml))

# list sort
mylist.sort()
print(mylist)

# 리스트 내의 특정 원소 인덱스 .index()
print(mylist.index(3))

# 리스트 내의 특정 원소 갯수 세기 .count()
print(mylist.count(3))


# dictionary
mydict = {"a": "aaa", "b": "bbb", "c": "ccc"}
print(mydict)

# key value 추가
mydict["d"] = "hey"
print(mydict)

# del 변수[키]
del mydict["d"]
print(mydict)

# key로 value 얻기
print(mydict.get("a"))


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

# 반복문
for score in range(1, 11):
    print(score)

sum = 0
for a in range(1, 11):
    sum += a
print(sum)

while True:
    a = input("input(while): ")
    if a == "while":
        print("go")
    else:
        break 