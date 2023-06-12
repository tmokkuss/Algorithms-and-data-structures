def func():
    for num in range(0, 501):
        if num % 7 == 0 and '8' in str(num):
            print(num)


print(func())