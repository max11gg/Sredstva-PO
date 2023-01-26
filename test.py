Kol = float(input('Количество операций:'))
lchislo = float(input('Первое число:'))

Rezult = 0
Rezult = float(Rezult)
i = 0

while i < Kol:
    llchislo = float(input('Второе число:'))
    Operation = input('Действие:'
'1:+ '
'2:- '
'3:* '
'4:/ ')
    if Operation == "1":
        Rezult = lchislo + llchislo
        i+=1
        lchislo = Rezult
        print(f"Результат:" + str(Rezult))
    elif Operation == "2":
        Rezult = lchislo - llchislo
        i+=1
        lchislo = Rezult
        print(f"Результат:" + str(Rezult))
    elif Operation == "3":
        Rezult = lchislo * llchislo
        i+=1
        print(f"Результат:" + str(Rezult))
    elif (Operation == "4") & (llchislo == 0):
        Rezult = lchislo
        i+=1
        print("Нельзя делить")
    elif Operation == "4": 
        Rezult = lchislo / llchislo
        i+=1
        lchislo = Rezult
        print(f"Результат:" + str(Rezult))
    
