"""BRICKBRIGE"""

a = int(input())
b = int(input())
goal = int(input())

big_use = goal // 5

if big_use > b:
    big_use = b

small_use = goal - (big_use * 5)

if small_use <= a:
    print(small_use)
else:
    print(-1)
