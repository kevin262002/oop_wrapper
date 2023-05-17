class Shape:
    def calculate(self):
        self.l = int(input("Enter The Length : "))
        self.w = int(input("Enter The Width : "))

    def area1(self):
        self.ar = self.l*self.w

    def area2(self):
        self.tr = 0.5*self.l*self.w

class Rectangle(Shape):
    def area1(self):
        super().area1()
        print("Area Of Rectangle : ",self.ar)

class Triangle(Shape):
    def area2(self):
        super().area2()
        print("Area Of Triangle : ",self.tr)

obj1 = Rectangle()
obj2 = Triangle()

obj1.calculate()
obj1.area1()

obj2.calculate()
obj2.area2()


        
        
