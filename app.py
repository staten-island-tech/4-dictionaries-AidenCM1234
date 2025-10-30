store = [
    {'name': "Apple", 'price': 5.0, 'brand': "ShopRite"},
    {'name': "Pear", 'price': 4.0, 'brand': "KirkLand"},
    {'name': "Kangaroo", 'price': 559.99, 'brand': "Austrila"}
]

for index, item in enumerate(store):
    print(f"{index}: {item['name']} ${item['price']}, {item['brand']}")

cart = []
total = 0
done = False

while not done:
    isitem = False
    while not isitem:
        choice = input("Please choose one item to purchase: ")
        
        for item in store:
            if choice == item["name"]: 
                print(f"You have purchased one {item['name']} for ${item['price']}")
                cart.append(f"{item['name']} - ${item['price']}")
                total+=item['price']
                isitem = True
        
        if not isitem:  
            print("Try again")


    again = input("Would you like to purchase more items? (Y/N): ")
    if again == 'N':
        done = True  
        
print("Your cart:")
for item in cart:
    print(item)
print (f"Total:{total}")
print("Thank you for wasting your money")
