import math
from Circulo import Circulo
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado
from Triangulo import Triangulo


salir= False
At = 0
Pt = 0

while not salir:
    print(" ")
    print("Elija la figura geometrica para calcular Area y Perimetro")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Rectangulo")
    print("5. Salir")

    entrada= int(input())

    if entrada== 1:
        lado=float(input("Ingrese el lado: "))
        cuadrado=Cuadrado()
        At = At + cuadrado.area(lado)
        Pt = Pt + cuadrado.perimetro(lado)

    elif entrada == 2:
        triangulo = Triangulo()

        base= float(input("Ingrese la base: "))
        altura= float(input("Ingrese la altura: "))
        At = At + triangulo.area(base,altura)

        lado1=float(input("Ingrese el lado 1: "))
        lado2=float(input("Ingrese el lado 2: "))
        lado3=float(input("Ingrese el lado 3: "))
        Pt = Pt + triangulo.perimetro(lado1,lado2,lado3)

    elif entrada == 3:
        circulo = Circulo()
        radio=float(input("Ingrese el Radio: "))
        At= At+circulo.area(radio)
        Pt= Pt+circulo.perimetro(radio)

    elif entrada == 4:
        rectangulo= Rectangulo()
        base=float(input("Ingrese la base: "))
        altura=float(input("Ingrese la altura: "))
        At = At + rectangulo.area(base,altura)
        Pt = Pt + rectangulo.perimetro(base,altura)

    elif entrada == 5:
        print('La suma total del Area es: {:,.2f}'.format(At))
        print('La suma total del Perimetro es: {:,.2f}'.format(Pt))
        salir= True
    else:
        print("Ingrese un dato valido")   
