from data import resources


def search_resources():
    print("\n----- SEARCH RESOURCES -----")

    search_text = input("Enter resource name: ").strip().lower()

    found = False

    for resource in resources:
        if search_text in resource["name"].lower():
            print(f"\nID: {resource['id']}")
            print(f"Name: {resource['name']}")
            print(f"Category: {resource['category']}")
            print(f"Available: {resource['available']}")

            found = True

    if not found:
        print("No resources found.")


def filter_by_category():
    print("\n----- FILTER BY CATEGORY -----")

    category = input("Enter category: ").strip().lower()

    found = False

    for resource in resources:
        if resource["category"].lower() == category:
            print(f"\nID: {resource['id']}")
            print(f"Name: {resource['name']}")
            print(f"Category: {resource['category']}")
            print(f"Available: {resource['available']}")

            found = True

    if not found:
        print("No resources found in this category.")