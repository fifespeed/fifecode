##7/12/2021 My first python script, borrowing new
##concepts of random selection
##and larger variables. Playing with
##idea of chance and fate.

import random

days = ["Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"]

heavens = ["the sun rises",
          "the sun sets",
          "the sun is obscured in clouds",
          "the moon wanes",
          "the moon waxes",
          "there is a gold harvest moon",
          "the moon thins to a cresent"]

fates = ["encounter a mysterious person with dark eyes",
"experience a sense of deja vu as you enter a building",
"lose something you think matters but in fact does not",
"find an opportunity involving risk and reward",
"learn something surprising about yourself",
"have a difficult choice to make",
"endure a hardship with a silver lining"]

random_day = random.choice(days)
random_heaven = random.choice(heavens)
random_fate = random.choice(fates)

print("        ")
print("        ")
print("        ")
print("        ")
print(f"On {random_day} as {random_heaven}, you will {random_fate}.")
print("        ")
print("        ")
print("        ")
print("        ")
