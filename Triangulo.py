class Triangulo:
    
    def area(self,base,altura):
        area= (base*altura)/2
        print("El area es" + " " + str(self.area))
        return area

    def perimetro(self,lado1,lado2,lado3):
        perimetro= lado1+lado2+lado3
        print("El perimetro es" + " " + str(self.perimetro))
        return perimetro
