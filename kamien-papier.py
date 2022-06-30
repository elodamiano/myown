import random

user = input("kamien, papier, czy nozyce? ")

computer = random.choice(["kamien", "papier", "nozyce"])

if user == computer:
    print("remis!")
elif user == "kamien":
    if computer == "papier":
        print("przegrana!")
    else:
        print("wygrana!")
elif user == "papier":
    if computer == "nozyce":
        print("przegrana!")
    else:
        print("wygrana!")
elif user == "nozyce":
    if computer == "kamien":
        print("przegrana!")
    else:
        print("wygrana!")


