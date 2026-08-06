"""A-B range and Div D and r left"""

a = int(input())
b = int(input())
d = int(input())
r = int(input())

count = 0

for i in range(a,b+1, +1 ):
    if i % d == r:
        count = count +1

print(count)
