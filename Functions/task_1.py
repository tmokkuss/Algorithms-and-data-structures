def distance(x_1, x_2, y_1, y_2):
    dist = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5
    return dist


if __name__ == '__main__':
    boole = True
    while boole is True:
        try:
            x_1 = int(input('Введите x1:'))
            x_2 = int(input('Введите x2:'))
            y_1 = int(input('Введите y1:'))
            y_2 = int(input('Введите y2:'))
            print(distance(x_1=x_1, x_2=x_2, y_1=y_1, y_2=y_2))
            boole = False
        except ValueError:
            print("Пожалуйста введите число")
