def get_word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count