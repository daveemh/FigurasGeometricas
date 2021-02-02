class Triangulo:
    
    def area(self,base,altura):
        self.Area= (base*altura)/2
        print("El area es:" + " " + str(self.Area))
        return self.Area

    def perimetro(self,lado1,lado2,lado3):
        self.Perimetro= lado1+lado2+lado3
        print("El perimetro es:" + " " + str(self.Perimetro))
        return self.Perimetro
