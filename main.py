import sys
from stats import count_characters, count_words, sort_characters


def get_books_text(filepath):
    with open(filepath) as f:
        book_text = f.read()

    return book_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_books_text(book_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_characters(character_count)

    print(f"{'=' * 12} BOOKBOT {'=' * 12}")
    print(f"Analysing book found at {book_path}...")
    print(f"{'-' * 12} Word Count {'-' * 12}")
    print(f"Found {word_count} total words")
    print(f"{'-' * 12} Character Count {'-' * 12}")
    for char in sorted_characters:
        if not char.get("character").isalpha():
            continue

        print(f"{char.get('character')}: {char.get('count')}")

    print(f"{'=' * 12} END {'=' * 12}")


if __name__ == "__main__":
    main()
