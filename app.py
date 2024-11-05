#"Are you guys looking at my notes? " - LaRose
#"Shut it" - LaRose
#"Did you really just? " - LaRose
#"Yeah, that's stupid" - LaRose
#"I do, just not frequently " - LaRose
#"No, it's not malware" - LaRose
#"I would like to remind you you are the advanced programming class. " - LaRose
#"It exists, it's there, it's fine. " - LaRose
#
class App:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
    
    def __str__(self):
        return f"{self.name} is a(n) {self.category} app that is {self.description}. "