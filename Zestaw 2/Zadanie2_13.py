"""
ZADANIE 2.13
Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum()

Autor kodu: Jan Kaleta
"""
import re

#Usuwa znaki interpunkcyjne z stringu
def remove_punctuation(string: str) -> str:
    return re.sub(r'[^\w\s]', '', string)

def count_word_length(string: str) -> int:
    return len(string)

def count_all_words_length(string: str) -> int:
    words = remove_punctuation(string).split()
    words_lengths = [count_word_length(i) for i in words]
    return sum(words_lengths)

def main() -> None:
    string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ante urna, suscipit in sapien sit amet, feugiat eleifend ante. Sed ac 
interdum leo. In risus ante, cursus sit amet ligula nec, pellentesque tempus nibh. Mauris ac congue mi, eget molestie leo. Morbi erat 
turpis, mollis et consequat et, placerat et justo. Maecenas luctus iaculis odio eu dignissim. Duis ex erat, egestas in augue cursus, semper 
mollis sapien. Maecenas a ullamcorper augue. Ut mollis eros in arcu aliquet convallis. Duis in feugiat sapien. Vivamus at libero nec eros aliquam lobortis."""

    print(f'Długość wszystkich słów w stringu wynosi: {count_all_words_length(string)}')

if __name__ == "__main__":
    main()