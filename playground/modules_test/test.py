import testmodule as tm
from importlib import reload

print('test.py')
tm.fun_a()
print('-------------------------------------')
from testmodule import fun_a
tm.fun_a()
print('-------------------------------------')
reload(tm)