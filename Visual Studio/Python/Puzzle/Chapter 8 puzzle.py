import turtle
jake = turtle.Pen()
josh = turtle.Pen()
avery = turtle.Pen()
joe = turtle.Pen()

jake.forward(50)
jake.right(90)
jake.forward(40)
jake.left(90)
jake.forward(40)

josh.forward(50)
josh.left(90)
josh.forward(40)
josh.right(90)
josh.forward(40)

avery.forward(55)
avery.right(90)
avery.forward(20)
avery.left(90)
avery.forward(20)

joe.forward(55)
joe.left(90)
joe.forward(20)
joe.right(90)
joe.forward(20)

class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')
        
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
    def left_Foot_Forward(self):
        print('left foot forward')
    def right_Foot_Forward(self):
        print('right foot forward')
    def left_Foot_Back(self):
        print('left foot back')
    def right_Foot_Back(self):
        print('right foot back')
    def dance(self):
        self.left_Foot_Forward()
        self.right_Foot_Forward()
        self.left_Foot_Back()
        self.right_Foot_Back()

reginald = Giraffes()
reginald.dance()
