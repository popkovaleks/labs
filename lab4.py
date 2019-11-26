class  A:

    def __init__(self, a):
        self.a = a

    def show(self):
        print(self.a)

    def r_show(self):
        return self.a

    def __repr__(self, show):
        return 'class A, variable a = ' + show()

class B(A):

    def show(self):
        print(self.a + ' , this is inherited class')

    def r_show(self):
        return self.a + ' , this is inherited class'

    def __repr__(self, show):
        return 'class B(inherited), variable a = ' + show()

def main():
    a = A('Hello')
    b = B('Hello')
    a.show()
    b.show()
    print(a.__repr__(a.r_show))
    print(b.__repr__(b.r_show))


if __name__ == '__main__':
    main()
