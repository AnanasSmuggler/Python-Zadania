"""
ZADANIE 4.6

Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje. 
Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)). 
"""

def sum_seq(sequence: list) -> int:
    return sum(i if not isinstance(i, (list, tuple)) else sum_seq(i) for i in sequence)

def main() -> None:
    sequence = [1,(6,3),4,9,[0,3,6,2,1], 8, (3,5)]
    print(f'Suma sekwencji wynosi: {sum_seq(sequence)}')

if __name__ == "__main__":
    main()  