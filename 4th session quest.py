a = [1, 2, 3, ["a", "b", "c"]]

print("a:", a)
print("a[3]:", a[3])
print("a[3][1]:", a[3][1])
print("length:", len(a))

a.append(4)
print("a:", a)

a.insert(0, 5)
print("a:", a)

a.remove(3)
print("a:", a)

b = {1: "하나", 2: "둘", 3: "셋"}
print("b:", b)

b[4] = "넷"
print("b:", b)

del b[4]
print("b:", b)