"""
ZADANIE 2.18
Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.
"""
import re

def count_zeros_in_int(integer: int) -> int:
    string = str(integer)
    return len(re.sub(r'[1-9]', '', string)) #wyrażenie regularne zamienia wszystkie cyfry różne od 0 na ''

def main() -> None:
    integer = 10928099002920
    print(f'Liczba zer w liczbie całkowitej {integer}: {count_zeros_in_int(integer)}')

if __name__ == "__main__":
    main()