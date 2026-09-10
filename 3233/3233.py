"""SARAK"""

win_letter, win_num = input().split()
my_letter, my_num = input().split()

same_letter = win_letter == my_letter

if same_letter and win_num == my_num:
    print(1000000)
elif not same_letter and win_num == my_num:
    print(100000)
elif same_letter and win_num[-3:] == my_num[-3:]:
    print(2000)
elif same_letter and win_num[-2:] == my_num[-2:]:
    print(1000)
elif not same_letter and win_num[-3:] == my_num[-3:]:
    print(200)
elif not same_letter and win_num[-2:] == my_num[-2:]:
    print(100)
elif same_letter:
    print(20)
else:
    print(0)
