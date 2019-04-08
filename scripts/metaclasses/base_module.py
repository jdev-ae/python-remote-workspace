class MetaBase(type):
    def __new__(cls, name, bases, body):
        print(cls)
        print('---------------')
        print(name)
        print('---------------')
        print(bases)
        print('---------------')
        print(body)
        print('---------------')
        if bases and 'most_critical_fun' not in body:
            raise TypeError('You have to implement most_critical_fun()')
        return super().__new__(cls, name, bases, body)


class BaseX(metaclass=MetaBase):
    def base_bar(self):
        return 'base_bar from Base class'

    def base_foo(self):
        return 'Base.foo() ' + self.most_critical_fun()
