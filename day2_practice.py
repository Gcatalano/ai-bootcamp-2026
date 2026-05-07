from __future__ import annotations


def totals_by_category(items: list[dict[str, object]]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for idx, item in enumerate(items):
        category = str(item.get("category", ""))
        amount_raw = item.get("amount", 0)
        try:
            amount = float(amount_raw)  # accepts int/float/numeric strings
        except (TypeError, ValueError) as e:
            print(
                f"Skipping item #{idx} ({item!r}): "
                f"amount {amount_raw!r} is invalid ({e.__class__.__name__})."
            )
            continue

        totals[category] = totals.get(category, 0.0) + amount
    return totals


def main() -> None:
    sample_data = [
        {"name": "Coffee", "category": "Food", "amount": 4.50},
        {"name": "Sandwich", "category": "Food", "amount": 8},
        {"name": "Bus pass", "category": "Transport", "amount": 25},
        {"name": "Movie", "category": "Entertainment", "amount": "12.99"},
        {"name": "Invalid", "category": "Food", "amount": "not a number"},
    ]

    summary = totals_by_category(sample_data)
    print(summary)


if __name__ == "__main__":
    main()
