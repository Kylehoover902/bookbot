def main():
    book = "books/frankenstein.txt"
    book_text = get_book_text(book)
    print(book_text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
