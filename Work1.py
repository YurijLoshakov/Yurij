count = int(input("Введите любое число: "))
pogran = int(input("Введите пограничное число: "))

if count / pogran > 3:
    print("Введенное число больше пограничного более, чем в 3 раза")
elif count > pogran:
    print("Введенное число больше пограничного")
elif count < pogran:
    print("Введенное число меньше пограничного")
