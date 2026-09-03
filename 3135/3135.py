"""ของขวัญและขโมย"""

data = input().split()
n = int(data[0])
k = int(data[1])
t = int(data[2])

if t == 1:
    print(1)
else:
    current = 1
    count = 1

    while True:
        current = current + k

        if current > n:
            current = current - n

        if current == 1:
            break

        count = count + 1

        if current == t:
            break

    print(count)
