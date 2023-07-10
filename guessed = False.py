magic_number = False
count = 1
a = 0
b = 1001
 
while not magic_number:
    number = (a + b) // 2
    print("Я думаю это число: ", number)
    answ = input(": ")
    if not answ in ("<", ">", "="):
        print("Нужно отвечать >, <, = ")
        continue
    if answ == "<":
        b = number
    elif answ == ">":
        a = number
    elif answ == "=":
        break
    count += 1
print("Угадал за", count, "попыток")
