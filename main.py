from stats import get_num_words
from stats import get_character_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = './books/frankenstein.txt'
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    print(f"{num_words} words found in the document")
    character_counts = get_character_counts(contents)
    for c in character_counts:
        print(f"'{c}': {character_counts[c]}")

main()
