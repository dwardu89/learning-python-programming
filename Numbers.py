from math import pow, factorial

__author__ = 'edwardvella'


###
# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.
###
def find_pi_to_the_nth_digit(n):
    """
    Finds pi to the Nth digit
    :param n: the Nth digit to compute to
    :return: pi to the Nth digit
    """
    result = 0.0
    for k in range(0, n):
        a = float(1) / pow(16, k)
        b = float(4) / (8 * k + 1)
        c = float(2) / (8 * k + 4)
        d = float(1) / (8 * k + 5)
        e = float(1) / (8 * k + 6)
        result += a * (b - c - d - e)
    return result


###
# Find e to the Nth Digit - Just like the previous problem, but with e instead of PI.
# Enter a number and have the program generate e up to that many decimal places.
# Keep a limit to how far the program will go.
###
def find_e_to_the_nth_digit(x):
    """
    Finds the exponential digit to the nth digit
    :param x: the Nth digit to compute to
    :return: the result to the Nth digit
    """
    result = 0.0
    for n in range(0, x):
        result += pow(x, n) / factorial(n)
    return result


###
# Fibonacci Sequence -
# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
###
def fibonacci_sequence(n):
    """
    Calculates a fibonacci sequence
    :param n: the Nth number
    :return: the fibonacci sequence to the number
    """
    result = 0
    if n < 2:
        return n
    return fibonacci_sequence(n - 2) + fibonacci_sequence(n - 1)


###
# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
###
def prime_factorization(n):
    """
    Finds all the prime factors of a number
    :param n: the number
    :return: a list of prime factors
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


###
# Determines whether a number is a prime number.
###
def is_prime_number(n):
    """
    Determines whether a given number is a prime number
    :param n:
    :return: True if prime number, False if not a prime number
    """
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


###
# Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
###
def next_prime_number(prime_number):
    """
    Calculates the next prime number preceding the current prime number
    :param prime_number: the current prime number
    :return: the next prime number
    """
    next_number = prime_number + 1

    while True:
        if not is_prime_number(next_number):
            next_number += 1
        else:
            break
    return next_number


###
# A function used to get the next prime number after getting a user input, this will continuously call next_prime_number
# till the user enters 'n'
###
def get_prime_number():
    """
    Loops and prints a prime number until the user stops requesting a prime number.
    :return:
    """
    currentPrime = 1
    while True:
        answer = raw_input('Would you like to see the next prime? (Y/N) ')

        if answer.lower().startswith('y'):
            print currentPrime
            currentPrime = next_prime_number(currentPrime)
        else:
            break


###
# Find Cost of Tile to Cover W x H Floor -
# Calculate the total cost of tile it would take to cover a floor plan of width and height,
# using a cost entered by the user.
###
def find_cost_of_tile(w, h, cost):
    return w * h * cost


###
# A function used to get the cost, width and height of a plan and return the cost
###
def get_cost_of_tile():
    """
    Calculates the cost of the tile
    :return: None
    """
    width = float(raw_input('What is the width of the floor plan? '))
    height = float(raw_input('What is the height of the floor plan? '))
    cost = float(raw_input('What is the cost of a single tile? '))
    print 'The total cost of the floor plan is ' + str(find_cost_of_tile(width, height, cost))


###
# Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given
# interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity,
# add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
# This uses the formula found on Wikipedia:
#
#    c = ______rP________
#        1 - (1 + r) ^ -N
#
#   r - the monthly interest rate, expressed as a decimal, not a percentage. Since the quoted yearly percentage rate is
#   not a compounded rate, the monthly percentage rate is simply the yearly percentage rate divided by 12; dividing the
#   monthly percentage rate by 100 gives r, the monthly rate expressed as a decimal.
#   N - the number of monthly payments, called the loan's term, and
#   P - the amount borrowed, known as the loan's principal.
#
#
#   Amount owed at end of month N = (1 + r)^N*P - __(1+r)^N_-1__ * c
#                                                        r
###
def calculate_mortgage(monthly_rate, monthly_payments, amount_borrowed, months_in_payment):
    """
    Calculates the amount owed by a mortgage by the end of the month.
    :param monthly_rate: the monthly interest rate, expressed as a float.
    :param monthly_payments: the number of monthly payments
    :param amount_borrowed: the amount borrowed
    :return: the amount owed after N months
    """

    rate = float(monthly_rate) / 12 / 100

    c = (rate * amount_borrowed) / (1 - pow(1 + rate, (-1) * monthly_payments))

    amount_owed = (pow(1 + rate, monthly_payments) * amount_borrowed) - months_in_payment * c
    return amount_owed


####
# Change Return Program - The user enters a cost and then the amount of money given.
# The program will figure out the change and the number of 1 Pound coins, 50 p coins, 10 p coins, 5 p coins, 2 p coins
# and 1 p coins needed for the change.
####
def calculate_change(total_cost, money_paid):
    """
    Calculates the change returned when more money is paid, it also prints change given in coins, and if there is less
    money given, the amount required to pay is shown.
    :param total_cost: the total cost to be paid
    :param money_paid: the amount paid
    :return: None
    """
    from math import floor
    change = money_paid - total_cost
    if change > 0:
        print str(floor(change / 1)) + ' 1 GBP Coins'
        change -= floor(change / 1) * 1

        print str(floor(change / 0.5)) + ' 50p Coins'
        change -= floor(change / 0.5) * 0.5

        print str(floor(change / 0.1)) + ' 10p Coins'
        change -= floor(change / 0.1) * 0.1

        print str(floor(change / 0.05)) + ' 5p Coins'
        change -= floor(change / 0.05) * 0.05

        print str(floor(change / 0.02)) + ' 2p Coins'
        change -= floor(change / 0.02) * 0.02

        print str(floor(change / 0.01)) + ' 1p Coins'
        change -= floor(change / 0.01) * 0.01
    else:
        print str(change) + ' GBP is still owed'
