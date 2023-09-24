from random import randint

# List of story templates
story_templates = [
    "Once upon a time, there was a __noun__ named __Name__. __Name__ was very __adjective__ and loved to __verb__. One day, while __verb_ing, __Name__ stumbled upon a __adjective__ __noun__. __Name__ was __adjective__ with joy and decided to __verb__ it every day.",
    "__Name__ woke up feeling very __adjective__ today. __Name__ decided to go for a __adjective__ __noun__ to feel better. While __verb_ing, __Name__ met a __adjective__ __noun__ who offered to __verb__ with __Name__. After a while, __Name__ felt __adjective__ and decided to go home.",
    "__Name__ was always fascinated by __adjective__ __noun_s. One day, __Name__ decided to __verb__ a __noun__ of their own. __Name__ spent hours __verb_ing and __verb_ing until finally, they created a __adjective__ __noun__. __Name__ was very __adjective__ and decided to __verb__ their __noun__ every day."
]

# Choose a random story template
story_template = story_templates[randint(0, 2)]

# Prompt the user to enter words


def noun():
    global noun1
    noun1 = input("Enter a noun: ")
    if noun1 == '' or any(chr.isdigit() for chr in noun1):
        print("Your input is not valid.Enter again!")
        noun()


def name():
    global name2
    name2 = input("Enter a name: ")
    if name2 == '' or any(chr.isdigit() for chr in name2):
        print("Your input is not valid.Enter again!")
        name()


def adjective():
    global adjective3
    adjective3 = input("Enter an adjective: ")
    if adjective3 == '' or any(chr.isdigit() for chr in adjective3):
        print("Your input is not valid.Enter again!")
        adjective()


def verb():
    global verb4
    verb4 = input("Enter a verb: ")
    if verb4 == '' or any(chr.isdigit() for chr in verb4):
        print("Your input is not valid.Enter again!")
        verb()


noun()
name()
adjective()
verb()


# Fill in the blanks with the user's words
story = story_template.replace("__noun__", noun1)
story = story.replace("__Name__", name2)
story = story.replace("__adjective__", adjective3)
story = story.replace("__verb__", verb4)
story = story.replace("__verb_ing", verb4 + "ing")
story = story.replace("__noun_s", noun1 + "s")

# Print the completed story
print(story)
