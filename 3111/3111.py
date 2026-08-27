"""sahakon"""

M = input()
things = int(input())

total_price = 0

for _ in range(things):
    price = float(input())
    total_price += price

if M == "Y":
    de = total_price * 5/100
    total_price -= de
elif M == "N" and total_price >= 500:
    de2 = total_price * 3/100
    total_price -= de2

print(f"{total_price + 0.000001:.2f}")
