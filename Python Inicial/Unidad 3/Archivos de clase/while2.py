# break
# continue

a = 1
b = 7

while a < b:
    print(a)
    a += 1 #Incremento de valor
    
    if a > 5:
        break
    if a > 2:
        continue
    
    print("---: ", a)