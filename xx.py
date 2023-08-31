# 1.在类中，我们通过__str__这个方法定制对象obj输出的内容
# 2.在类中，可以通过__init__方法可以封装实参
# 3.所以，我们可以实现：在输出对象obj时，返回封装的数据
class Foo(object):
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return 'hahaha'


obj = Foo('财务部')
print(obj)

obj = Foo('技术部')
print(obj)