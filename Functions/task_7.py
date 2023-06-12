def roman():
    global three
    three = one + two
    print(f"Первое слагаемое: {convert_to_roman(one)}")
    print(f"Второе слагаемое: {convert_to_roman(two)}")
    print(f"Сумма: {convert_to_roman(three)}")


def convert_to_roman(number):
    roman_numerals = {
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_numeral = ''
    for value, symbol in roman_numerals.items():
        while number >= value:
            roman_numeral += symbol
            number -= value

    return roman_numeral


if __name__ == '__main__':
    boole = True
    three = 0
    while boole == True:
        try:
            one = int(input("Введите значение переменной 'one': "))
            two = int(input("Введите значение переменной 'two': "))
            roman()
            boole = False
        except ValueError:
            print(f"Введите пожалуйста правильный формат, поддерживаются только натуральные числа=)")
