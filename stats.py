def count_of_words(book_text) -> int:
    list_of_words = book_text.split()
    return len(list_of_words)

def countofchar(book_text) -> dict:
    countofcharacters = {}
    for char in book_text.lower():
       count = countofcharacters.get(char, 0)
       countofcharacters[char] = count + 1
    return countofcharacters

def sort_on(dict):
    return dict["num"]
def sorteddicts(dictofcharacters):
    new_char_count_list  = []
    for k,v in dictofcharacters.items():
        char_count_dict = {"char": k , "num" : v}
        new_char_count_list.append(char_count_dict)
        new_char_count_list.sort(reverse=True, key = sort_on)
    for dictionary in new_char_count_list:
        character = dictionary['char']
        if character.isalpha():
            print(f"{dictionary['char']}: {dictionary['num']} \n")
        continue

