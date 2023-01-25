def count_words(file_contents) -> int:
    words = file_contents.split()
    word_count = len(words)
    return word_count


def count_letters(file_contents) -> dict:
    letters_dict = {}
    file_contents = file_contents.lower()
    for character in file_contents:
        if character in letters_dict:
            letters_dict[character] += 1
        else:
            letters_dict[character] = 1

    return letters_dict


def print_report(path_to_file, word_count, letter_count) -> None:
    sorted_letters = []
    for letter, count in letter_count.items():
        if letter.isalpha():
            sorted_letters.append({"letter": letter, "count": count})
    sorted_letters = sorted(sorted_letters, reverse=True, key=lambda d: d["count"])

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    for letter in sorted_letters:
        print(
            f"The character {letter.get('letter')} was found {letter.get('count')} times."
        )
    print("--- End report ---")


def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)

    print_report(path_to_file, word_count, letter_count)


if __name__ == "__main__":
    main()
