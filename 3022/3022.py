"""TEM"""
temp = float(input())
type_1 = input()
type_2 = input()


new_temp = 0.0

if type_1 == "K":
    new_temp = temp - 273.15
elif type_1 == "F":
    new_temp = 5/9 * (temp - 32)
elif type_1 == "R":
    new_temp = (temp * 5 / 9) - 273.15
elif type_1 == "C":
    new_temp = temp

final_temp = 0.0

if type_2 == "K":
    final_temp = new_temp + 273.15
elif type_2 == "F":
    final_temp = new_temp * 9 / 5 + 32
elif type_2 == "R":
    final_temp = (new_temp + 273.15) * 9 / 5
elif type_2 == "C":
    final_temp = new_temp

print(f"{final_temp:.2f}")
