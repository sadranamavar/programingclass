#!/usr/bin/python3

number_of_number = 3

numbers = {}

for _ in range(number_of_number):
    numbers[input("pls import a number")] = 0



for i in numbers:
    for j in range(2,int(i)):
        if int(i) % j == 0 :
            numbers[i] += 1
        
print(numbers)
print(max(numbers,key=numbers.get))