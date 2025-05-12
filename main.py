from stats import get_word_count
from stats import get_num_char

def main():
    filepath = "books/frankenstein.txt"
    print(get_word_count(filepath))
    print(get_num_char(filepath))

main()

