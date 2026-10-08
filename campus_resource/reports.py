from data import resources


def show_reports():
    print("\n===== RESOURCE REPORT =====")

    total_units = sum(
        resource["total"]
        for resource in resources
    )

    available_units = sum(
        resource["available"]
        for resource in resources
    )

    borrowed_units = total_units - available_units

    print(f"Total units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Currently borrowed: {borrowed_units}")

    print("\nLow-stock resources:")

    low_stock = [
        resource
        for resource in resources
        if resource["available"] < 3
    ]

    if low_stock:
        for resource in low_stock:
            print(
                f"- {resource['name']} "
                f"({resource['available']} available)"
            )
    else:
        print("No low-stock resources.")

    print("\nMost borrowed resource(s):")

    borrowed_amounts = [
        resource["total"] - resource["available"]
        for resource in resources
    ]

    max_borrowed = max(borrowed_amounts, default=0)

    if max_borrowed == 0:
        print("No resources are currently borrowed.")
        return

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        if borrowed == max_borrowed:
            print(
                f"- {resource['name']} "
                f"({borrowed} borrowed)"
            )








            