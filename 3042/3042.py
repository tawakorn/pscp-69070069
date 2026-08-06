"""DIV TEN"""

num = int(input())

div_ten = []

for i in range(num , -1 ,-1):
    if not i % 10 :
        div_ten.append(i)

print(*div_ten)
