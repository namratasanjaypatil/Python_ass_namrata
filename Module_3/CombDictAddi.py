d1 = {'a': 100, 'b': 200, 'c': 200, 'd': 300}
d2 = {'a': 300, 'b': 200, 'd': 100, 'c': 100}

for key in d2:
    if key in d1:
        d2[key] = d2[key] + d1[key]
    else:
        pass
         
print(d2)