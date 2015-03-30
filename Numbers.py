from math import pow, factorial
__author__ = 'edwardvella'

###
#Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
#Keep a limit to how far the program will go.
###
def find_pi_to_the_nth_digit(n):
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
#Find e to the Nth Digit - Just like the previous problem, but with e instead of PI.
#Enter a number and have the program generate e up to that many decimal places.
#Keep a limit to how far the program will go.
###
def find_e_to_the_nth_digit(x):
    result = 0.0
    for n in range(0, x):
        result += pow(x, n) / factorial(n)
    return result


###
#Fibonacci Sequence -
#Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
###
def fibonacci_sequence(n):
    result = 0
    if n < 2:
        return n
    return fibonacci_sequence(n - 2) + fibonacci_sequence(n - 1)


###
#Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
###
def prime_factorization(n):
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
#Determines whether a number is a prime number.
###
def is_prime_number(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

###
#Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
###
def next_prime_number(prime_number):
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
    width = float(raw_input('What is the width of the floor plan? '))
    height = float(raw_input('What is the height of the floor plan? '))
    cost = float(raw_input('What is the cost of a single tile? '))
    print 'The total cost of the floor plan is ' + str(find_cost_of_tile(width, height, cost))


###
# Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given
# interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity,
# add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
###
def calculate_mortgage():
    None
