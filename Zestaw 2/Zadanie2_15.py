"""
ZADANIE 2.15
Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

Autor kodu: Jan Kaleta
"""

def create_string_from_int_list(l: list) -> str:
    str_list = [str(i) for i in l]
    
    return "".join(str_list)

def main() -> None:
    num_list = [7,12,34,19,63,5,28,42,9,51]
    print(create_string_from_int_list(num_list))

if __name__ == "__main__":
    main()