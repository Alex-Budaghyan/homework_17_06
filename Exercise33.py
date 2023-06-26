def f(i, number, count, k):
    if i >= count:
        return
    print(f"At the top i is {i}")
    number.append(i)
    print("Numbers now: ", number)
    print(f"At the bottom i is {i}")
    f(i + k, number, count, k)


q = 0
numbers = []
n = int(input("Enter n: "))
addCount = int(input("Enter count: "))
f(q, numbers, n, addCount)
print("The numbers: ")
for num in numbers:
    print(num)