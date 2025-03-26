import random

lucky_number = random.randint(1, 100)

fortune_number = random.randint(1, 3)

fortune_text = ""

if fortune_number == 1:
    fortune_text = "A stranger will cross your path who later becomes your friend!"
if fortune_number == 2:
    fortune_text = "A beautiful, smart, and loving person will be coming into your life!"
if fortune_number == 3:
    fortune_text = "You have a secret admirer!"

print(f"{fortune_text}! Your Lucky Number is: {lucky_number}")