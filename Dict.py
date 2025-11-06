store = [
    {'name': "Apple", 'price': 5.0, 'brand': "ShopRite"},
    {'name': "Pear", 'price': 4.0, 'brand': "KirkLand"},
    {'name': "Kangaroo", 'price': 559.99, 'brand': "Austrila"}
]

for index, item in enumerate(store):
    print(f" {item['name']} ${item['price']}, {item['brand']}")

cart = []
done = False
total=0

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
    a=False
    while not a:
        again = input("Would you like to purchase more items? (Y/N): ")
        if again == 'N':
            done = True
            a=True 
        elif again == 'Y':
            a=True
        elif again != 'N' or 'Y':
            print("Try again")

print("Your cart:")
for item in cart:
    print(item)
print (f"Total: ${total}")
print("Thank you for wasting your money")
