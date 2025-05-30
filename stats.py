def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def word_counter(text):
    return len(text.split())

def character_counter(text):
    char_dict = {}
    text_list = text.split()
    for word in text_list:
        for alphabet in word:
            lower_cased_alphabet = alphabet.lower()
            if lower_cased_alphabet in char_dict:
                char_dict[lower_cased_alphabet] += 1
            else:
                char_dict[lower_cased_alphabet] = 1
    return char_dict

def get_sorted_list(char_dict):
    char_list = []
    for char in char_dict:
        new_dict = {
            "char": char,
            "num": char_dict[char]
        }
        char_list.append(new_dict)
    char_list.sort(key=lambda character: character["num"], reverse=True)
    return char_list