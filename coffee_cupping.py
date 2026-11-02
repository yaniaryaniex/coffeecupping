# === Stage 1: Каркас модуля ===
# Project: CoffeeCupping
from datetime import date
from typing import List


class Roast:
    LIGHT = "light"
    MEDIUM = "medium"
    MEDIUM_DARK = "medium_dark"
    DARK = "dark"


class CoffeeBatch:
    def __init__(self, name: str, country: str, roast: str, roast_date: date):
        self.name = name
        self.country = country
        self.roast = roast
        self.roast_date = roast_date

    def __repr__(self):
        return (
            f"CoffeeBatch(name={self.name!r}, country={self.country!r}, "
            f"roast={self.roast!r}, roast_date={self.roast_date!r})"
        )


def create_demo_batches() -> List[CoffeeBatch]:
    return [
        CoffeeBatch("Ethiopia Yirgacheffe", "Ethiopia", Roast.LIGHT, date(2024, 3, 15)),
        CoffeeBatch("Colombia Huila", "Colombia", Roast.MEDIUM, date(2024, 4, 2)),
        CoffeeBatch("Sumatra Mandheling", "Indonesia", Roast.DARK, date(2024, 4, 20)),
        CoffeeBatch("Kenya AA", "Kenya", Roast.MEDIUM_DARK, date(2024, 5, 10)),
    ]


def main() -> None:
    batches = create_demo_batches()
    print("CoffeeCupping - дегустации кофе")
    print("=" * 30)
    for batch in batches:
        print(batch)
    print(f"Всего партий: {len(batches)}")


if __name__ == "__main__":
    main()
