import re
from src.core.job.mapper import Mapper

class WordCountLongMapper(Mapper):
    def map(self, record, emit):
        text = str(record).lower()
        words = text.split()
        for word in words:
            word = word.strip('.,!?;:"()[]{}')            
            if len(word) > 5:
                emit(word, 1)
