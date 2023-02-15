connect = True

while connect == True:
    number = input('Число: ')
    procent = input('Процент: ')
    while type(number) != float:
        try:
            number = float(number)
            procent = float(procent)

        except ValueError:
            print ('Для получения удовлетворяющего результата надо вводить числа! Попробуй ещё раз.')
            number = input('Число: ')
            print()
            procent = input('Процент: ')
            print()
    

    finish = number/100*procent

    print('Ваш ответ -  ', float(finish))