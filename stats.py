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