"""FROG JUMP"""

x, y = map(int, input().split())

total_distance = 0
jumps = 0
current_jump = x

while total_distance < y:
    if current_jump <= 0:
        jumps = -1
        break
    total_distance += current_jump
    jumps += 1
    current_jump -= 2

print(jumps)
