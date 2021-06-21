stroka = input("Введите слово: ")
last_letter = stroka[:-1]
stroka2 = ""
for x in range(0, len(last_letter)):
    if x != 2:
        stroka2 = stroka2 + last_letter[x]
print(stroka2)
if stroka.find("с") >= 0:
    print("Есть с.")
