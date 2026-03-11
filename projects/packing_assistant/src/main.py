from knapsack import knapsack

# Airline cabin baggage limit (grams)
CABIN_LIMIT_G = 10_000

# (name, weight_g, value)
# Value represents how useful/important the item is for a typical trip
ITEMS = [
    ("Laptop",             1800, 95),
    ("Phone charger",       200, 80),
    ("Laptop charger",      400, 75),
    ("Headphones",          300, 60),
    ("Change of clothes",   800, 55),
    ("Toiletry bag",        600, 50),
    ("Book",                400, 30),
    ("Neck pillow",         350, 25),
    ("Snacks",              500, 40),
    ("Water bottle",        300, 35),
    ("Umbrella",            400, 20),
    ("Extra shoes",        1000, 15),
    ("Jacket",              900, 45),
    ("Tablet",              700, 50),
    ("Notebook + pen",      200, 20),
]


def print_table(items):
    print(f"  {'Item':<22} {'Weight':>8}  {'Value':>6}")
    print("  " + "-" * 42)
    for name, weight, value in items:
        print(f"  {name:<22} {weight/1000:>6.2f}kg  {value:>6}")


def main():
    print("=" * 50)
    print("  Airport Packing Assistant")
    print(f"  Cabin baggage limit: {CABIN_LIMIT_G / 1000:.1f} kg")
    print("=" * 50)

    print("\nAll available items:")
    print_table(ITEMS)

    total_value, selected = knapsack(ITEMS, CABIN_LIMIT_G)
    total_weight = sum(w for _, w, _ in selected)

    print(f"\nOptimal selection ({total_weight / 1000:.2f} kg / {CABIN_LIMIT_G / 1000:.1f} kg):")
    print_table(selected)
    print(f"\n  Total value score: {total_value}")

    leftout = [item for item in ITEMS if item not in selected]
    if leftout:
        print("\nLeft behind:")
        for name, weight, _ in leftout:
            print(f"  - {name} ({weight / 1000:.2f} kg)")


if __name__ == "__main__":
    main()
