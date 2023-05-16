class Player:
    def data1(self):
        print("Batsman Name : Virat Kohli")
        print("Bowler Name : Jasprit Bumrah")

class Cricketplayer(Player):
    def data2(self):
        print("Virat Kohli T20 Match : 355")
        print("Jasprit Bumrah T20 Match : 210")
    
class Batsman(Cricketplayer):
    def data3(self):
        print("Virat Kohli Run : 11764")
        a= 11764/355
        print("Virat Kohli Avg : ",a)

class Bowler(Cricketplayer):
    def data4(self):
        print("Jasprit Bumrah Wicket : 256")
        b = 256/210
        print("Jasprit Bumrah Avg : ",b)


obj1 = Batsman()
obj2 = Bowler()

obj1.data1()
print()
obj1.data2()
print()
obj1.data3()
print()

#obj2.data1()
#obj2.data2()
obj2.data4()
