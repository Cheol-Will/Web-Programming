print(12+1234)
number = 3
print(number+1)

a = input('반장 이름을 입력하세요: ')
print("우리반 반장 이름은", a)

# integer float
num1 = int(input("첫번째 숫자: "))
num2 = float(input("두번째 숫자: "))
print(num1 + num2)
print(num1//num2)
print(num1%num2)
print(num1**num2)

a = list(range(1, 10))
a[0] = 100
print(a*3)
b = tuple(range(1, 10))
# b[0] = 100 불가능
print(b*3)

a = {"a": 1234, "b": 431, "c": 339}
print(a)