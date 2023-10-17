"""
ZADANIE 3.3

Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3. 

Autor kodu: Jan Kaleta
"""

def numbers_not_divisible_by(rng: int, not_div: int) -> list:
    return [i for i in range(rng + 1) if i % 3 != 0]

def main() -> None:
    print(f'Liczby nie podzielne przez 3 z zakresu 0-30: {numbers_not_divisible_by(30, 3)}')

if __name__ == "__main__":
    main()