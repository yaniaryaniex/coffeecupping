# === Stage 9: Фильтрация записей ===
# Project: CoffeeCupping
from datetime import date


def filter_batches_by_country(batches, country):
    return [b for b in batches if b.get("country") == country]


def filter_batches_by_date_range(batches, start, end):
    return [b for b in batches if start <= b.get("roast_date") <= end]


def filter_batches(batches, country=None, start=None, end=None):
    result = batches

    if country is not None:
        result = filter_batches_by_country(result, country)

    if start is not None:
        result = filter_batches_by_date_range(result, start, date.max)

    if end is not None:
        result = filter_batches_by_date_range(result, date.min, end)

    return result


def filter_batches_by_country_and_date(batches, country, start, end):
    result = filter_batches_by_country(batches, country)
    result = filter_batches_by_date_range(result, start, end)
    return result
