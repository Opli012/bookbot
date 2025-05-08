from collections import Counter

text_file = "books/frankenstein.txt"
chars_dict = {}

def get_num_words():
    text = get_book_text(text_file)
    num_words = len(text.split())
    return num_words

def print_header():
    num_words = get_num_words()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

def print_footer():
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read().lower()
    return file_contents

def char_dict():
    letters_only = [ch for ch in get_book_text(text_file) if ch.isalpha()]
    char_counts = Counter(letters_only)
    for ch, count in sorted(char_counts.items()):
        chars_dict[ch] = count
    return chars_dict

def sort_dict():
    chars_dict = char_dict()
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict