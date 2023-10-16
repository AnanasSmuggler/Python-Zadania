"""
ZADANIE 2.12
Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
"""

def first_signs_of_lines(string: str) -> list:
    lines = string.split("\n")
    return [i[0] for i in lines]

def last_signs_of_lines(string: str) -> list:
    lines = string.split("\n")
    return [i[-1] for i in lines]

def main() -> None:
    string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum faucibus ipsum quam, non ornare orci molestie at. Aenean turpis
lacus, maximus eu purus ac, luctus pretium nibh. Donec eget lorem nibh. Nullam accumsan scelerisque metus, at pulvinar velit placerat
quis. Cras ultricies vulputate ultrices. Sed sit amet vehicula velit. Ut consectetur mattis aliquam. In hac habitasse platea dictumst. Aenean
id molestie enim. In tempor magna eu luctus lacinia. Pellentesque rutrum dolor feugiat ante consectetur dignissim. Aenean in bibendum
mi, et congue magna."""

    print(f'Pierwsze znaki łańcucha: {first_signs_of_lines(string)}')
    print(f'Ostatnie znaki łańcucha: {last_signs_of_lines(string)}')

if __name__ == "__main__":
    main()