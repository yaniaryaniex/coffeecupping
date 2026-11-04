# === Stage 2: Проверка полей ===
# Project: CoffeeCupping
module = "coffee_cupping"


def normalize_string(value: str) -> str:
    text = (value or "").strip()
    if not text:
        raise ValueError("Поле не может быть пустым")
    return text


def normalize_country(value: str) -> str:
    text = normalize_string(value)
    return text.capitalize()


def normalize_roast(value: str) -> str:
    text = normalize_string(value)
    return text.lower()


def normalize_roast_level(value: str) -> str:
    levels = {"light": "Светлая", "medium": "Средняя", "dark": "Тёмная"}
    normalized = normalize_roast(value)
    if normalized not in levels:
        valid = ", ".join(levels.keys())
        raise ValueError(f"Неверный уровень обжарки. Допустимые значения: {valid}")
    return levels[normalized]


def normalize_date(value: str) -> str:
    text = normalize_string(value)
    for format_code in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m.%d.%Y"):
        try:
            return datetime.strptime(text, format_code).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Неверный формат даты. Пример: 2024-05-17")


def validate_party(name: str, country: str, roast: str, roast_level: str, date: str) -> None:
    if not name:
        raise ValueError("Название партии не может быть пустым")
    if not country:
        raise ValueError("Укажите страну происхождения партии")
    if not roast:
        raise ValueError("Укажите уровень обжарки партии")
    if not date:
        raise ValueError("Укажите дату обжарки партии")
    validate_roast_level(roast_level)
    validate_date_format(date)


def validate_roast_level(roast_level: str) -> None:
    levels = {"Светлая", "Средняя", "Тёмная"}
    if roast_level not in levels:
        valid = ", ".join(sorted(levels))
        raise ValueError(f"Неверный уровень обжарки. Допустимые значения: {valid}")


def validate_date_format(date: str) -> None:
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Неверный формат даты '{date}'. Ожидается формат ГГГГ-ММ-ДД")


def create_party(name: str, country: str, roast: str, roast_level: str, date: str) -> dict:
    validate_party(name, country, roast, roast_level, date)
    return {
        "name": normalize_string(name),
        "country": normalize_country(country),
        "roast": normalize_roast(roast),
        "roast_level": normalize_roast_level(roast_level),
        "roast_date": normalize_date(date),
    }
