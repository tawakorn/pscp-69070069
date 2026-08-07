"""UNICORN"""
first , last = input().split()
weight = float(input())

tax = 0
weighttax = 0

if first == "BKK" and last == "CNX":
    tax = 10
    weighttax = weight * 30
    print(f"{tax + weighttax:.2f}")
elif first == "CNX" and last == "UBP":
    tax = 15
    weighttax = weight * 40
    print(f"{tax + weighttax:.2f}")
elif first == "UBP" and last == "BKK":
    tax = 20
    weighttax = weight * 40
    print(f"{tax + weighttax:.2f}")
elif first == "BKK" and last == "PKT":
    tax = 25
    weighttax = weight * 50
    print(f"{tax + weighttax:.2f}")
elif first == "PKT" and last == "CNX":
    tax = 30
    weighttax = weight * 60
    print(f"{tax + weighttax:.2f}")
elif first == "UBP" and last == "PKT":
    tax = 40
    weighttax = weight * 70
    print(f"{tax + weighttax:.2f}")
else:
    print("Error")
