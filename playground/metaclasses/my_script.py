from base_module import BaseX


class Derived(BaseX):
    def my_fun(self):
        return 'Some random function'

    def most_critical_fun(self):
        return 'The most critical function in Derived....'

d = Derived()
print(d.base_foo())