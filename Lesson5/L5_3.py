days  =  {'January':31,  'February':28,  'March':31,  'April':30,  'May':31,  'June':30,  'July':31,  'August':31, 'September':30, 'October':31, 'November':30,  'December':31}

#Letter A
month = input("Enter a month name: ")
if month.capitalize() in days.keys():
    print("There are", days.get(month.capitalize()), "days in the month of", month.capitalize())

#Letter B
print("\n", sorted(days.keys()))

#Letter C
result = []
for m in days.keys():
    if days[m] == 31:
        result.append(m)
print("\n31 Days: ", result)

#Letter D
print("\n", sorted(days.items(), key=lambda x: x[1]))