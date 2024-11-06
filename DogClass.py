"""
Create the Dog class with attributes for name and breed. Then, create a list named dogs that contains five dogs based on the following table:
Dog	Name	Breed
1	Marceline	German Shepherd
2	Cajun	Belgian Malinois
3	Daisy	Border Collie
4	Rocky	Golden Retriever
5	Bella	Irish Setter
Verify that the name and breed of the dogs in the list match the order of the table
"""
from csv import reader

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def __str__(self):
        return f"{self.name.capitalize()} is a {self.breed}"

dogs = []

with open('C:\Users\elsa.schultheiss\Downloads\Untitled spreadsheet - Sheet1.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=",")
    next(csv_reader)
    for name, description, category in csv_reader:
        dogs.append(Dog(name, breed))

print(dogs)