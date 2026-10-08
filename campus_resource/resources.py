from data import resources


def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource

    return None


def add_resource():
    print("\n----- ADD RESOURCE -----")

    resource_id = input("Enter resource ID: ").strip()

    if find_resource(resource_id) is not None:
        print("Resource ID already exists.")
        return False

    name = input("Enter resource name: ").strip()
    category = input("Enter category: ").strip()

    try:
        total = int(input("Enter total units: "))
    except ValueError:
        print("Please enter a valid number.")
        return False

    if total <= 0:
        print("Total units must be greater than zero.")
        return False

    resources.append({
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    })

    print("Resource added successfully.")
    return True


def list_resources():
    print("\n----- RESOURCE INVENTORY -----")

    if not resources:
        print("No resources available.")
        return

    for resource in resources:
        print(f"\nID: {resource['id']}")
        print(f"Name: {resource['name']}")
        print(f"Category: {resource['category']}")
        print(f"Total units: {resource['total']}")
        print(f"Available units: {resource['available']}")
        print("-" * 30)