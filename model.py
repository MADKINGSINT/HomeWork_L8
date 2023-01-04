import csv
from loguru import logger
logger.add('running.log')

def get_lists():
    try:
        with open ('file.csv' , encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=";",)
            return list(reader)
    except:
        logger.exception("Ошибка поулчения данных")


def add_employees_to_list(employees):
    try:
        with open('file.csv', 'a', encoding="utf-8", newline='',) as csvfile:
            writer=csv.writer(csvfile, delimiter=";")
            writer.writerow(employees)
    except:
        logger.exception("Ошибка в открытии файла в методе добавления данных в файл")
        exit()


def update_employees(number,string):
    try:
        with open('file.csv', 'r', encoding="utf-8", newline='',) as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            data=list(reader)
            print(f'data{data}')
            data[number]=string
        with open('file.csv', 'w', encoding="utf-8", newline='',) as csvfile:
            writer=csv.writer(csvfile, delimiter=";")
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы массива")
        exit()
    # codiga-disable
    except Exception:
        logger.exception("Ошибка в обновлении данных")
        exit()
def delete(number):
    try:
        with open('file.csv', 'r', encoding="utf-8", newline='',) as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            data=list(reader)
            del data[number]
        with open('file.csv', 'w', encoding="utf-8", newline='',) as csvfile:
            writer=csv.writer(csvfile, delimiter=";")
            for i in data:
                writer.writerow(i)              
    except:
        logger.exception("Ошибка удаления данных")