
import re

def parol():
    while True:
        password = input("Введите пароль: ")
        if len(password) < 8:
            print("Пароль должен быть больше 8 символов")
        elif re.search('[0-9]',password) is None:
            print("Проверьте содержит ли он цифры")
        elif re.search('[A-Z]',password) is None: 
            print("проверьте содержит ли он Заглавные")
        elif re.search('[a-z]',password) is None: 
            print("проверьте содержит ли он Заглавные")
        else:
            print("Пароль подошел")
            break

parol()