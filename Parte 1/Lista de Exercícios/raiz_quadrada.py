def main():
    
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = (b ** 2) - (4 * a * c)
    
    if delta < 0:       
        print("A equação não possui raiz real.")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        if delta == 0:
            print("A raiz da equação é:",x1)
        else:            
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            if x1 < x2:
                print("As raízes da equação são:",x1, "e", x2)
            else:
                print("As raízes da equação são:",x2, "e", x1)
    
import math
main()
