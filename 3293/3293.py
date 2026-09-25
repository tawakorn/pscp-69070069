"""BIG FRAME"""

lines = []
for _ in range(5):
    lines.append(input())

max_len = 0
for line in lines:
    if len(line) > max_len:
        max_len = len(line)

border = "*" * (max_len + 4)

print(border)
for line in lines:
    spaces = " " * (max_len - len(line))
    print("* " + line + spaces + " *")
print(border)
