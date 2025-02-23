import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

from stats import get_num_words, get_char_count, sort_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    text = get_book_text(book_path)
    word_count = get_num_words(text)

    char_count = get_char_count(text)

    sorted_chars = sort_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")

    print("============= END ===============")

main()