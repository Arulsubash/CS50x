from cs50 import get_int
while True:
    a = get_int("Height: ")
    if a >= 1 and a <= 8 and type(a) is int:
        break
n = 1
space = a - 1
while n <= a:
    for i in range(space):
        print(" ", end="")
    space -= 1
    for j in range(n):
        print("#", end="")
    print("  ", end="")
    for k in range(n):
        print("#", end="")
    print()
    n += 1
