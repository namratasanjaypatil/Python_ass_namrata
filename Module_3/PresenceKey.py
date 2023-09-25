"""
In Python, you can check the presence of a key in a dictionary using the in operator or the get() method. 
"""

dict = {1:'nammu', 2:'kishu', 3:'nik', 4:'piu', 5:'diu', 6:'bhavesh'}

dict_key = int(input('enter the key : '))

if dict_key in dict:
    print('key present in dict.' , 'key is ', dict_key , '&' , 'value is',dict[dict_key])
else:
    print('key not present')