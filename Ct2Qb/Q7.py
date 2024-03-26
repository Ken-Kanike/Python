class Grandparent:
    def display_grandparent(self):
        print("Grandparent class")

class Parent(Grandparent):
    def display_parent(self):
        print("Parent class")

class Child(Parent):
    def display_child(self):
        print("Child class")

# Creating objects
obj_child = Child()

# Accessing methods
obj_child.display_grandparent()
obj_child.display_parent()
obj_child.display_child()