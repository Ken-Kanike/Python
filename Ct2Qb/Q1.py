class MyClass:
   def __init__(self, value):
     self.value = value
   def display_value(self):
     print("Value:", self.value)
   def update_value(self, new_value):
     self.value = new_value
     print("Value updated to:", self.value)

# Create an object of the class
obj = MyClass(10)

# Call methods on the object
obj.display_value() # Output: Value: 10

# Update the value attribute
obj.update_value(20) # Output: Value updated to: 20

# Call the method again to see the updated value
obj.display_value() # Output: Value: 20
