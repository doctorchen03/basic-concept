class Class1:
    #class variable
    classVar = 0
    #invisible class variable
    __classVar2 = 1
    #constructor
    def __init__(self, attr1Val, attr2Val, attr3Val):
        self.attr1 = attr1Val
        self.attr2 = attr2Val
        self.attr3 = attr3Val
        Class1.classVar = str(0)
    #customize __del__() destructor
    def __del__(self):
        print(self.__class__.__name__, 'destroyed')
    #class functions
    def classFunc1(self):
        print(self.attr1,self.attr2)
    def classFunc2(self):
        returnVal = self.attr1 + ',' + str(self.attr2)
        return returnVal
    def classFunc3(self,arg1):
        returnVal = self.attr1 + ',' + str(arg1)
        return returnVal

class1Var = Class1('val1',1234,True)
print(class1Var.attr1)
print(class1Var.attr2)
print(class1Var.attr3)
print(class1Var.classVar)
#print(class1Var.__classVar2) #Message='Class1' object has no attribute '__classVar2'
class1Var.classFunc1()
print(class1Var.classFunc2())
print(class1Var.classFunc3(4321))
#Built-In Class Attributes
print(Class1.__doc__)
print(Class1.__name__)
print(Class1.__module__)
print(Class1.__bases__)
print(Class1.__dict__)
#destroy object then show message.
del class1Var