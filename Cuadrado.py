class Cuadrado:
    def area(self,lado):
        self.area = lado**2
        print("El area es" + " " + str(self.area))

        return self.area


    def perimetro(self,lado):
        self.perimetro = lado*4
        print("El perimetro es" + " " + str(self.perimetro))
        return self.perimetro
