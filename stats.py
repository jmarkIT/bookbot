def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count.keys():
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count


def sort_characters(characters: dict[str, int]) -> list[dict]:
    sorted_characters = []
    for char, count in characters.items():
        sorted_characters.append({"character": char, "count": count})

    def sort_on(dict: dict):
        return dict["count"]

    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
