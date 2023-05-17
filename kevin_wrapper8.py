class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __le__(self,o):
        return self.a <= o.a

obj1 = A(10,50)
obj2 = A(25,80)

print(obj1 <= obj2)
