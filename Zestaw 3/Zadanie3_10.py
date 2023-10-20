"""
ZADANIE 3.10

Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) 
na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()]. 

Autor kodu: Jan Kaleta
"""

#Jak tworzymy słownik:
#   1) Przy pomocy {}:
#       my_dict = {} - tworzymy pusty słownik
#       person = {
#           "imie": "Jan",
#           "nazwisko": "Kaleta",
#           "nazwa_repozytorium": "Python zadania"
#       }
#   
#   2) Przy pomocy funkcji dict():
#       my_dict = dict() - pusty słownik
#       person = dict( imie = "Jan", nazwisko = "Kaleta", nazwa_repozytorium = "Python zadania")

import re

def roman2int(inp: str) -> str:
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    prev = 0

    for i in inp[::-1]:
        value = roman_numerals[i]
        result += -value if value < prev else value
        prev = value 

    return result

def is_roman_numeral(inp: str) -> str:
    return roman2int(inp) if re.match(r"^(M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}))$", inp) else "Podany ciąg znaków nie jest liczbą rzymską"

def main() -> None:    
    print(is_roman_numeral(input("Podaj liczbę rzymską: ")))

if __name__ == "__main__":
    main()  