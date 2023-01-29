# Используя filter(), создать функцию, которая принимает список и возвращает только элементы, которые встречаются в списке более одного раза.

input_list = [s for s in input('Input your elements: ').split()]
def change_list(input_list):
    result = list(filter(lambda x: input_list.count(x) > 1, input_list))
    return result
print(change_list(input_list))