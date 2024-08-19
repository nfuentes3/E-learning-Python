"""Escriba un programa que guarde en una variable una contraseña y consulte al usuario por la contraseña hasta que esta sea correcta. 
El programa debe informar al usuario si la contraseña fue correcta o no.  """

contraseña = "much4ch0s!" #contraseña inicalizada.

while True:
    usuario = str(input("Indique la contraseña: "))
    if usuario != contraseña:
        print("Has ingresado una contraseña incorrecta, intente nuevamente.\n")
    else:
        print("Contraseña correcta.")
        break