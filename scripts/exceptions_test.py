try:
    a = 10
    b = 2

    c = a / b

    f = open('sample.txt', 'w')
    f.write('Sample text')
    f.close()
except OSError as e:
    print(type(e))
# else:
#     print('not a OS ERROR')
except ZeroDivisionError as r:
    print('division zero xx')
else:
    print('its good')
