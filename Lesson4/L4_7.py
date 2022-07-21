result = [] 
my_list =  [1,1,2,3,4,3,0,0]
print ("The list is: ", my_list) 

for i in my_list: 
    if i not in result: 
        result.append(i) 

print ("The list after removing duplicates : ", result)
