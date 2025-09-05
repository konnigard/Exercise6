import random
rand1 = random.randint(0, 100)
rand2 = random.randint(0,100)

while True:
    if rand1 + rand2 == 69:
        print(f"{rand1} + {rand2} is 69")
        break
    rand1 = random.randint(0, 100)
    rand2 = random.randint(0,100)

scooby_gang = input("Plese enter the first name you're favorite Scooby-Gang Member: ")

if (scooby_gang == "Scooby" or scooby_gang == "scooby"):
    print ("Rugh row")
elif (scooby_gang == "Shaggy" or scooby_gang == "shaggy" or scooby_gang == "Norville" or scooby_gang == "norville"):
    print ("Zoinks!")
elif (scooby_gang == "Velma" or scooby_gang == "velma"):
    print ("Jinkies!")
elif (scooby_gang == "Daphne" or scooby_gang == "daphne"):
    print ("Jeepers!")
elif (scooby_gang == "Fred" or scooby_gang == "fred"):
    print ("FUCK!")
elif (scooby_gang == "Buffy" or scooby_gang == "Buffy"):
    print ("Wrong Scooby-Gang")
else: 
    print("That's not a member of the Scooby-Gang")
