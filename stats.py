def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lowercase_text = text.lower()
    char_count = {}

    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_chars(char_count):
    def sort_on(dict):
        return list(dict.values())[0]
    
    char_list = []

    for char, count in char_count.items():
       new_dict = {char: count}
       char_list.append(new_dict)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list