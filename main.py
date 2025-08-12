from stats import get_book_text, word_count, num_of_chars

def main(relative_path):
    contents = get_book_text(relative_path)
    d = num_of_chars(contents)
    num_words = word_count(contents)
    print(f"{num_words} words found in the document")
    print(d)

main("/home/noah/workspace/bookbot/books/frankenstein.txt")
