def decorador(funcion):
    def envoltura(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        if resultado:
            print("Decorador True")
            return resultado
        else:
            print("Decorador False")
            return resultado
    return envoltura




@decorador
def eleccion(numero):
    try:
        numero = int(numero)
        if numero:
            print("Numero valido", numero)
            return numero
        else:
            print("Numero invalido")
    except Exception as err:
        print("Error:", err)

eleccion(5)
eleccion("Hola")