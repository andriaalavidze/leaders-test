# 3) Remove Duplicates from a List (3 ქულა)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']


def func(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result
   
print(func([1, 2, 2, 3, 4, 4, 5]))
print(func(['a', 'b', 'a', 'c']))

# done