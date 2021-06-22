stroka = input("Введите слово: ")
last_letter = stroka[:-1]
stroka2 = ""
for i in range(0, len(last_letter)):
    if i != 2:
        stroka2 = stroka2 + last_letter[i]
print(stroka2)
if stroka.find("с") >= 0:
    print("Есть с.")
