print("1-камень, 2-ножницы, 3-бумага")
Timur = int(input("Введите знак..."))
Ruslan = int(input("Введите знак..."))
if ((Timur==1)and(Ruslan==2)):
    print("Тимур выиграл!")
elif ((Timur==2)and(Ruslan==3)):
    print("Тимур выиграл!")
elif ((Timur==3)and(Ruslan==1)):
    print("Тимур выиграл!")
elif Timur==Ruslan:
    print("Ничья!")
else:
    print("Руслан выиграл!")
