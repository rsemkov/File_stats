import re


def option_1_document_stats(file_content):
    def count_words_and_avg_word_len():
        words_pattern = r'\b\w+\b'

        # count words:
        words_only = re.findall(words_pattern, file_content)
        words_count = len(words_only)

        # average word length:
        total_word_chars_count = sum(len(word) for word in words_only)
        average_word_len = total_word_chars_count / words_count if words_count > 0 else 0

        return words_count, average_word_len

    def count_chars():
        file_content_cleaned = file_content.split()

        # count chars:
        chars_count_excluding_whitespaces = len(''.join(file_content_cleaned))
        chars_count_including_whitespaces = len(file_content)

        return chars_count_including_whitespaces, chars_count_excluding_whitespaces

    def count_sentences():
        # count sentences:
        sentences_count = len([x for x in file_content if x in [".", ";", ":", "...", "?", "!"]])

        return sentences_count

    count_words, avg_word_len = count_words_and_avg_word_len()
    chars_including, chars_excluding = count_chars()
    sent_count = count_sentences()

    return f"\nDOCUMENT STATS:" \
           f"\n-Total words in the file: {count_words}" \
           f"\n-Average word length: {avg_word_len:.1f} characters." \
           f"\n-Total characters in the file(INCLUDING white spaces, tabs and new lines: {chars_including}" \
           f"\n-Total characters in the file(EXCLUDING white spaces, tabs and new lines: {chars_excluding}" \
           f"\n-Total sentences in the file: {sent_count}"


def option_2_word_search(file_content, searched_word):
    coordinates_result = ""

    def word_occurrences_count():
        words_pattern = r'\b\w+\b'
        # find all words:
        words_only = re.findall(words_pattern, file_content)

        # count searched word occurrences:
        word_occurrences = sum([1 for word in words_only if word.lower() == searched_word.lower()])

        return word_occurrences

    def word_coordinates_search():
        coordinates = []
        data_matrix = []

        # SPLITS THE TEXT BY ROWS
        data = file_content.split('\n')

        # REMOVES WHITE SPACES, AND ALL CHARS WHICH ARE NOT ALPHABETIC(ONLY ACTUAL WORDS REMAIN), ADDS THEM TO MATRIX
        for current_row in data:
            current_row = ''.join(current_row).split()
            for index in range(len(current_row)):
                current_row[index] = "".join(x for x in current_row[index] if x.isalpha())
            data_matrix.append(current_row)

        # SEARCHES FOR THE WORD IN THE MATRIX AND ADDS ALL COORDINATES TO THE LIST, AS TUPLE
        for i, row in enumerate(data_matrix):
            for j, element in enumerate(row):
                if element.lower() == searched_word.lower():
                    coordinates.append((i, j))

        return coordinates

    word_count = word_occurrences_count()
    word_coordinates = word_coordinates_search()

    for r, c in word_coordinates:
        coordinates_result += f"\nRow: {r + 1}, Word number: {c + 1}"

    if word_count == 0:
        return f"\nThe word '{searched_word}' cannot be found in the document."
    else:
        return f"\nThe word '{searched_word}' can be found {word_count} time/s in the document." \
               f"\nIt can be found at the following coordinates:" \
               f"{coordinates_result}"


def options_display_menu():
    print("\nOptions Menu:")
    print("1. Documents stats")
    print("2. Search for word")
    print("3. Exit")


def main():
    file_path = input("Please, enter the file path: ")

    try:
        with open(file_path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

    while True:
        options_display_menu()

        option_selected = input("\nPlease, enter your choice from the menu: ")

        if option_selected == "1":
            print(option_1_document_stats(content))
            break
        elif option_selected == "2":
            word_searched = input("\nPlease, enter the word you would like to search for(case INSENSITIVE): ")
            print(option_2_word_search(content, word_searched))
            break
        elif option_selected == "3":
            print("\nThank you for using our service. Goodbye!")
            break
        else:
            print("\nPlease, select a valid option.")


if __name__ == "__main__":
    main()
