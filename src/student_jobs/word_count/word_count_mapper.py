import re
from src.core.job.mapper import Mapper

class WordCountMapper(Mapper):
    def map(self, record, emit):
        text = str(record).lower()        
        words = text.split()
        for word in words:
            clean_word = word.strip('.,!?;:"()[]{}')
            if clean_word and not clean_word.isdigit():
                emit(clean_word, 1)
