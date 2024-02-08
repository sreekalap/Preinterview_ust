#checking divisiblity by 5 and 7 Program
def divisible_by_5_and_7(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield str(num)


def print_divisible_numbers(n):
    divisible_nums = divisible_by_5_and_7(n)
    print(','.join(divisible_nums))


# Example
#print_divisible_numbers(100)

