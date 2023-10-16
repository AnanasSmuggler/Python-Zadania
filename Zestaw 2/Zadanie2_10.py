"""
ZADANIE 2.10
Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. 
Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony 
od innych wyrazów białymi znakami (spacja, tabulacja, newline).
"""

def count_words_in_string(string: str) -> int:
    words = string.split()
    return len(words)

def main() -> None:
    
    string = """Ten string przeznaczony jest do celów testowych 
i ma na celu sprawdzić funkcję, która policzy ile słów dany łańcuch znaków posiada.
Ten łańcuch posiada 26 słów."""
    print(string)
    print(f'Policzona ilość słów: {count_words_in_string(string)}')

if __name__ == "__main__":
    main()