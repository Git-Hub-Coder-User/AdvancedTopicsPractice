#Composition is a type of class that exists inside of another class (class has a other class)
    #Is a relation or has a relationship
    #A vampire is a monster: Yes, Inheritance
    #Does a vampire have a monster: No
    #Inheritance in the class composition has the class

#"We'd hope it has a driver, but you know. " - LaRose
#"That's almost a car person" - LaRose
#"They get mad when I say I don't understand what they're talking about" - LaRose
#"The red ones go faster, it's proven" - LaRose
#"This isn't exactly rocket science" - LaRose "It's car science" - Class
#"Nope, that's totally how it works" - LaRose
#"This car has no engine. It's really awkward" - LaRose
#"It says vroom vroom" - LaRose
#"Basically Lightning McQueen" - LaRose
#"My car, Healthy? Lol, no? " - LaRose
class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
    
    def __str__(self):
        return f"{self.year}, {self.make}, {self.model}"
    
    #This method is for other programmers and it is for debugging purposes We want to tell them the class and all attributes
    def __repr__(self):
        return f"Car({self.make}, {self.model}, {self.year}, {self.engine})"

class Engine:
    def __init__(self, configuration, displacement, horsepower, torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque
    
    def __str__(self):
        return f"The engine is a {self.configuration}, with {self.displacement} displacement, {self.horsepower} horsepower, and {self.torque} torque"
    
    def __repr__(self):
        return f"Engine({self.configuration}, {self.displacement}, {self.horsepower}, {self.torque})"

    def ignite(self):
        print("Vroom, vroom! ")

myEngine = Engine("V8", 5.8, 326, 344)
myCar = Car("Mazda", "Mazda3", 2013, myEngine)


print(myCar)
#To acess a composite class, you have to call that specific item from your class
myCar.engine.ignite()
print(repr(myCar))
print(repr(myEngine))