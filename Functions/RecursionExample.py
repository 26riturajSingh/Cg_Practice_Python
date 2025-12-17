n = 1234

def sum_of_digits(n):
    if n%10 == 0:
        return 0

    return sum_of_digits(n//10) + n%10

print(sum_of_digits(n))
