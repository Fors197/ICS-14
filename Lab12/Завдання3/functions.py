def count_even(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n //= 10
    return count


def multiply_odd(n):
    product = 1
    found = False

    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
            found = True
        n //= 10

    if found:
        return product
    return 0
