





resources = [
  {
    "id": "R001",
   "name": "Laptop",
   "category": "Electronics", 
   "total": 10, 
   "available": 10
   },

  {
    "id": "R002",
   "name": "Keyboard", 
   "category": "Accessories", 
   "total": 5, 
   "available": 5
 },
   
  {
    "id": "R003", 
    "name": "Headset", 
    "category": "Accessories", 
    "total": 3, 
    "available": 3
 }
]

fellows = {
    "F001": "Ada",
    "F002": "John",
    "F003": "Grace"
}

borrow_records = []


def add_resource():
    print("----Add Resource----")
    resource_id = input("Enter resource ID: ")
    for resource in resources:
        if resource["id"] == resource_id:
            print("Resource ID already exists.")
            return
#add_resource()
    resource_name = input("Enter resource Name: ")
    resource_category = input("Enter resource category: ")
    try:
        resource_total = int(input("Enter total units: "))
    except ValueError:
        print("please enter a valid number")
        return


    if resource_total <= 0:
        print("Total unit must be greater than zero.")
        return

    new_resource = {
      "id": resource_id,
      "name": resource_name,
      "category": resource_category,
      "total": resource_total,
      "available": resource_total
    }
    resources.append(new_resource)
    print("Resources added successfully.")
#add_resource()
#fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
#borrow_records = []
def list_resources():
    print("\n---- RESOURCE INVENTORY -----")

    for resource in resources:
        print(f"ID: {resource['id']}")
        print(f"Name: {resource['name']}")
        print(f"Category: {resource['category']}")
        print(f"Total units: {resource['total']}")
        print(f"Available units: {resource['available']}")
        print("-" * 30)
#list_resources()

def borrow_resource():
    print("\n----- BORROW RESOURCE -----")

    fellow_id = input("Enter fellow ID: ")

    if fellow_id not in fellows:
        print("Fellow ID not found.")
        return
    resource_id = input("Enter resource ID: ")
    resource = None

    for item in resources:
        if item["id"] == resource_id:
            resource = item
            break

    if resource is None:
        print("Resource ID not found.")
        return
    
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if quantity <= 0: # quantity should be positive
        print("Quantity must be greater than zero.")
        return

    if quantity > resource["available"]: # checking available stock
        print("Not enough units available.")
        return

    resource["available"] = resource["available"] - quantity

    borrow_records.append({
        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": quantity
    })

    print(f"{fellows[fellow_id]} borrowed {quantity} unit(s) of {resource['name']}.")


def return_resource():
    print("\n----- RETURN RESOURCE -----")

    fellow_id = input("Enter fellow ID: ")

    if fellow_id not in fellows:
        print("Fellow ID not found.")
        return

    resource_id = input("Enter resource ID: ")

    resource = None

    for item in resources:
        if item["id"] == resource_id:
            resource = item
            break

    if resource is None:
        print("Resource ID not found.")
        return

    try:
        quantity = int(input("Enter quantity to return: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    record = None

    for item in borrow_records:
        if item["fellow_id"] == fellow_id and item["resource_id"] == resource_id:
            record = item
            break

    if record is None:
        print("This fellow has no units of this resource on loan.")
        return

    if quantity > record["quantity"]:
        print("You cannot return more units than you borrowed.")
        return
    
    resource["available"] += quantity

    record["quantity"] -= quantity

    if record["quantity"] == 0:
        borrow_records.remove(record)

    print(f"{fellows[fellow_id]} returned {quantity} unit(s) of {resource['name']}.")



def search_resources():
    print("\n----- SEARCH RESOURCES -----")

    search_name = input("Enter resource name: ").strip().lower()

    found = False

    for resource in resources:
        if search_name in resource["name"].lower():
            print(f"ID: {resource['id']}")
            print(f"Name: {resource['name']}")
            print(f"Category: {resource['category']}")
            print(f"Available units: {resource['available']}")
            print("-" * 30)

            found = True

    if not found:
        print("No resources found.")


def filter_by_category():
    print("\n----- FILTER BY CATEGORY -----")

    category = input("Enter category: ").strip().lower()

    found = False

    for resource in resources:
        if resource["category"].lower() == category:
            print(f"ID: {resource['id']}")
            print(f"Name: {resource['name']}")
            print(f"Category: {resource['category']}")
            print(f"Available units: {resource['available']}")
            print("-" * 30)

            found = True

    if not found:
        print("No resources found in this category.")
def show_reports():
    print("\n--- RESOURCE REPORT ---")

    total_units = 0

    for resource in resources:
        total_units += resource["total"]

    available_units = 0

    for resource in resources:
        available_units += resource["available"]

    borrowed_units = total_units - available_units

    print(f"Total units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Currently borrowed: {borrowed_units}")

    print("\nLow-stock resources:")

    low_stock_found = False

    for resource in resources:
        if resource["available"] < 3:
            print(f"- {resource['name']} ({resource['available']} available)")
            low_stock_found = True

    if not low_stock_found:
        print("No low-stock resources.")

    print("\nMost borrowed resource(s):")

    max_borrowed = 0

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        if borrowed > max_borrowed:
            max_borrowed = borrowed

    if max_borrowed == 0:
        print("No resources are currently borrowed.")
    else:
        for resource in resources:
            borrowed = resource["total"] - resource["available"]

            if borrowed == max_borrowed:
                print(f"- {resource['name']} ({borrowed} borrowed)")

def main():
    while True:
        print("\n--- CAMPUS RESOURCE MANAGEMENT SYSTEM ---")
        print("1. Add resource")
        print("2. List resources")
        print("3. Borrow resource")
        print("4. Return resource")
        print("5. Search resources")
        print("6. Filter by category")
        print("7. Show reports")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_resource()

        elif choice == "2":
            list_resources()

        elif choice == "3":
            borrow_resource()

        elif choice == "4":
            return_resource()

        elif choice == "5":
            search_resources()

        elif choice == "6":
            filter_by_category()

        elif choice == "7":
            show_reports()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-8.")
if __name__ == "__main__":
    main()