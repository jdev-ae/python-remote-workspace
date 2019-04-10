import one
import three_file

print('-' * 100)

print('file  ->  two.py')

print('one.py __name__={}'.format(__name__))
print('one.py __file__={}'.format(__file__))

print('-' * 100)

three_file.three_fun()

three_file.