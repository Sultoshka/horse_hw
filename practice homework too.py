class Parents:
    def say_a_word(self, s):
        print(s)



class Children(Parents):
    pass

children = Children()
children.say_a_word('bruh')

class car:
    def __init__(self,model, color, year):
        self.model = model
        self.color = color
        self.year = year


class SuperCar(car):
    def __init__(self, model, color, year, sponsor):
        super().__init__(model, color, year)
        self.sponsor = sponsor

petronas = SuperCar('AMG One' , 'Silver' , '2024', 'Mercedes')

print(vars(petronas))

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area (self):
        return self.width * self.height
    

Rectangle = Rectangle(4,5)
print(Rectangle.area)

Rectangle.width = 6
print(Rectangle.area)

class worker:
    def __init__(self, name, position):
        self.name = name
        self.position = position


        
class Player:
    def init(self, stamina, accuracy, power, speed):
        self.stamina= stamina
        self.accuracy= accuracy
        self.power= power
        self.speed= speed


class attacker(Player):
    def init(self, stamina, accuracy, power, speed):
        super().init(stamina,accuracy,power,speed)

    def kicking(self):
        print('Пинает мяч')

class saver(Player):
    def init(self, stamina, accuracy, power, speed):
        return super().init(stamina, accuracy, power, speed)
    
    def saver(self):
        print('защищает варата')

class trying_to_defend(Player):
    def init(self, stamina, accuracy, power, speed):
        return super().init(stamina, accuracy, power, speed)

    def trying_to_defend(self):
        print('пытается щащищять своей каманды варата')

class defender(Player):
    def init(self, stamina, accuracy, power, speed):
        return super().init(stamina, accuracy, power, speed)
    
    def defender(palyer):
        print('точно защищает свои варата')





