length = int(input("Enter the size of the pattern: "))
lines = 0
while lines < length:
    for n in range(1, length + 1):
        print("*", end="")
    print()
    lines += 18