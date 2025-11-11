import re
from src.core.job.mapper import Mapper

class WordCountMapper(Mapper):
    def map(self, record, emit):
        # Перетворюємо рядок на нижній регістр
        text = str(record).lower()
        # Знаходимо всі слова (літери та цифри), ігноруючи розділові знаки
        words = re.findall(r'\b\w+\b', text)
        for word in words:
            emit(word, 1)
