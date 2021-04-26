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
