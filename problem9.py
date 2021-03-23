import math
# pythagorean triplet

def _check_if_pythagorean(a, b, c):
    pythagorean = a**2 + b**2 == c**2
    if pythagorean:
        return True

def _check_if_sum_is_1000(a, b, c):
    sum_1000 = a + b + c == 1000
    if sum_1000:
        return True

def _find_abc(limit):
    for a in range(1, limit):
        for b in range(1, limit):
            if a < b:
                c = math.sqrt(a ** 2 + b ** 2)
                if _check_if_sum_is_1000(a, b, c):
                    return a, b, c

a, b, c = _find_abc(1000)

print(f"The triplet is: {a}², {b}² = {c}²")
print(f"The product is: {(a*b*c)}")
