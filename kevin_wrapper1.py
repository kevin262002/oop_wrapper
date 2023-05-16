class A():

    def get_String(self):
        self.str1 = input("Name : ")

    def print_String(self):
        print(self.str1.upper())

str1 = A()
str1.get_String()
str1.print_String()
