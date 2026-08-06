"""COUNT SARA"""

message = input().lower()
sara = [ "a","e","i","o","u"]

for i in sara:
    count = message.count(i)

    if count > 0:
        print(f"{i} : {count}")
