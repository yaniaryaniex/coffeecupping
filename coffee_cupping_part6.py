# === Stage 6: Связанная сущность ===
# Project: CoffeeCupping
from datetime import date


class Cupping:
    def __init__(self, batch_id, taster, score, date=None):
        self.batch_id = batch_id
        self.taster = taster
        self.score = score
        self.date = date or date.today()

    def to_dict(self):
        return {
            'batch_id': self.batch_id,
            'taster': self.taster,
            'score': self.score,
            'date': self.date.isoformat() if isinstance(self.date, date) else str(self.date),
        }

    def __repr__(self):
        return (f'Cupping(batch_id={self.batch_id!r}, taster={self.taster!r}, '
                f'score={self.score}, date={self.date!r})')


def add_cupping(cupping_store, batch_id, taster, score, date=None):
    cupping = Cupping(batch_id, taster, score, date)
    cupping_store.append(cupping)
    return cupping


def find_by_batch(cupping_store, batch_id):
    return [c for c in cupping_store if c.batch_id == batch_id]


def find_by_taster(cupping_store, taster):
    return [c for c in cupping_store if c.taster == taster]


def average_score(cupping_store, batch_id):
    results = find_by_batch(cupping_store, batch_id)
    if not results:
        return None
    return sum(c.score for c in results) / len(results)
