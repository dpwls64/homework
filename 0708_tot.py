import sys

l = []

for i in range(10):
    print(i+1,"]", end = " ")
    l.append(int(input("Input Number : ")))


def my_max(list):
   
    max_val = list[0]
    
    for j in range(10):
        if list[j] > max_val:
            max_val = list[j]
    
    return max_val

def my_min(list):
    min_val = list[0]
    for j in range(10):
        
        if list[j] < min_val:
            min_val = list[j]
    
    return min_val

def my_sum(list):
    sum = 0
    for j in range(10):
        sum = sum + list[j]
    return sum


def my_avg(list):
    sum = my_sum(list)
    avg = sum/10

    return avg

print(my_max(l))
print(my_min(l))
print(my_sum(l))
print(my_avg(l))
