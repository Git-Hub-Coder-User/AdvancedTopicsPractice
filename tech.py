"""
Write a program that has 3 classes on a file called "tech.py". Those classes should be Tech (the parent class), Phone, and Laptop (the child classes) 

 

1. Tech should initialize name and storage

(Note that storage should be an integer!)

2. Phone should initialize color

Have a __str__ method that prints out "A {color} {name} with {storage} of storage."

EXAMPLE: A sage Pixel 5 with 128GB of storage

have a __repr__ method that prints "Phone({the name}, {storage}, {the color})

EXAMPLE: Phone(Pixel 5, 128, sage)

3. Laptop should initialize size

- Have a __str__ method that prints out "{size}-inch {name} with {storage} of storage."

     EXAMPLE: 15-inch MacBook Pro with 256GB of storage.

-have a __repr__ method that prints "Laptop({the name}, {storage}, {the size})

     EXAMPLE: Laptop(MacBook Pro, 256, 15)

(NOTE: Size should be an integer!)
 """

class Tech:
    def __init__(self, name, storage):
        self.name = name
        self.storage = storage

class Phone(Tech):
    def __init__(self, name, storage, color):
        super().__init__(name, storage)
        self.color = color
    
    def __str__(self):
        return f"A {self.color} {self.name} with {self.storage}GB of storage. "
    
    def __repr__(self):
        return f"Phone({self.name}, {self.storage}, {self.color})"

class Laptop(Tech):
    def __init__(self, name, storage, size):
        super().__init__(name, storage)
        self.size = size
    
    def __str__(self):
        return f"{self.size}-inch {self.name} with {self.storage}GB of storage"
    
    def __repr__(self):
        return f"Laptop({self.name}, {self.storage}, {self.size})"