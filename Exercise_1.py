# Написать функцию, которая принимает список слов и возвращает список слов длиной более 5 символов, используя lambda функцию.

words = [s for s in input('Input your words: ').split()]
def change_list(words):
    result = list(filter(lambda x: len(x)>5, words))
    return result
print(change_list(words))
