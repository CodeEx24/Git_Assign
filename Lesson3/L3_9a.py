def primes(n=100):
    result = []
    for i in range(1, n):
        for j in range (2, i):
            if(i % j == 0):
                break
        else :
            result.append(i)
    return result

#The code below is for testing
print(primes())
