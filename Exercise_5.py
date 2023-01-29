# Напишите функцию, которая принимает список чисел и возвращает список кортежей, 
# где первый элемент каждого кортежа - это индекс числа, а второй элемент - это само число.

numbers = [int(s) for s in input("Input your numbers: ").split()]
def index_number_tuples(numbers):
    return list(enumerate(numbers))
print(index_number_tuples(numbers))