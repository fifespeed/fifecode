##07/12/2021 My daughter likes a type of toy
##called fidgets. There are many kinds.
##This is a playful attempt to make
##a fidget random selection tool.

##Eventually, I will learn another way
##but for now, I'm using these print statements
##to create space when running outputs
##in the terminal shell.

print("          ")
print("          ")

name = input("Please enter your first name: ")

##Setting up the random selction & variables.

import random

colors = ["red",
        "blue",
        "green",
        "pink",
        "pale orange",
        "yellow"]

fidgets = ["pop-it",
          "squishy ball",
          "whacky twisty trax",
          "fidget pad",
          "monkey noodle",
          "simple dimple"]

actions = ["try getting a toot sound.",
"practice enjoying life here and now.",
"go to your happy place.",
"find yourself in a relaxing world.",
"rate it on a fun scale of 1 to 10.",
"feel it and observe your consciousness."]


##Creating variables of the variables.
##As I learn more, I hope to explain this better.

random_color = random.choice(colors)
random_fidget = random.choice(fidgets)
random_action = random.choice(actions)

print("        ")
print("        ")
print("        ")
print("        ")

## And finally, putting together the input
## with the random selection from
##3 variable categories.

print(f"How's it going, {name.title()}?")
print(f"We recommend a {random_color} {random_fidget} "
f"to help you {random_action}")
print("        ")
print(f"Enjoy your {random_fidget}!")
print("        ")
print("        ")
print("        ")
