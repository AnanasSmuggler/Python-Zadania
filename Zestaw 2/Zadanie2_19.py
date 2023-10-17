"""
ZADANIE 2.19
Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków, 
gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

Autor kodu: Jan Kaleta
"""

def numbers_with_zeros(l: list) -> str:
    l_with_zeros = [str(i).zfill(3) for i in l] 
    return " ".join(l_with_zeros)

def main() -> None:
    l = [1, 23, 4, 56, 789, 10, 111, 12, 234, 56, 7, 89, 23, 4, 567, 8, 910, 22, 345, 67]
    print(numbers_with_zeros(l))

if __name__ == "__main__":
    main()