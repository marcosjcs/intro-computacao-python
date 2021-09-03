import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def imprime(a, b, c):
    d = delta(a, b, c)

    if d < 0:
        print("esta equação não possui raízes reais")
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        if d == 0:
            print("a raiz desta equação é", x1)
        else:
            x2 = (-b - math.sqrt(d)) / (2 * a)
            if x1 < x2:
                print("as raízes da equação são", x1, "e", x2)
            else:
                print("as raízes da equação são", x2, "e", x1)

def main():
    a = float(input())
    b = float(input())
    c = float(input())
    imprime(a, b, c)

main()


