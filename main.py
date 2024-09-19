def add_vowels_to_set():
    digits_set = {'c', 'd'}
    vowels_set = {'a', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я'}
    result = digits_set.union(vowels_set)
    print("Множина після додавання голосних:", result)
add_vowels_to_set()
