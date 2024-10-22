class OperacionesM():
    def sumar(self,a,b):
        c = a + b
        print("1:", self)
        print(id(self))
        return c

obj = OperacionesM()
print(type(obj))
print("2:",obj)
print(obj.sumar(2,5))
print(id(obj))