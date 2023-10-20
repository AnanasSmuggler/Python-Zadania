"""
ZADANIE 3.9

Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. 
Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18]. 

Autor kodu: Jan Kaleta
"""

def get_sum_of_sequences(seq: list) -> int:
    return [sum(sequence) for sequence in seq]

def main() -> None:
    seq = [[],[4],(1,2),[3,4],(5,6,7)]
    print(f'Suma sekwencji wynosi: {get_sum_of_sequences(seq)}')

if __name__ == "__main__":
    main()          