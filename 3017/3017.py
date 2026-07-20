"""bill"""

money = int(input())

ser_cal = money * (10/100)


if ser_cal < 50:
    ser_cal = 50
elif ser_cal > 1000:
    ser_cal = 1000

vat = (money + ser_cal) * (7/100)

real_price = money + vat + ser_cal

print(f"{real_price:.2f}")
