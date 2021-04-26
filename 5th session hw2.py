# list 내장함수
ml = [3, 1, "baebae", 4, "hungry", 6, 1]
mylist = [4, 5, 2, 3, 1, 3, 4, 5, 3, 2, 3, 4, 1]
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

