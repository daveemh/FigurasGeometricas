class Rectangulo:
    def area(self,base,altura):
        self.Area= base*altura
        print("El area es:" + " " + str(self.Area))
        return self.Area

    def perimetro(self,base,altura):
        self.Perimetro = base*2 + altura*2
        print("El perimetro es:" + " " + str(self.Perimetro))
        return self.Perimetro
