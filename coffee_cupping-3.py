# === Stage 3: Хранилище в памяти ===
# Project: CoffeeCupping
import threading


class PartyStore:
    """Хранилище партий кофе в памяти.

    Хранит партии по их идентификаторам и предоставляет доступ
    к ним через ключ, а также итерацию по всем записанным партиям.
    """

    def __init__(self):
        self._data = {}
        self._counter = 0
        self._lock = threading.Lock()

    def add_party(self, name, country, roast, date):
        with self._lock:
            self._counter += 1
            party_id = self._counter
            self._data[party_id] = {
                "id": party_id,
                "name": name,
                "country": country,
                "roast": roast,
                "date": date,
            }
        return party_id

    def get_party(self, party_id):
        return self._data.get(party_id)

    def list_parties(self):
        return list(self._data.values())


class Party:
    """Сущность партия кофе."""

    def __init__(self, name, country, roast, date):
        self.name = name
        self.country = country
        self.roast = roast
        self.date = date

    def __repr__(self):
        return (
            f"Party(id={self._id}, name={self.name!r}, "
            f"country={self.country!r}, roast={self.roast!r}, "
            f"date={self.date!r})"
        )


class PartyModel(Party):
    """Партия с привязкой к идентификатору хранилища."""

    def __init__(self, name, country, roast, date):
        self._id = None
        super().__init__(name, country, roast, date)

    def bind(self, store, party_id):
        self._id = party_id
        return self

    def __eq__(self, other):
        if not isinstance(other, PartyModel):
            return NotImplemented
        return (
            self._id == other._id
            and self.name == other.name
            and self.country == other.country
            and self.roast == other.roast
            and self.date == other.date
        )


def main():
    store = PartyStore()
    p1 = PartyModel("Ethiopia", "Ethiopia", "Medium", "2024-05-01").bind(store, 1)
    p2 = PartyModel("Colombia", "Colombia", "Dark", "2024-06-15").bind(store, 2)
    print(store.get_party(1))
    print(store.list_parties())


if __name__ == "__main__":
    main()
