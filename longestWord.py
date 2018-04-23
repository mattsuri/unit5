#Matthew Suriawinata
#4/23/18
#longestWord.py

words = input("Enter some words, dood: ").split()


l = 0
word = ""
for w in words:
    length = len(w)
    if length > l:
        l = length
        word = w
print("The longest word is", word)
