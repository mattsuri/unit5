#Matthew Suriawinata
#4/25/18
#warmup13.py 


from random import randint

numbers = []
for i in range(0,20):
    numbers.append(randint(1,100)) 
    
print(numbers)
    
print("Sum = ", sum(numbers))
print("Min = ", min(numbers))
print("Max = ", max(numbers))



