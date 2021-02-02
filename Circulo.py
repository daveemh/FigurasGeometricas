import math

class Circulo:
    

    def area(self,radio):
        self.Area= math.pi*(radio**2)
        print('El area es: {:,.2f}'.format(self.Area))
        return self.Area

    def perimetro(self,radio):
        self.Perimetro=2*math.pi*radio
        print('El perimetro es: {:,.2f}'.format(self.Perimetro))
        return self.Perimetro
