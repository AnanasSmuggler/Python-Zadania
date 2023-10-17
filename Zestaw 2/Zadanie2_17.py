"""
ZADANIE 2.17
Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().
"""

import re

#Usuwa znaki interpunkcyjne z stringu
def remove_punctuation(string: str) -> str:
    return re.sub(r'[^\w\s]', '', string)

def sort_words_by_len(string: str) -> list:
    return sorted(remove_punctuation(string).split(), key=len)

def sort_words_alphabetically(string: str) -> list:
    return sorted(remove_punctuation(string).split())

def main() -> None:
    string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ante urna, suscipit in sapien sit amet, feugiat eleifend ante. Sed ac 
interdum leo. In risus ante, cursus sit amet ligula nec, pellentesque tempus nibh. Mauris ac congue mi, eget molestie leo. Morbi erat 
turpis, mollis et consequat et, placerat et justo. Maecenas luctus iaculis odio eu dignissim. Duis ex erat, egestas in augue cursus, semper 
mollis sapien. Maecenas a ullamcorper augue. Ut mollis eros in arcu aliquet convallis. Duis in feugiat sapien. Vivamus at libero nec eros aliquam lobortis."""

    print(f'Napis posortowany alfabetycznie: {sort_words_alphabetically(string)}\n')
    print(f'Napis posortowany długością rosnąco: {sort_words_by_len(string)}')

if __name__ == "__main__":
    main()