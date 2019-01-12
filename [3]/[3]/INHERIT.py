class Class2:
    class2Attr1 = 0
    def __init__(self):
        pass
    #get & set attr1
    def setAttr1(self,arg1):
        Class2.class2Attr1 = arg1;
    def getAttr1(self):
        return Class2.class2Attr1

class Class3(Class2):#Class3 inherits everything(attributes) from Class2.
    def __init__(self):
        pass
    def func1(self):
        print('Class3.func1()')
class2Var = Class2()
class2Var.setAttr1(1234)
print(class2Var.getAttr1())
class3Var = Class3()
class3Var.func1()
class3Var.setAttr1(4321)
print(class3Var.getAttr1())
