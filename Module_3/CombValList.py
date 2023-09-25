from collections import Counter

list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},{'item': 'item1', 'amount': 750}]

result = Counter()

for i in list:
    result[i['item']] += i['amount']
print(result)