# === Stage 5: Удаление и восстановление ===
# Project: CoffeeCupping
import uuid
from datetime import datetime


class Party:
    """Сущность «партия» с поддержкой мягкого удаления и восстановлением."""

    def __init__(self, name, country, roast, date=None):
        self.id = uuid.uuid4().hex
        self.name = name
        self.country = country
        self.roast = roast
        self.date = date or datetime.now().date().isoformat()
        self.deleted = False
        self.deleted_at = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "roast": self.roast,
            "date": self.date,
            "deleted": self.deleted,
            "deleted_at": self.deleted_at,
        }

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = datetime.now().isoformat()


class PartyStore:
    """Хранилище партий: добавление, получение, мягкое удаление и восстановление."""

    def __init__(self):
        self._items = {}

    def add(self, party):
        self._items[party.id] = party
        return party

    def get(self, party_id):
        party = self._items.get(party_id)
        return party if party and not party.deleted else None

    def soft_delete(self, party_id):
        party = self._items.get(party_id)
        if party:
            party.soft_delete()
        return party

    def restore(self, party_id):
        party = self._items.get(party_id)
        if party and party.deleted:
            party.deleted = False
            party.deleted_at = None
        return party

    def list_active(self):
        return [p for p in self._items.values() if not p.deleted]

    def list_deleted(self):
        return [p for p in self._items.values() if p.deleted]
