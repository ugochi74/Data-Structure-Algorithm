from data import resources, fellows, borrow_records
from resources import find_resource


def borrow_resource():
    print("\n----- BORROW RESOURCE -----")

    fellow_id = input("Enter fellow ID: ").strip()

    if fellow_id not in fellows:
        print("Fellow ID not found.")
        return False

    resource_id = input("Enter resource ID: ").strip()

    resource = find_resource(resource_id)

    if resource is None:
        print("Resource ID not found.")
        return False

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        return False

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return False

    if quantity > resource["available"]:
        print("Not enough units available.")
        return False

    resource["available"] -= quantity

    # Check if this fellow already has this resource
    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            record["quantity"] += quantity
            break
    else:
        borrow_records.append({
            "fellow_id": fellow_id,
            "resource_id": resource_id,
            "quantity": quantity
        })

    print(
        f"{fellows[fellow_id]} borrowed "
        f"{quantity} unit(s) of {resource['name']}."
    )

    return True


def return_resource():
    print("\n----- RETURN RESOURCE -----")

    fellow_id = input("Enter fellow ID: ").strip()

    if fellow_id not in fellows:
        print("Fellow ID not found.")
        return False

    resource_id = input("Enter resource ID: ").strip()

    resource = find_resource(resource_id)

    if resource is None:
        print("Resource ID not found.")
        return False

    try:
        quantity = int(input("Enter quantity to return: "))
    except ValueError:
        print("Please enter a valid number.")
        return False

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return False

    record = None

    for item in borrow_records:
        if (
            item["fellow_id"] == fellow_id
            and item["resource_id"] == resource_id
        ):
            record = item
            break

    if record is None:
        print("This fellow has no units of this resource on loan.")
        return False

    if quantity > record["quantity"]:
        print("You cannot return more than you borrowed.")
        return False

    resource["available"] += quantity
    record["quantity"] -= quantity

    if record["quantity"] == 0:
        borrow_records.remove(record)

    print(
        f"{fellows[fellow_id]} returned "
        f"{quantity} unit(s) of {resource['name']}."
    )

    return True