from stats import count_of_words , sorteddicts, countofchar
import sys
def get_book_text(bookpath) -> str :
  with open(bookpath) as f:
    book_text = f.read()
    return book_text


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    path_to_book = sys.argv[1]
    book_txt = get_book_text(f"{path_to_book}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_of_words(book_txt)} total words")
    print("--------- Character Count -------")
    print(sorteddicts(countofchar(book_txt)))
    print("============= END ===============")


main()
