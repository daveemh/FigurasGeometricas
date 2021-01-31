class Rectangulo:
    def area(self,base,altura):
        area= base*altura
        print("El area es" + " " + str(self.area))
        return area

    def perimetro(self,base,altura):
        perimetro = base*2 + altura*2
        print("El perimetro es" + " " + str(self.perimetro))
        return perimetro
