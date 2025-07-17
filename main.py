def main():
    book = "books/frankenstein.txt"
    book_text = get_book_text(book)
    
    from stats import get_word_count
    from stats import get_character_count
    print(f"{get_word_count(book_text)} words found in the document")
    # print(get_character_count(book_text))
    test = {}
    print(get_character_count(book_text))


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
