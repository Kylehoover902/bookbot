def get_word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def get_character_count(text):
    text = text.lower()
    characters = {}
    char_list = list(text)
    for char in char_list:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_character_count(text):
    sorted_char = []
    characters = get_character_count(text)
    for i in characters:
        if i.isalpha() == True:
            char, count = i, characters[i]
            tmp_dir = {"char":char, "num":count}
            sorted_char.append(tmp_dir)
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char

