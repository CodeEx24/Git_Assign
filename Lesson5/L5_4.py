productName = "Initialize"
product_Dict = {}

while(productName != ""):
    print("Press ENTER in Product Name when you are done!")
    productName = input("Product Name: ")
    if productName != "":
        productPrice = float(input("Product Price: "))
        #I add the capitalize function so it is easier for the user to type a product without pressing shift.
        product_Dict[productName.capitalize()] = productPrice 

#For checking purposes
print("Product List: ", product_Dict)

while(True):
    productName = input("Please enter the product name: ")
    if productName.capitalize() in product_Dict.keys():
        print("The price of the", productName.capitalize(), "is" ,product_Dict[productName.capitalize()])
    else:
        print(productName.capitalize(), "is not in the dictionary.")