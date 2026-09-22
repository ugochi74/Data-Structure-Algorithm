def summarise_amounts(raw_values):
    total = 0
    rejected_count = 0
    for raw in raw_values:
        try:
            # Using float handles both decimals and whole numbers safely
            total += float(raw)
        except ValueError:
            rejected_count += 1
    return {"total": total, "rejected": rejected_count}
