"""ARCADE OF TIME STORE CHECK"""

line1 = input().split()
num = int(line1[0])
check = int(line1[1])

start_times = []
stop_times = []

for i in range(num):
    time_data = input().split()
    start_times.append(int(time_data[0]))
    stop_times.append(int(time_data[1]))

queries = input().split()

for i in range(check):
    q = int(queries[i])
    count = 0

    for j in range(num):
        if q >= start_times[j]:
            if q < stop_times[j]:
                count = count + 1
            else:
                pass
        else:
            pass

    print(count, end=" ")
