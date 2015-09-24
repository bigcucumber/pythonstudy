__author__ = 'luowen'


# staticmethod function return a static method for function

class StaticMethodClass:
    def commonMethod(self):
        return "this is not a static method"

    @staticmethod
    def staticMethod():
        return "this is a static function"


staticmethodDemo = StaticMethodClass()
print(staticmethodDemo.commonMethod())

print(StaticMethodClass.staticMethod())


