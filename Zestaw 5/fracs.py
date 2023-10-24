import math

#Skrócenie ułamka do najprostszej postaci
def simplify_frac(frac: list) -> list:
    gcd = math.gcd(frac[0], frac[1])
    return [frac[0] / gcd, frac[1] / gcd]

#Rozszerzanie ułamków do wspólnego mianownika
def extend_frac(frac1: list, frac2: list) -> tuple[list, list]:
        denominator = lcm(frac1[1], frac2[1])
        frac1[0] *= int(denominator / frac1[1])
        frac2[0] *= int(denominator / frac2[1])
        frac1[1] = frac2[1] = denominator
        return frac1, frac2

#NNW - najmniejsza wspólna wielokrotność
def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a,b)

#Ustala znak ułamka i ustawia go w liczniku (dodatni/ujemny)
def handle_sign(frac: list) -> list:
    if (frac[0] > 0 and frac[1] < 0) or (frac[0] < 0 and frac[1] < 0):
        frac[0], frac[1] = -frac[0], -frac[1]

    return frac

#Dodawanie ułamków
def add_frac(frac1: list, frac2: list) -> list:
    if frac1[1] != frac2[1]:
        frac1, frac2 = extend_frac(frac1, frac2)

    return simplify_frac([frac1[0] + frac2[0], frac1[1]])

#Odejmowanie ułamków
def sub_frac(frac1: list, frac2: list) -> list:        # frac1 - frac2
    if frac1[1] != frac2[1]:
        frac1, frac2 = extend_frac(frac1, frac2)

    return simplify_frac([frac1[0] - frac2[0], frac1[1]])

#Mnożenie ułamków
def mul_frac(frac1: list, frac2: list) -> list:        # frac1 * frac2
    return simplify_frac([frac1[0] * frac2[0], frac1[1] * frac2[1]])

#Dzielenie ułamków
def div_frac(frac1: list, frac2: list) -> list:        # frac1 / frac2
    return simplify_frac([frac1[0] * frac2[1], frac1[1] * frac2[0]])

#Czy ułamek jest dodatni
def is_positive(frac: list) -> bool:              # bool, czy dodatni
    return (frac[0] > 0 and frac[1] > 1) or (frac[0] < 0 and frac[1] < 0)

#Czy ułamek jest równy 0
def is_zero(frac: list) -> bool:                # bool, typu [0, x]
    return frac[0] == 0

#Porównywanie ułamków
def cmp_frac(frac1: list, frac2: list) -> int:         # -1 | 0 | +1
    
    frac1, frac2 = handle_sign(frac1), handle_sign(frac2)
    
    if frac1[1] != frac2[1]:
        frac1, frac2 = extend_frac(frac1, frac2)

    res = 0

    if frac1[0] < frac2[0]:
        res = -1
    elif frac1[0] > frac2[0]:
        res = 1
    
    return res

#Konwersja ułamka do float
def frac2float(frac: list) -> float:           # konwersja do float
    frac = handle_sign(frac)
    return frac[0]/frac[1]

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)