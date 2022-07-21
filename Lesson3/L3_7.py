def number_of_factors(n):
    factors = 0
    for i in range(1, num+1):
        if num % i == 0:
            factors += 1
    return factors

#The code below is for testing
num = int(input("Enter an integer:  "))
print("It has", number_of_factors(num), "factors")