def f(a, *args):
    #print(a)
    for arg in args:
        print(arg)
    
f(0, 1, 2, "Manzana")


def f(**kwargs):
    if kwargs is not None:
        for clave, valor in kwargs.items():
            print(f"{clave} --> {valor}")
    
f(nombre = "Anna", edad = 49)