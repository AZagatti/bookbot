from stats import get_num_words, get_number_of_characters, get_formatted_number_of_characters
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_name = sys.argv[1]
    try:
        book = get_book_text(book_name)
        num_words = get_num_words(book)
        count_dict = get_number_of_characters(book)
        formatted_dict = get_formatted_number_of_characters(count_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_name}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in formatted_dict:
            print(f"{item['name']}: {item['count']}")
        print("============= END ===============")
    except:
        print("Book not found")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

main()
