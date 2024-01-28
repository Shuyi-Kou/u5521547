inventory={}
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Add{quantity}{item}(s).")
    
def view_inventory():
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    
def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"Updated {item} quantity to {quantity}.")
    else:
        print(f"{item} not found")
def manage_invntory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ["1","2","3","4"]:
            if choice == "1":
                item = input("请输入存货名称 ")
                quantity = int(input("请输入数量 "))   
                add_item(item, quantity) 
            elif choice =="2":
                print(view_inventory())
            elif choice == "3":
                item = input("请输入存货名称 ")
                quantity = int(input("请输入数量 "))   
                update_item(item, quantity)
            else:
                print("Exiting Inventory Management System.")
                break
        else:
            print("error")
manage_invntory()
                    
                        
                    
