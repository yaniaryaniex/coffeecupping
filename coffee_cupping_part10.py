# === Stage 10: Сортировка записей ===
# Project: CoffeeCupping
import datetime


def sort_by_name(records, descending=False):
    return sorted(records, key=lambda r: r["name"], reverse=descending)


def sort_by_date(records, descending=False):
    return sorted(
        records,
        key=lambda r: r["created_at"],
        reverse=descending,
    )


def sort_records(records, field=None, descending=False):
    if field == "name":
        return sort_by_name(records, descending=descending)
    if field == "created_at":
        return sort_by_date(records, descending=descending)
    raise ValueError(f"Неизвестное поле для сортировки: {field!r}")


def get_records():
    path = "coffee_cupping партии.json"
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_records(records):
    path = "coffee_cupping партии.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    import os
    import json

    records = get_records()
    if not records:
        print("Нет записей для сортировки.")
    else:
        sorted_by_name = sort_records(records, field="name", descending=False)
        print("По названию (по возрастанию):")
        for r in sorted_by_name:
            print(f'  {r["name"]}')

        sorted_by_date = sort_records(records, field="created_at", descending=True)
        print("По дате создания (по убыванию):")
        for r in sorted_by_date:
            print(f'  {r["created_at"]}')

        save_records(sorted_by_date)
        print("Сортировка сохранена.")
