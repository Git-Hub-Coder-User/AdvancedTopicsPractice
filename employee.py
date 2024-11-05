#"I'm trying to be lazy. You guys are so whiny. " - LaRose
class Employee:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __str__(self):
        return f"Employee: {self.name}\nTitle: {self.title}"
    
def greeting():
    print('Hello from the "employee.py" module/page')
    