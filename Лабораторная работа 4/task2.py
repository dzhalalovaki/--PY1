def get_count_char(str_):
    str_ = str_.lower()

    sentence_letters = {}

    for i in str_:
        if i.isalpha():
            if i in sentence_letters:
                sentence_letters[i] += 1
            else:
                sentence_letters[i] = 1

    return sentence_letters

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
