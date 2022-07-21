def factors(n):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result

#The code below is for testing
num = int(input("Enter an integer: "))
print("List of factors:",factors(num))
