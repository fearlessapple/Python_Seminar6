# Напишите функцию, которая принимает на вход два списка и возвращает словарь, 
# где ключи - элементы первого списка, а значения - соответствующие элементы второго списка.

def lists_to_dict(keys, values):
    return dict(zip(keys, values))

keys = [int(s) for s in input('Input your keys: ').split()]
values = [c for c in input('Input your values: ').split()]
print(lists_to_dict(keys, values))  
