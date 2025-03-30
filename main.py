from stats import get_num_words
from stats import get_character_counts
from stats import get_sorted_character_counts 
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # check to make sure they specified the book to process
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {filepath}...")

    contents = get_book_text(filepath)
    num_words = get_num_words(contents)


    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    character_counts = get_character_counts(contents)
    sorted_character_counts = get_sorted_character_counts(character_counts)

    print("--------- Character Count -------")
    for count in sorted_character_counts:
        c = next(iter(count))
        if c.isalpha():
            print(f"{next(iter(count))}: {count[next(iter(count))]}")

main()
