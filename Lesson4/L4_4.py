size = int(input("Input the size of list: "))
list = []
ctr = 0
result = "No"

for i in range(0, size):
    list.append(int(input("Please enter an integer for the list: ")))

print("List result:", list)

#Letter A
print("\nThe sum of list is", sum(list))
#Letter B
print("Last item in the list is", list[-1])
#Letter C
print("Reverse of list: ", list[::-1])
#Letter D
for i in list:
    if(i == 5):
        result = "Yes"
        break
print(result)
#Letter E
for i in list:
    if(i < 5):
        ctr += 1
print(ctr)
#Letter F
list.pop(0)
list.pop(-1)
list = sorted(list)
print(list)