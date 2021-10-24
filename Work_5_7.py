def key_word_dict():
    first_str = input("Введите первый список слов через запятую: ")
    first_list = first_str.split(',')
    print("Количество слов в первом списке:",
          first_str.count(" ") + 1)

    second_str = input(f"Введите второй список из "
                       f"{first_str.count(' ') + 1} "
                       f"слов через запятую: ")
    second_list = second_str.split(',')

    dictionary_double = dict(zip(first_list, second_list))
    print(dictionary_double)

    with open('dictionary.txt', 'w', encoding='utf-8') as f:
        for key, val in dictionary_double.items():
            f.write(f'{key}:{val}\n')
    return 0

key_word_dict()