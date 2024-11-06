"""
Then on your main.py page import tech.py

Instantiate an instance of phone and an instance of laptop and print both instances, and print the repr for both instances. 
"""

from tech import Tech, Phone, Laptop

myPhone = Phone("iPhone 6", 64, "pink")
myLaptop = Laptop("iMac 6", 640, 32)

print(myPhone)
print(myLaptop)
print(repr(myPhone))
print(repr(myLaptop))