def main():
    book = "books/frankenstein.txt"
    book_text = get_book_text(book)
    from stats import get_word_count
    print(f"{get_word_count(book_text)} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
