
n = input('Please give me an integer: ')
n = int(n)

total = 0
for x in range(1, (n + 1)):
    if (x % 3 == 0) or (x % 5 == 0):
        total += x

print(total)
