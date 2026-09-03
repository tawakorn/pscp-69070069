"""PRIME NUMBER"""

data = input().split()
start_number = int(data[0])
end_number = int(data[1])

if start_number > end_number:
    start_number, end_number = end_number, start_number

primes = []

for num in range(start_number, end_number + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if not num % i:
                is_prime = False
                break

        if is_prime:
            primes.append(str(num))

if len(primes) > 0:
    print(" ".join(primes))

print("Total primes:", len(primes))
