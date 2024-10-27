# 7) Fibonacci Sequence Generator (4 ქულა)
# Create a program that receives an integer n 
# and returns the first n numbers in the Fibonacci
# sequence. The sequence starts with 0 and 1, and
# each subsequent number is the sum of the previous
# two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]
def func(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(func(5))
print(func(7))

# done