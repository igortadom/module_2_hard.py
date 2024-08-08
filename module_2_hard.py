number = int(input('Введите число от 3 до 20: '))

if number < 3 or number > 20:
     print('Ошибка')
else:
    def get_password(number):
        password = ''
        for i in range(1, 21):
            for j in range(i + 1, 21):
                if number % (i +j) == 0:
                    password += str(i) + str(j)
        return password

    print(get_password(number))