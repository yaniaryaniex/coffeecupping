# === Stage 8: Генерация идентификаторов ===
# Project: CoffeeCupping
import uuid
import datetime


def generate_id(prefix="cc"):
    """Генерация уникального идентификатора с префиксом проекта.

    Идентификатор формируется из случайного значения UUID4, приводимого к
    короткому виду, и префикса проекта. Возвращает строку вида
    'cc-<8 символов>'.
    """
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


class IdManager:
    """Управление генерацией и проверкой коллизий идентификаторов.

    Отслеживает сгенерированные идентификаторы в пределах одного экземпляра
    и гарантирует уникальность при добавлении.
    """

    def __init__(self, prefix="cc"):
        self.prefix = prefix
        self._used = set()

    def generate_unique(self):
        """Генерация идентификатора без коллизий.

    Повторяет логику функции generate_id, но при обнаружении коллизии
    автоматически увеличивает номер, пока не будет найдён свободный
    идентификатор."""
        candidate = generate_id(self.prefix)
        counter = 1
        while candidate in self._used:
            candidate = f"{self.prefix}-{uuid.uuid4().hex[:8]}-{counter}"
            counter += 1
        self._used.add(candidate)
        return candidate

    def is_available(self, candidate):
        """Проверка доступности идентификатора.

    Возвращает True, если идентификатор ещё не был сгенерирован этим
    экземпляром IdManager, иначе False."""
        return candidate not in self._used

    def used(self):
        """Возвращает множество всех сгенерированных идентификаторов."""
        return set(self._used)


if __name__ == "__main__":
    manager = IdManager()
    ids = [manager.generate_unique() for _ in range(5)]
    print(ids)
    print(manager.is_available(ids[0]))
    print(manager.is_available(manager.generate_unique()))
