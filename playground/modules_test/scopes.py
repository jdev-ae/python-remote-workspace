x = 1

def f1():
    print(f'locals = {locals()}')
    print(f'globals = {globals()}')
    # global x
    x = 100
    print(f'x = {x}')

f1()