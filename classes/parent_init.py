class Parent(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.list = []


class Child(Parent):
    def __init__(self):
        age = 8
        name = 'Bernoulli'
        super(Child, self).__init__(name=name, age=age)


if __name__ == '__main__':
    child = Child()
    print(child.name)
    print(child.age)
    print(child.list)