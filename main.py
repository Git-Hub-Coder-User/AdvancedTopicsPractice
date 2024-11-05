#"This is why my other classes don't get to watch me code. " - LaRose
#"Who can guess what we're going to print?!" - LaRose
#"Absolutely insane. " - LaRose
#"So close to being funny. So close. " - LaRose
#"No, as if it would be that simple. " - LaRose
#"Still not funny. " - LaRose
#"Why do you assume I hate you? " - LaRose
#"I told you, the 'p' doesn't work. " - LaRose
#"I've not been paid anything" - LaRose
#"I hate it so much" - LaRose
#"Are we still all hyperventilating or does our file exist? " - LaRose
#"You're getting lost because you're distracted. " - LaRose
#"The crazy choas" - LaRose
#"You didn't listen until I sat there and pointed at it"
from app import App
from csv import reader

apps = []

with open('app_list.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=",")
    next(csv_reader)
    for name, description, category in csv_reader:
        apps.append(App(name, description, category))

for app in apps:
    print(app)