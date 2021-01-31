class Cuadrado:
    
    def area(self,lado):
        area = lado**2
        print("El area es" + " " + str(self.area))

        return area


    def perimetro(self,lado):
        perimetro = lado*4
        print("El perimetro es" + " " + str(self.perimetro))
        return perimetro
