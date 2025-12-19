import re
from src.core.job.mapper import Mapper

class VowelsConsonantsMapper(Mapper):
    def map(self, record, emit):
        vowels = "аеєиіїоуюяaeiou"
        text = str(record).lower()
        words = text.split()
        
        for word in words:
            clean_word = word.strip('.,!?;:"()[]{}')            
            if not clean_word:
                continue            
            letters = ""
            for char in clean_word:
                if char.isalpha():
                    letters += char
            if not letters:
                continue
            vowel_count = 0
            for char in letters:
                if char in vowels:
                    vowel_count += 1
            
            consonant_count = len(letters) - vowel_count
            
            emit(len(clean_word), (vowel_count, consonant_count))
