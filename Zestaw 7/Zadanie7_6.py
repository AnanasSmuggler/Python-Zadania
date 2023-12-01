"""
ZADANIE 7.6 (ITERATORY)
Stworzyć następujące iteratory nieskończone:
(a) zwracający 0, 1, 0, 1, 0, 1, ...,
(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].

Autor: Jan Kaleta
"""
import itertools
from timeout_decorator import timeout
from timeout_decorator import TimeoutError
import random
import time

@timeout(5)
def zero_one() -> None:
    for i in itertools.cycle([0,1]):
        print(i)

@timeout(5)
def nsew() -> None:
    for i in iter(lambda: random.choice("NSEW"), -1):
        print(i)

@timeout(5)
def week_days() -> None:
    for i in itertools.cycle([0,1,2,3,4,5,6]):
        print(i)

def main() -> None:
    try:
        zero_one()
    except TimeoutError:
        print("Koniec funkcji zero_one()")

    time.sleep(2)

    try:
        nsew()
    except TimeoutError:
        print("Koniec funkcji nsew()")

    time.sleep(2)

    try:
        week_days()
    except TimeoutError:
        print("Koniec funkcji week_days()")

if __name__ == "__main__":
    main()