#Previous Code
list = []
list.append(67)
list.append(62.9)
list.append("hi")
list.append(False)
list += [8] 
list += [67] 
list += ["Apple"] 
list += [6.5]

#I add the print so it can be  seen what happen in code.
#Letter A
list.append("banana")
list.append(67)
print(list)
#Letter B
list.insert(2, "dog")
print(list)
#Letter C
list.insert(0, 909)
print(list)
#Letter D 
print(list.index("hi"))
#Letter E
print(list.count(67)) 
#Letter F
list.remove(67)
print(list)
#Letter G
list.pop(4)
print(list)
