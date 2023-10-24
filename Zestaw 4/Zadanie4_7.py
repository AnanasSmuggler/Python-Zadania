"""
ZADANIE 4.7

Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. 
Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, 
a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))   # [1,2,3,4,5,6,7,8,9]

"""

def flatten(seq: list) -> list:
        return [item for sublist in seq for item in (flatten(sublist) if isinstance(sublist, (list, tuple)) else [sublist]) ]

def main() -> None:
    seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
    print(f'Spłaszczona lista: {flatten(seq)}')

if __name__ == "__main__":
    main()  