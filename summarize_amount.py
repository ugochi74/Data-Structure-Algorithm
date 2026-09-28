def summarise_amounts(raw_values):
    total = 0
    rejected_count = 0
    for raw in raw_values:
            try:
                # Using float handles both decimals and whole numbers safely
                amount = int(raw)
                if amount < 0:
                    rejected_count += 1
                else:
                    total += amount
            except ValueError:
                rejected_count += 1
    return {"total": total, "rejected": rejected_count}

print(summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""]))

assert summarise_amounts(["10", "5", "bad", "-3" "0", ""]) == {
    "total": 15,
    "rejected": 3
}


assert summarise_amounts([]) == {
    "total": 0,
    "rejected": 0
}

assert summarise_amounts(["0"]) == {
    "total": 0,
    "rejected": 0
}
