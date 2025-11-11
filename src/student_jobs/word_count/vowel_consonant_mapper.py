import re
from src.core.job.mapper import Mapper

class VowelsConsonantsMapper(Mapper):
    def map(self, record, emit):
        vowels = "аеєиіїоуюяaeiou"
        record = str(record).lower()
        # Знаходимо слова, що складаються з літер і підкреслень
        words = re.findall(r'\b[\w]+\b', record)  # \w включає літери, цифри та _
        
        for word in words:
            length = len(word)  # довжина включно з підкресленнями
            # Рахуємо голосні та приголосні лише серед букв
            letters_only = re.sub(r'[^а-яєіїa-z]', '', word)
            v_count = sum(1 for c in letters_only if c in vowels)
            c_count = sum(1 for c in letters_only if c.isalpha() and c not in vowels)
            emit(length, (v_count, c_count))
