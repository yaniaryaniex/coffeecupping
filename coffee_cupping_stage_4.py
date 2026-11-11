# === Stage 4: Редактирование записей ===
# Project: CoffeeCupping
def validate_party_update(data):
    """Проверяет, что переданные поля допустимы для партии.

    Допустимые поля: название, страна, обжарка, дата.
    Возвращает True, если все поля валидны, иначе выкидывает ValueError.
    """
    allowed_fields = {'название', 'страна', 'обжарка', 'дата'}

    unknown = set(data.keys()) - allowed_fields
    if unknown:
        raise ValueError(f'Недопустимые поля для партии: {sorted(unknown)}')

    if 'название' in data:
        value = data['название']
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Название партии должно быть непустой строкой')

    if 'страна' in data:
        value = data['страна']
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Страна должна быть непустой строкой')

    if 'обжарка' in data:
        value = data['обжарка']
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Обжарка должна быть непустой строкой')

    if 'дата' in data:
        value = data['дата']
        if not isinstance(value, str):
            raise ValueError('Дата должна быть строкой в формате ГГГГ-ММ-ДД')
        try:
            from datetime import date
            date.fromisoformat(value)
        except ValueError:
            raise ValueError(f'Неверный формат даты: {value!r}')

    return True


def update_party(party_id, **changes):
    """Редактирует партию по идентификатору.

    Применяет только допустимые поля к существующей партии.
    Возвращает обновлённую партию или None, если партии не существует.
    """
    parties = _load_parties()

    if party_id not in parties:
        return None

    target = parties[party_id]

    if validate_party_update(changes):
        for field, value in changes.items():
            setattr(target, field, value)
        _save_parties(parties)

    return target


def _load_parties():
    """Загружает партии из хранилища (заглушка для реального слоя)."""
    return _PARTIES


def _save_parties(parties):
    """Сохраняет партии в хранилище (заглушка для реального слоя)."""
    global _PARTIES
    _PARTIES = parties


_PARTIES = {}
