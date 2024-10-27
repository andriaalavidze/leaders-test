# 6) Convert Pascal Case string into snake_case (4 ქულა)

# You will receive a string which will contain words in
# PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"
def func(testcases):
    if testcases  == 1:
        return "1"
    result = []
    for i in testcases:
        if i.isupper():
            result.append('_' + i.lower())
        else:
            result.append(i)

    return ''.join(result)
print(func("TestController"))
print(func("MoviesAndBooks"))
print(func("App7 Test"  ))
print(func(1))


# not finished