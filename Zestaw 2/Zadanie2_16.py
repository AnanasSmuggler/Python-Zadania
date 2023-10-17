"""
ZADANIE 2.16
W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

Autor kodu: Jan Kaleta
"""

def replace_str(string: str, to_replace: str, replacement: str) -> str:
    return string.replace(to_replace, replacement)

def main() -> None:
    string = "W tym GvR zdaniu, podmieniamy GvR na inny GvR napis, który GvR zastąpi GvR"
    print(f'Przed zamianą: {string}')
    print(f'Po zamianie: {replace_str(string, "GvR", "Guido van Rossum")}')

if __name__ == "__main__":
    main()