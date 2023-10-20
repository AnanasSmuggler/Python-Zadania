"""
ZADANIE 3.5

Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12

"""

def has_less_digits(prev: int, next: int) -> bool:
    return len(str(prev)) < len(str(next))

def draw_measure(length: int) -> str:
    part1 = ["|" for i in range(length)]
    part2 = ['{: <5}'.format(str(i)) if not has_less_digits(i,i+1) else '{: <4}'.format(str(i)) for i in range(length)]

    return "....".join(part1) + "\n" + "".join(part2)

def main() -> None:
    print(draw_measure(13))

if __name__ == "__main__":
    main()