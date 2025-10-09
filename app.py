dict_apple = {"name":"Apple","price":5.0,"brand":"ShopRite"}
dict_pear = {"name":"Pear","price":4.0,"brand":"KirkLand"}
dict_kangaroo = {"name":"Kangaroo","price":559.99,"brand":"Austrila"}

store=[dict_apple, dict_pear, dict_kangaroo]
for item in store:
    print (f"{item["name"]}" f" ${item["price"]}" f" ({item["brand"]})")
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