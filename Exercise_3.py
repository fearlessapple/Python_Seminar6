# Напишите функцию, которая принимает список строк и возвращает список с длинами этих строк, используя map.

input_list = [s for s in input('Input your elements: ').split()]
def len_output(words):
    result = list(map(len, words))
    return result
print(len_output(input_list))