def amicable_numbers_sum(limit):
    def sum_of_divisors(n):
        return sum(i for i in range(1, n) if n % i == 0)

    amicable_numbers = set()

    for num in range(1, limit + 1):
        partner = sum_of_divisors(num)
        if partner != num and sum_of_divisors(partner) == num:
            amicable_numbers.add(num)
            amicable_numbers.add(partner)

    return sum(amicable_numbers)
assert amicable_numbers_sum(999)==504
assert amicable_numbers_sum(9999)==31626
assert amicable_numbers_sum(99)==0