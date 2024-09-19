def add_vowels_to_set():
    digits_set = {'c', 'd'}
    vowels_set = {'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я'}
    result = digits_set.union(vowels_set)
    if isinstance(result, set):
        print("Множина після додавання голосних:", result)
    else:
        result_list = list(digits_set) + list(vowels_set)
        print("Перетворено на список і знову на множину:", set(result_list))

add_vowels_to_set()
