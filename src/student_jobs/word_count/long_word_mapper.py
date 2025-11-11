import re
from src.core.job.mapper import Mapper

class WordCountLongMapper(Mapper):
    def map(self, record, emit):
        # Розділяємо текст на слова, прибираючи розділові знаки
        words = re.findall(r'\b\w+\b', str(record).lower())
        for word in words:
            if len(word) > 5:  # тільки слова довші 5 символів
                emit(word, 1)
