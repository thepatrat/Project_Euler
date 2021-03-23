
numbers = []

for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        numbers.append(number)
    else:
        continue

print(sum(numbers))