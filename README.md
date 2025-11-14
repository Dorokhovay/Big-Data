Task 1 command:
python -m src.cli.main run --workers 2 --reducers 2 --input data/input --output data/output/wordcount --job src.student_jobs.word_count.word_count_mapper:WordCountMapper,src.student_jobs.word_count.reducer:WordCountReducer

Task 2 command:
python -m src.cli.main run --workers 2 --reducers 2 --input data/input --output data/output/wordcount --job src.student_jobs.word_count.long_word_mapper:WordCountLongMapper,src.student_jobs.word_count.reducer:WordCountReducer

Task 3 command:
python -m src.cli.main run --workers 2 --reducers 2 --input data/input --output data/output/wordcount --job src.student_jobs.word_count.vowel_consonant_mapper:VowelsConsonantsMapper,src.student_jobs.word_count.vowel_consonant_reducer:VowelsConsonantsReducer
