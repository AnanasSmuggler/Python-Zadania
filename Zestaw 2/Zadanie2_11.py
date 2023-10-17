"""
ZADANIE 2.11
Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

Autor kodu: Jan Kaleta
"""

def enter_sign_between_signs(sign: str, string: str) -> str:
    return sign.join(string)

def main() -> None:
    string = "Napis do rozdzielenia znakami podkreślenia"
    print(enter_sign_between_signs('_', string))


if __name__ == "__main__":
    main()