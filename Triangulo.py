class Triangulo:
    
    def area(self,base,altura):
        self.area= (base*altura)/2
        print("El area es" + " " + str(self.area))
        return self.area

    def perimetro(self,lado1,lado2,lado3):
        self.perimetro= lado1+lado2+lado3
        print("El perimetro es" + " " + str(self.perimetro))
        return self.perimetro
