class Rectangulo:
    def area(self,base,altura):
        self.area= base*altura
        print("El area es" + " " + str(self.area))
        return self.area

    def perimetro(self,base,altura):
        self.perimetro = base*2 + altura*2
        print("El perimetro es" + " " + str(self.perimetro))
        return self.perimetro
