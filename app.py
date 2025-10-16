store=[{'name':"Apple",'price':5.0,'brand':"ShopRite"},
{'name':"Pear",'price':4.0,'brand':"KirkLand"},
{'name':"Kangaroo",'price':559.99,'brand':"Austrila"}]
for index, item in enumerate(store):
    print(index, ":", item["name"])
    print (item["name"], item["price"] item["brand"])

    #print (f"store {item}[name]")
    #print (f"{item} ['name'] ${item ['price]'} {item ["brand"]}")
#print(store)

isitem = False
done = False
while done == False:
    while isitem == False:
        choice = input("Please choose one item to purchase: ")
        for item in store:
            if choice == item["name"]:
                print(f"You have purchased one {item["name"]} for ${item["price"]}")
                isitem = True
                again = input("Would you like to purchase more Y or N: ")
                if again == "N" or again == "n":
                    done = True
        if isitem == False:
            print ("Try again")

