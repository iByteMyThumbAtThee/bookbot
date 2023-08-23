def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #count_words(text)
    #print(text)
    count_letters(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
        file_contents = f.read()

def count_words(path):
    words = path.split()
    return len(words)

def count_letters(path):
    count_dict = {}
    for letter in path:
        letter = letter.lower()
        if letter.isalpha():
            if letter not in count_dict:
                count_dict[letter] = 0
            count_dict[letter] += 1
    count_list = list(count_dict)
    count_list.sort()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(path)} words found in the document")
    for item in count_list:
        print(f"The '{item}' character was found {count_dict[item]} times")
    print("--- End report ---")
    
        
main()