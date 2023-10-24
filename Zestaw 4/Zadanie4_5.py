"""
ZADANIE 4.5

Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. 
Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną. 

Autor kodu: Jan Kaleta
"""

def reverse_iter(l: list, left: int, right: int) -> list:
    temp_list = [l[i] for i in reversed(range(left, right+1))]
    for i in range(len(temp_list)):
        l[i+left] = temp_list[i]
    
    return l

def reverse_rec(l: list, left: int, right: int) -> list:
    if left < right:
        l[left], l[right] = l[right], l[left]
        reverse_rec(l, left+1, right-1)

    return l

def main() -> None:
    l = [1,5,4,3,2,7,9,8,0]
    left = 2
    right = 5

    l2 = [3,36,56,13,22,81,9]
    left2 = 0
    right2 = 2
    
    print(f'Lista 1 po odwróceniu zakresu {left}-{right}: {reverse_iter(l, left, right)}')
    print(f'Lista 2 po odwróceniu zakresu {left2}-{right2}: {reverse_rec(l2, left2, right2)}')

if __name__ == "__main__":
    main()  