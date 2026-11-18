# === Stage 7: Связи между сущностями ===
# Project: CoffeeCupping
def get_cupping_notes_for_batch(batch, db):
    """
    Возвращает список оценок для всех дегустаций указанной партии,
    проверяя целостность связи.
    """
    result = []
    for cupping_id, cupping_name, batch_id in db.query(
        "SELECT cupping_id, cupping_name, batch_id "
        "FROM cupping "
        "WHERE batch_id = ?",
        (batch["batch_id"],)
    ):
        if batch["batch_id"] != cupping["batch_id"]:
            print(f"Ошибка: несостоятельная ссылка batch_id")
        result.append({"cupping_id": cupping_id, "cupping_name": cupping_name})
    return result
