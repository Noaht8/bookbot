import sys
from stats import get_book_text, word_count, num_of_chars

def main(path):

    contents = get_book_text(path)
    d = num_of_chars(contents)
    sorted_scores = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    num_words = word_count(contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_scores:
        print(f"{c}: {sorted_scores[c]}")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
