import view
import model
from loguru import logger
logger.add("running.log")


def main():
    try:
        select=view.show_menu()
        if select == 1:
            sotr = model.get_lists()
            view.show_employees(sotr)
        elif select == 2:
            data = view.add_employees()
            model.add_employees_to_list(data)
        elif select == 3:
            change, string = view.change_employees()
            print(change, string)
            model.update_employees(change, string)
        else:
            number = view.delete()
            model.delete(number)
    except:
        logger.exception('Критическая ошибка контроллера')