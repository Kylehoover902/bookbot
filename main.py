from stats import get_word_count
from stats import sorted_character_count
import sys
if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book = sys.argv[1]
    book_text = get_book_text(book)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    for char in sorted_character_count(book_text):
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
