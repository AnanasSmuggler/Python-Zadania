"""

ZADANIE 3.8

Dla dwóch sekwencji liczb lub znaków znaleźć: 
(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), 
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń). 

Autor kodu: Jan Kaleta
"""

def get_simultaneous_characters(s1: set, s2: set) -> list:
    return list(s1.intersection(s2))

def get_all_characters(s1: set, s2: set) -> list:
    return list(s1.union(s2))

def main() -> None:
    input1 = set(input("Podaj pierwszy ciąg liczb lub znaków: "))
    input2 = set(input("Podaj drugi ciąg liczb lub znaków: "))

    print(f'Znaki występujące jednocześnie w obu ciągach: {get_simultaneous_characters(input1, input2)}')
    print(f'Wszystkie znaki występujące w obu ciągach: {get_all_characters(input1, input2)}')

if __name__ == "__main__":
    main()          