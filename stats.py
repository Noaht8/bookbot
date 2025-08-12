def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def num_of_chars(s):
    d = {}
    for c in s.lower():
        if c.isalpha():
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    return d

def word_count(text):
    words = text.split()
    return len(words)
