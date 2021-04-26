# 반복문
for score in range(1, 4):
    print(score, end = " ")

sum = 0
for a in range(1, 4):
    sum += a
print(sum)

while True:
    a = input("input(while): ")
    if a == "while":
        print("go")
    else:
        break 