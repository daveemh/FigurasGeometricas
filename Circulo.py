import math

class Circulo:
    

    def area(self,radio):
        area= math.pi*(radio**2)
        print('El area es: {:,.2f}'.format(self.area))
        return area

    def perimetro(self,radio):
        perimetro=2*math.pi*radio
        print('El perimetro es: {:,.2f}'.format(self.perimetro))
        return perimetro
    