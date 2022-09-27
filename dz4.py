# калькулятор


def coordinates(a, b, c):
    if (b == "/" or b == "mod" or b == "div") and z == 0:
        print("Деление на 0!")
    elif b == "*":
        print (a*c)
    elif b == "mod" and b!=0:
        print(a % c)
    elif b == "+":
        print(a+c)
    elif b == "-":
        print(a-c)
    elif b == "pow":
        print(a ** c)
    elif b == "div" and b!=0:
        print(a // c)
    elif b == "/" and b!=0:
        print(a/c)
    # else:
    #     print("Деление на 0!")
try:
    x = float(input("Введите число: "))
    y = input("Введите действие (+, -, /, *, mod, pow, div): ")
    z = float(input("Введите число: "))
    
    coordinates(x, y, z)
except:
    print("Что-то пошло не так")