"""
ZADANIE 3.1

Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

1) 
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

2)
for i in "axby": if ord(i) < 100: print (i)

3)
for i in "axby": print (ord(i) if ord(i) < 100 else i)

"""

#Kod syntaktycznie jest poprawny - to znaczy uruchomi się i da nam wynik
def number_one() -> None:
    x = 2; y = 3;
    if (x > y):
        result = x;
    else:
        result = y;    
    print(result)

#Funkcja nie wykona się, ze względu na umiejscowienie if-a w kodzie. Jeśli chcemy w takiej kolejności napisać kod, 
# to cały blok if-a powinien być poniżej pętli poprzedzony tabulatorem
"""
def number_two() -> None:
     for i in "axby": if ord(i) < 100: print (i)

     Poprawiona wersja:
     for i in "axby":
        if ord(i) < 100:
            print(i)
"""

#kod jest syntaktycznie poprawny
def number_three() -> None:
     for i in "axby": print (ord(i) if ord(i) < 100 else i)

def main() -> None:
    #number_one()
    #number_two()
    number_three()


if __name__ == "__main__":
    main()