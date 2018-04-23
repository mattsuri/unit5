#Matthew Suriawinata
#4/23/18
#fwordDemo.py - print out words with f


words = input("Type in some wordsL ").split(" ")

for item in words:
    if "f" in item or "F" in item:
        print(item)
