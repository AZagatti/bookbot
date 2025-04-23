def get_num_words(text_book):
    return len(text_book.split())

def get_number_of_characters(text_book):
    count_dict = {}
    for char in text_book:
        lower_char = char.lower()
        if lower_char in count_dict:
            count_dict[lower_char] += 1
        else:
            count_dict[lower_char] = 1
    return count_dict

def get_formatted_number_of_characters(char_dict):
    result = []
    for char, count in char_dict.items():
        if char.isalpha():
            result.append({ "name": char, "count": count })
    result.sort(reverse=True, key=lambda x: x["count"])
    return result
