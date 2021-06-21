def vegetableLow(name):
    return name.lower()

def vegetableUp(name):
    return name.upper()

def vegetableT(name):
    return name.title()

def sum(count):
    return count

veget1 = input("Первый овощ: ")
veget2 = input("Второй овощ: ")
veget3 = input("Третий овощ: ")

vegets1 = int(input("Сколько " + veget1 + ": "))
vegets2 = int(input("Сколько " + veget2 + ": "))
vegets3 = int(input("Сколько " + veget3 + ": "))

print('{} {}({}, {})'.format(sum(vegets1), vegetableLow(veget1), vegetableUp(veget1), vegetableT(veget1)))
print('{} {}({}, {})'.format(sum(vegets2), vegetableLow(veget2), vegetableUp(veget2), vegetableT(veget2)))
print('{} {}({}, {})'.format(sum(vegets3), vegetableLow(veget3), vegetableUp(veget3), vegetableT(veget3)))