"""SEASONWOW"""

MONTH = int(input())
DAY = int(input())

if MONTH in {1,2}:
    print("winter")
elif MONTH == 3:
    if DAY < 21:
        print("winter")
    else:
        print("spring")
elif MONTH in {4,5}:
    print("spring")
elif MONTH == 6:
    if DAY < 21:
        print("spring")
    else:
        print("summer")
elif MONTH in {7,8}:
    print("summer")
elif MONTH == 9:
    if DAY < 21:
        print("summer")
    else:
        print("fall")
elif MONTH in {10,11}:
    print("fall")
elif MONTH == 12:
    if DAY < 21:
        print("fall")
    else:
        print("winter")
