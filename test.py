class test():
    def __init__(self):
        print('Sucsess')
class testa():
    def __init__(self):
        print('Sucsessa')
class testb():
    def __init__(self):
        print('Sucsessb')

test_list = [testb, test, testa, testa, testa, testb]
print('#########################')
for i in test_list:
    i()