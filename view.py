from loguru import logger
logger.add("running.log")
def show_menu():
    print('Выберите команду:\n 1 - показать всех сотрудников\n'
        '2 - добавить сотрудника\n 3 - изменить данные сотрудника\n 4 - удалить сотрудника')
    try:
        select = int(input())
        if not select in [1, 2, 3, 4]:
            logger.exception("Ошибка получения данных о пользователя")
            exit(2)
        return select
    except:
        logger.exception('Ошибка в выборе действий')
        exit()
 



def show_employees(spisok):
    
    print('Список всех сотрудников :')   
    for i, sotrudnik in enumerate (spisok):
        if i == 0:
            print(" ", *sotrudnik)
        else:
            print(i, *sotrudnik)    


def add_employees():
    print('Введите Фамилию Имя Телефон Должность через пробел:')
    data=input().split()
    return data


def change_employees():
    try:
        print('Выберите строку для изменений: ')
        change=int(input())
        print('Введите новые данные: ')
        string=input().split()
        return change, string      
    except:
        logger.exception("Ошибка получения данных от пользователя")      

def delete():
    try:
        print('Введите номер строки для удаления данных:  ')
        number = int(input()) 
        return number       
    except:
        logger.exception("Ошибка удаления данных")