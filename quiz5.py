#Matthew Suriawinata
#5/4/18
#quiz5.py - 


def penultimate(list):
    pen = len(list) -2
    return(list[pen])
    
    
print(penultimate([3,4,5,6,7]))

def plusEquals(numbers,integer):
    i = 5

    for i in range(0,len(numbers)):
        numbers[i] = numbers[i] + integer
        i += 1


        return(numbers)
        
print(plusEquals([1,2,3,4],10))

def smallest(numbers):
    small = 0
    run = 1
    for i in numbers:
        if i < small or run == 1:
            small = i
            run +=1
        return(small)
    
print(smallest([1,2,3,4]))


def decimalRange(low, high, step):
    list = []
    current = low
    list.append(low)
    while current < high:
        current = current + step
        list.append(current)
        
    return list

print(decimalRange(4,10,0.5))