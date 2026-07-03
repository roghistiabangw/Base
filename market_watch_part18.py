# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: MarketWatch
class TagManager:
    def __init__(self, db):
        self.db = db
        self.tags_db = db.get_collection("tags")
    
    def add_tag(self, name):
        if not name.strip(): return False
        existing = self.tags_db.find_one({"name": {"$regex": "^" + re.escape(name) + "$", "$options": "i"}})
        if existing: return True
        result = self.tags_db.insert_one({"name": name, "created_at": datetime.now()})
        return result.inserted_id
    
    def remove_tag(self, tag_name):
        count = self.tags_db.delete_many({"name": {"$regex": "^" + re.escape(tag_name) + "$", "$options": "i"}}).deleted_count
        if count > 0:
            for doc in self.db.watch.find({}):
                tags_to_remove = [t["tag"] for t in doc.get("tags", []) if t["tag"].lower() == tag_name.lower()]
                if tags_to_remove:
                    self.db.watch.update_one({"_id": doc["_id"]}, {"$pull": {"tags": {"$in": tags_to_remove}}})
        return count
