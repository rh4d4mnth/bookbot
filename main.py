from stats import get_word_count
from stats import get_num_char
from stats import get_sorted_dicts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    sorted_dict = get_sorted_dicts(get_num_char(filepath))
    # prints the formated report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(filepath)} total words")
    print("--------- Character Count -------")
    for i in sorted_dict:
        if str(i["char"]).isalpha():
            print(str(i["char"]) + ": " + str(i["num"]))
    print("============= END ===============")

main()

