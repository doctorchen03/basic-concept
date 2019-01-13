
def func1():
    print('test-func1')
def func2():
    _returnVal = 'test-func2'
    return _returnVal
def func3(arg1):
    return arg1
def func4(*arg1):
    return arg1
lambdaVar1 = lambda arg1,arg2: arg1+','+arg2
def func5(arg1,arg2):
    _returnVal = arg1+','+arg2
    return _returnVal
func1();
print(func2())
print(func3('test-func3-arg1'))
print(func3(arg1='test-func3-arg1'))
print(func4(1))
print(func4(1,2,3))
print(func4('1','2','3'))
print(lambdaVar1('arg1','arg2'),func5(arg1='arg1',arg2='arg2'))