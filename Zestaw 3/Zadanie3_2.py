"""
ZADANIE 3.2

Co jest złego w kodzie:

L = [3, 5, 4] ; L = L.sort()

x, y = 1, 2, 3

X = 1, 2, 3 ; X[1] = 4

X = [1, 2, 3] ; X[3] = 4

X = "abc" ; X.append("d")

L = list(map(pow, range(8)))


Autor: Jan Kaleta
"""

def number_one() -> None:
    #L = [3, 5, 4] ; L = L.sort() - nie musimy nadpisywać zmiennej L, wręcz jest to niewskazane. 
    #W Pythonie, każde utworzenie czy nadpisanie zmiennej zajmuje kolejną komórkę w pamięci, więc należy unikać takich rzeczy.
    l = [3,5,4]
    l.sort()
    print(l)

def number_two() -> None:
    #x, y = 1, 2, 3 - w tym zapisie chcemy przypisać wartość 3 do nieistniejącej zmiennej
    x, y, z = 1, 2, 3
    print(x,y,z)

def number_three() -> None:
    #X = 1, 2, 3 ; X[1] = 4 - obiekt tuple, którym jest x nie wspiera przypisywania elementów. 
    #Jeśli chcemy w taki sposób przypisać element, powinniśmy użyć listy
    x = [1, 2, 3]
    x[1] = 4
    print(x[1])

def number_four() -> None:
    #X = [1, 2, 3] ; X[3] = 4 - indeks poza skalą
    x = [1,2,3]
    x.append(4)
    print(x)

def number_five() -> None:
    #X = "abc" ; X.append("d") - obiekt string nie posiada atrybutu append
    x = "abc"
    print(x+"d")

def number_six() -> None:
    #L = list(map(pow, range(8))) - brak odpowiednich argumentów funkcji pow
    l = list(map(lambda x: pow(x,2), range(8)))
    print(l)

def main() -> None:
    number_one()
    number_two()
    number_three()
    number_four()
    number_five()
    number_six()

if __name__ == "__main__":
    main()