class Parent:
    def echo(self):
        print('I am from Parent class')

class Child(Parent):
    def echo(self):
        print('I am from Child class')

p = Parent()
c = Child()
p.echo()
c.echo()
