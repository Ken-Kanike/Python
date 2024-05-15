'''
#class
class Student:
    rollno = 101
    name = "abc"

#object
obj = Student()
print("Rollno: ",obj.rollno)
print("Name: ",obj.name)


#instance method and self parameter
class Student2:
    rollno = 101
    name = "abc"
    def show_data(self):
        print("Rollno: ",self.rollno)
        print("Name: ",self.name)
obj2 = Student2()
obj2.show_data()

#public ,private and protected members and constructor
class Student3:
    def __init__(self):  #constructor
        self.rollno = 101     #publit
        self.__name = "abc"    #private  _ _
        self._dept = "CO"     #protected _
obj3 = Student3()
print("Rollno: ",obj3.rollno)
try:
    print("Name: ",obj3.__name)
except:
    print("__name connot be accses bec its private ")
print("Department: ",obj3._dept)

#method overloading
class Color:
    def select_color(self,name =None):
        if name is not None:
            print("My favourite color is ",name)
        else:
             print("I dont like any Color")
c1 = Color()
c1.select_color()
c1.select_color("Blue")

#method overrding
class DerivedColor(Color):
    def select_color(self,name =None):
        if name == "Blue":
            print("We both like same color")
c2 = DerivedColor()
c2.select_color("Blue")

#data hiding
# making private or protected data members then trying to access them
class Emp():
    __salary = 10000
    def increment(self):
        self.__salary+=1000
        print("New Salary: ",self.__salary)

e = Emp()
e.increment()
e.increment()
try:
    print(e.__salary) #=> this will cause error
except:
    print("'Emp' object has no attribute '__salary' ")
#correct way tpo access private members
print(e._Emp__salary)

#data abstraction
from abc import ABC,abstractmethod #abc => abstract base class
class Color:
    @abstractmethod
    def showColor(self):
        None

class Red(Color):
    def showColor(self):
        print("This is red color")

class Green(Color):
    def showColor(self):
        print("This is green color")

r = Red()
r.showColor()
g = Green()
g.showColor()

# def main():
#     r = Red()
#     r.showColor()

#     g = Green()
#     g.showColor()

# if __name__ =="__main":
#     main()


#inheritance
#single 
class Parent:
    def callParent(self):
        print("This is Parent class")

class Child(Parent):
    def callChild(self):
        print("This is Child class")

obj = Child()
obj.callParent()
obj.callChild()


#multiple
class Person:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
    def getName(self):
        return self.firstname+ " " +self.lastname
    
class Student(Person):
    def __init__(self,first,last,marks):
        Person.__init__(self,first,last)
        self.studMarks = marks
    def getStudent(self):
        return self.getName()+ " , " +self.studMarks
    
class Teacher(Person):
    def __init__(self,first,last,subject):
        Person.__init__(self,first,last)
        self.subject = subject
    def getTeacher(self):
        return self.getName()+ " , " +self.subject
    
print("The student details are....")
s = Student("AAA","BBB","100")
print("Student name and his/her makrs: ",s.getStudent())
print("--------------------------------------------")
print("The teacher details are....")
t = Teacher("PPP","TTT","Python")
print("Teacher name and subject thaught: ",t.getTeacher())

    
#compostion class......................??
class Marks:
    def __init__(self,th,pr):
        self.th = th
        self.pr = pr
    def calculate_marks(self):
        return (self.th+self.pr)

class Student:
    def __init__(self,rno,name,th,pr):
        self.rno=rno
        self.name=name
        self.th=th
        self.pr=pr
        self.obj_Marks=Marks(self.th,self.pr)  #composition

    def total_marks(self):
        return self.obj_Marks.calculate_marks()
    
s = Student(101,'AAA',70,25)
print("Rollno: ",s.rno)
print("Name: ",s.name)
print("Total marks: ",s.total_marks())

#spelizing inheritance methods?
'''