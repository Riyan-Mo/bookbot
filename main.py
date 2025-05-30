import sys
from stats import word_counter, get_book_text, character_counter, get_sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def main():
    content = get_book_text(path)
    number_of_words = word_counter(content)
    counter = character_counter(content)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    print(f"Found {number_of_words} total words")

    print("--------- Character Count -------")

    sorted_list = get_sorted_list(counter)

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print('============= END ===============')

main()
