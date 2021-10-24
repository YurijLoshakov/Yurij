def vegetables():
    veg1 = input("Введите название первого овоща: ")
    veg2 = input("Введите название второго овоща: ")
    veg3 = input("Введите название третьего овоща: ")

    print(veg1.lower(), veg2.lower(), veg3.lower())
    print(veg1.upper(), veg2.upper(), veg3.upper())
    print(veg1.title(), veg2.title(), veg3.title())

    cnt_veg1 = input("Введите количество первого овоща: ")
    cnt_veg2 = input("Введите количество второго овоща: ")
    cnt_veg3 = input("Введите количество третьего овоща: ")

    print(veg1.title() + " в количестве {}".format(cnt_veg1))
    print(veg2.title() + " в количестве {}".format(cnt_veg2))
    print(veg3.title() + " в количестве {}".format(cnt_veg3))
    return 0

vegetables()

