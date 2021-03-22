sum = 0
numbers = [1,2]

while numbers[-1] <= 4_000_000:
    numbers.append(numbers[-1]+numbers[-2])

for number in numbers:
    if number <= 4_000_000 and number % 2 == 0:
        sum += number

print(sum)