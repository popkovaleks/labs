class  A:

    def __init__(self, a):
        self.a = a

    def show(self):
        print(self.a)

    def __repr__(self):
        return 'class A, variable a = ' + self.a

class B(A):

    def show(self):
        print(self.a + ' , this is inherited class')

    def __repr__(self):
        return 'class B(inherited), variable a = ' + self.a

def main():
    a = A('Hello')
    b = B('Hello')
    a.show()
    b.show()
    print(a.__repr__())
    print(b.__repr__())


if __name__ == '__main__':
    main()
