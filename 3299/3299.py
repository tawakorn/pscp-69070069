"""แปลงดอกไม้"""

data = input().split()
L = int(data[0])
N = int(data[1])

total_planted = 0
current_diag = 1

while total_planted < N:
    total_planted = total_planted + current_diag
    current_diag = current_diag + 1

FINAL_DIAG = current_diag - 1

if not FINAL_DIAG % L:
    stripe = FINAL_DIAG // L
else:
    stripe = (FINAL_DIAG // L) + 1

print(stripe)
