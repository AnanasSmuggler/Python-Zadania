"""
ZADANIE 4.2

Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return. 
Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów. 

Autor kodu: Jan Kaleta
"""

def has_less_digits(prev: int, next: int) -> bool:
    return len(str(prev)) < len(str(next))

#Składamy dwa stringi ze sobą w jeden przy pomocy list comprehension
def draw_measure(length: int) -> str:
    part1 = ["|" for i in range(length)]
    part2 = ['{: <5}'.format(str(i)) if not has_less_digits(i,i+1) else '{: <4}'.format(str(i)) for i in range(length)]

    return "....".join(part1) + "\n" + "".join(part2)

def draw_line(length: int, symbol: str, separator: str) -> str:
    plus = [symbol for i in range(length+1)]
    return separator.join(plus) + "\n"

def draw_rectangle(row: int, column: int) -> str:
    lines = [draw_line(column, "+", "---") for i in range(row+1)]
    separator = draw_line(column, "|", "   ")
    return separator.join(lines)

def main() -> None:
    print(draw_measure(13))
    print(draw_rectangle(2,4))

if __name__ == "__main__":
    main()