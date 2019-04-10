def say_hi(name_fun): # decorator
    print('say hi: started')
    def your_name(name): # wrapper
        print('wrapper started!')
        name_fun(name)
        print('wrapper ended!')
    print('say hi: ended')

    return your_name

@say_hi
def get_name(name):
    print('Hello get name: ' + name)

get_name('SuRu')

# total_fun = say_hi(get_name)

# total_fun()