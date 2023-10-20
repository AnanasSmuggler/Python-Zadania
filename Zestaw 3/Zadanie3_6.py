"""
ZADANIE 3.6

Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   | 
+---+---+---+---+

Autor kodu: Jan Kaleta
"""
def draw_line(length: int, symbol: str, separator: str) -> str:
    plus = [symbol for i in range(length+1)]
    return separator.join(plus) + "\n"

def draw_rectangle(row: int, column: int) -> str:
    lines = [draw_line(column, "+", "---") for i in range(row+1)]
    separator = draw_line(column, "|", "   ")
    return separator.join(lines)

def main() -> None:
    print(draw_rectangle(3,5))

if __name__ == "__main__":
    main()