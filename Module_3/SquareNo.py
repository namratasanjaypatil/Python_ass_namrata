list = []

for i in range(1,31):
    list = list + [i*i]
    
list1 = list[:5] + list[-5:]

print(list1)