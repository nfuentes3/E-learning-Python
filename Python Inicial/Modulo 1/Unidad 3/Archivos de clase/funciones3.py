def contador_yield(max):
    n = 0
    print("---" * 20 + "1")
    while n < max:
        yield n
        print("---" * 20 + "2")
        n += 1

d = contador_yield(3)
print((d))
print("Ejecucíon de inicio de yield")
print(next(d))
print("Ejecucíon de yield")
print(next(d))
print("Ejecucíon de yield")
print(next(d))