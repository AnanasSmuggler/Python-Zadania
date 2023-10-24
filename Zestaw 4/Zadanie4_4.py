"""
ZADANIE 4.4

Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego. 

Autor kodu: Jan Kaleta
"""

def fibonacci(n: int) -> int:
    fibo = [0, 1]
    [fibo.append(fibo[i-1] + fibo[i-2]) for i in range(2,n+1)]
    return fibo[-1]

def main() -> None:
    while True:
        try:
            inp = int(input("Podaj liczbe naturalną n: "))
            break
        except ValueError:
            print("Bledne dane!")

    print(f'{int(inp)} wyraz ciągu Fibonacciego wynosi: {fibonacci(int(inp))}')

if __name__ == "__main__":
    main()  