"""
ZADANIE 2.14
Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
"""
import re

#Usuwa znaki interpunkcyjne z stringu
def remove_punctuation(string: str) -> str:
    return re.sub(r'[^\w\s]', '', string)

def max_len_word_in_string(string: str) -> tuple[str, int]:
    words_sorted = sorted(remove_punctuation(string).split(), key=len)

    return [words_sorted[-1], len(words_sorted[-1])]

def main() -> None:
    string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ante urna, suscipit in sapien sit amet, feugiat eleifend ante. Sed ac 
interdum leo. In risus ante, cursus sit amet ligula nec, pellentesque tempus nibh. Mauris ac congue mi, eget molestie leo. Morbi erat 
turpis, mollis et consequat et, placerat et justo. Maecenas luctus iaculis odio eu dignissim. Duis ex erat, egestas in augue cursus, semper 
mollis sapien. Maecenas a ullamcorper augue. Ut mollis eros in arcu aliquet convallis. Duis in feugiat sapien. Vivamus at libero nec eros aliquam lobortis."""

    print(f'[Najdłuższe słowo, Jego długość]: {max_len_word_in_string(string)}')

if __name__ == "__main__":
    main()