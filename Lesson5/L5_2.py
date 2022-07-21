list = []
for i in range(0, 5):
    #I input in list first because the tuples are immutable
    list += [int(input("Please enter an integer for index " +  str(i) +": "))]

#Convert the list into tuple
tuple_list = tuple(list)
print(tuple_list)

#K integer for divisibility
K = int(input("Enter an integer for K: "))

#Checking each value if there are divisible by K then print it
for i in tuple_list:
    if i % K == 0:
        print("The tuple", i, "is divisible by", K)