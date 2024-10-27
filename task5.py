# 5) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string
# is a palindrome (reads the same forward and backward).
# The function should ignore spaces, punctuation, and
# capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

def func(testcases):
    testcases = testcases.lower()
    testcases1 = testcases.split()
    testcases2 = ''.join(testcases1)
    return testcases2 == testcases2[::-1]

print(func("A man a plan a canal Panama"))
print(func("Hello"))

# done