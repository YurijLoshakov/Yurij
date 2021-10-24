string = input("Введите строку: ")
outString = ""
count = 0

for i in range (0, len(string)):
    if i == 2:
        continue
    elif i == len(string) - 1:
        continue
    elif string[i] == "c" or string[i] == "с" \
            or string[i] == "C" or string[i] == "С":
        count += 1
    outString += string[i]

if count >= 1:
    print("Присутствует символ 'c'!")

print("Строка со всеми изменениями: ", outString)



