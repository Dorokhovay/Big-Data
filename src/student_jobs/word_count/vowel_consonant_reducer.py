from src.core.job.reducer import Reducer

class VowelsConsonantsReducer(Reducer):
    def reduce(self, key, values, emit):
        total_vowels = 0
        total_consonants = 0

        for v, c in values:
            total_vowels += v
            total_consonants += c

        total_letters = total_vowels + total_consonants
        if total_letters == 0:
            vowel_percent = consonant_percent = 0
        else:
            vowel_percent = (total_vowels / total_letters) * 100
            consonant_percent = (total_consonants / total_letters) * 100

        emit(key, f"{vowel_percent:.1f}% голосних, {consonant_percent:.1f}% приголосних")
