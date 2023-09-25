#Question 6: Write a Python program to count the number of strings where the string length is 2 or more 
#and the first and last character are same from a given list of strings.

list1 = input('Enter list : ')

list1 = list1.split(' ')

print('Original list :- ',list1)
count = 0
for element in list1: # element = tanmat
    if len(element)>=2 and element[0]==element[-1]:
        count = count + 1
print('number of string that satisfies the above condition is/are :- ', count)