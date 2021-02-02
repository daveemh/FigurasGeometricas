class Cuadrado:
    

    def area(self,lado):
        self.Area = lado**2
        print("El area es:" + " " + str(self.Area))
        return self.Area


    def perimetro(self,lado):
        self.Perimetro = lado*4
        print("El perimetro es:" + " " + str(self.Perimetro))
        return self.Perimetro
