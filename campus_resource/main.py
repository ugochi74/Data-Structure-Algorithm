from resources import add_resource, list_resources
from borrowing import borrow_resource, return_resource
from search import search_resources, filter_by_category
from reports import show_reports


def show_menu():
    print("\n======================================")
    print(" CAMPUS RESOURCE MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Add resource")
    print("2. List resources")
    print("3. Borrow resource")
    print("4. Return resource")
    print("5. Search resources")
    print("6. Filter by category")
    print("7. Show reports")
    print("8. Exit")


def main():
    while True:
        show_menu()

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
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()