store=[{'name':"Apple",'price':5.0,'brand':"ShopRite"},
{'name':"Pear",'price':4.0,'brand':"KirkLand"},
{'name':"Kangaroo",'price':559.99,'brand':"Austrila"}]
for index, item in enumerate(store):
    print (f"{index}:{item['name']} ${item['price']}, {item['brand']}")

    #print (f"store {item}[name]")
    #print (f"{item} ['name'] ${item ['price]'} {item ["brand"]}")
#print(store)

cart=[]
isitem = False
done = False
while done == False:
    while isitem == False:
        choice = input("Please choose one item to purchase: ")
        for item in store:
            if choice == item["name"] or {index}:
                print(f"You have purchased one {item["name"]} for ${item["price"]}")
                isitem = True
                select = (choice)
                cart.append (select)#({item["name"]}, {item["price"]})
                again = input("Would you like to purchase more Y or N: ")
                if again == "N" or again == "n":
                    print (f"You have bought {cart}")
                    done = True
                    
            if isitem == False:
                print ("Try again")

