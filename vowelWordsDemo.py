#Matthew Suriawinata
#4/26/18
#vowelWordDemo.py - treat strings as lists 

words = input("Type in some words: ").split(" ")

for w in words:
    if w[0] in "AEIOUaeiou":
        print(w)