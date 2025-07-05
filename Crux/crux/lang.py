import json

class Lang:
    def __init__(self, default_lang='en'):
        self.translations = {}
        self.default_lang = default_lang

    def load_from_json(self, lang_code: str, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.translations[lang_code] = json.load(f)

    def get(self, key: str, lang_code: str = None, **kwargs):
        lang = lang_code if lang_code else self.default_lang
        
        # Try to get from the specified language
        text = self.translations.get(lang, {}).get(key)
        
        # Fallback to default language if not found
        if text is None:
            text = self.translations.get(self.default_lang, {}).get(key, key)
            
        return text.format(**kwargs)
