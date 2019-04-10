import shelve

# with shelve.open('test_shelve') as test:
#     test['a'] = 'man'
#     test['b'] = {
#         'data': 'quick look',
#         'version': 23,
#         'auth': ('yuipok', 'HJGKUYlak&*jd')
#     }
#

with shelve.open('test_shelve') as t:
    for k, v in t.items():
        print(k)
        print(v)
        print('-' * 40)
        print(k)

with shelve.open('test_shelve') as t:
    for k, v in t.items():
        print(v)
        print('-' * 40)
        print(34)
        print('er')


def fun():
    value = 'sa'
    print(value)
    a = 1
    b = a + 1
    print(b)
    print('`' * 100)


if __name__ == '__main__':
    fun()
