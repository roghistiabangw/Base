# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: MarketWatch
class SearchEngine:
    def __init__(self, data):
        self.data = data
    
    def search(self, query=None, fields=None, case_sensitive=False):
        if not fields:
            fields = ['name', 'shop_name']
        
        results = []
        for item in self.data:
            match = True
            for field in fields:
                value = item.get(field)
                search_value = query.lower() if not case_sensitive else query
                
                if value is None or (not case_sensitive and str(value).lower() != search_value):
                    match = False
                    break
            
            if match:
                results.append(item)
        
        return results
