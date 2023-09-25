string = 'w3resource'

result = {}

for str in string:
    if str in result:
        result[str] += 1
    else:
        result[str] = 1
print(result)