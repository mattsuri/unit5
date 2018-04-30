#Matthew Suriawinata
#4/30/18
#wamrup14.py

name = input("Type in your first and last name: ").split(" ")

initials = []

for w in name:
    initials.append(w[0])
        

print("Your initlas are", initials[0], ".", initials[1], ".")

