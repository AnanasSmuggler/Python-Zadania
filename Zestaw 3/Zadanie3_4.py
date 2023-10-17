"""
ZADANIE 3.4

Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. 
Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, 
to program ma wypisać komunikat o błędzie i kontynuować pracę. 

Autor kodu: Jan Kaleta
"""
import re

def validate_input(inp: str) -> None:
    # Wyrażenie regularne sprawdzające czy napis na wejściu jest liczbą zmiennoprzecinkową. 
    # Liczba musi być zmiennoprzecinkowa - regex nie przepuści inta
    if re.match(r'^-?\d+(?:\.\d+)$', inp) is None:
        print("Nie podano liczby zmiennoprzecinkowej!!!")
    else:
        print(f'a = {float(inp)}\na^3 = {float(inp)**3}')

def main() -> None:
    while True:
        inp = input("Podaj liczbę zmiennoprzecinkową a: ")
        if inp.lower() == "stop": break
        validate_input(inp)

if __name__ == "__main__":
    main()