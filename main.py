def count_words(the_content):
    words = the_content.split()
    for index in range(len(words)):
        words[index] = "".join(x for x in words[index] if x.isalpha())

    cleaned_words = list(filter(None, words))

    word_count = len(cleaned_words)
    total_chars = sum([len(x) for x in words])
    avg_word_len = total_chars / word_count

    print(f"Total words in the file: {word_count}")
    print(f"Total characters in the file: {len([x for x in the_content if x != ' '])}")
    print(f"The average word length is {avg_word_len:.2f} characters.")


def find_word(the_word, the_content):
    words = the_content.split()
    for index in range(len(words)):
        words[index] = "".join(x for x in words[index] if x.isalpha())

    word_occurrences_count = len([x for x in words if x.lower() == the_word.lower()])

    print(f"The word '{the_word}' appears {word_occurrences_count} time/s in the document.")


def find_word_coordinates(the_content, the_word):
    coordinates = []
    data_matrix = []

    # SPLITS THE TEXT BY ROWS
    data = the_content.split('\n')

    # REMOVES WHITE SPACES, REMOVES ALL CHARS WHICH ARE NOT ALPHABETIC(ONLY ACTUAL WORDS REMAIN), ADDS THEM TO MATRIX
    for current_row in data:
        current_row = ''.join(current_row).split()
        for index in range(len(current_row)):
            current_row[index] = "".join(x for x in current_row[index] if x.isalpha())
        data_matrix.append(current_row)

    # SEARCHES FOR THE WORD IN THE MATRIX AND ADDS ALL COORDINATES TO THE LIST, AS TUPLE
    for i, row in enumerate(data_matrix):
        for j, element in enumerate(row):
            if element.lower() == the_word.lower():
                coordinates.append((i, j))

    if coordinates:
        print(f"The word '{the_word}' can be found at the following "
              f"coordinates(row/column) in the document: {coordinates}.")


def main():
    file_path = input("Please, enter the file path: ")

    try:
        with open(file_path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

    count_words(content)

    word_searched = input("\nIf you want to search for a word, "
                          "please enter it(case INSENSITIVE). Otherwise, enter 'N': ")

    if word_searched.upper() != "N":
        find_word(word_searched, content)
        find_word_coordinates(content, word_searched)
    else:
        print("Thank you for using our services. Goodbye.")


main()
