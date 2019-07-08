

l = []

for i in range(10):
    print(i+1,"]", end = " ")
    l.append(int(input("Input Number : ")))

def my_sum(list):
    sum = 0
    for j in range(10):
        sum = sum + list[j]
    return sum
print(my_sum(l))



def my_avg(list):
    sum = my_sum(list)
    avg = sum/10

    return avg

print(my_avg(l))


