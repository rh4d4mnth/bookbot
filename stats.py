# takes the filepath as input and return the contents of the file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# counts the number of words in a string
def get_word_count(path_to_file):
    num_words = len(get_book_text(path_to_file).split())
    return f"{num_words} words found in the document"

# counts the number of each characters in a string
def get_num_char(path_to_file):
    file_dictionary = {}
    lower_file_contents = get_book_text(path_to_file).lower()
    character_list = list(lower_file_contents)
    for i in character_list:
        if i in file_dictionary:
            file_dictionary[i] += 1
        else:
            file_dictionary[i] = 1
    return file_dictionary

