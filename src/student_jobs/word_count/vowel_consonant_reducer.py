from src.core.job.reducer import Reducer

class VowelsConsonantsReducer(Reducer):
    def reduce(self, key, values, emit):
        total_vowels = 0
        total_consonants = 0
        
        for v, c in values:
            total_vowels += v
            total_consonants += c
        
        total_letters = total_vowels + total_consonants        
        if total_letters > 0:
            vowel_percent = (total_vowels * 100) / total_letters
            consonant_percent = (total_consonants * 100) / total_letters
        else:
            vowel_percent = 0
            consonant_percent = 0
        
        result = str(vowel_percent) + "% голосних, " + str(consonant_percent) + "% приголосних"
        emit(key, result)