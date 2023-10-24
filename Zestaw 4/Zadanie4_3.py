"""
ZADANIE 4.3

Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię. 

Autor kodu: Jan Kaleta
"""
import re
from functools import reduce

def factorial(n: int) -> list:
    return reduce((lambda x,y: x * y), [ n - i for i in range(0,n)])
    

def main() -> None:  
    while True:
        try:
            inp = int(input("Podaj liczbe naturalną n: "))
            break
        except ValueError:
            print("Bledne dane!")
    
    print(f'{int(inp)}! = {factorial(int(inp))}')

if __name__ == "__main__":
    main()  