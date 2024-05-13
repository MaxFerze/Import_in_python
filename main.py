from aplication.salary import calculate_salary
from aplication.db.people import get_employees
from datetime import datetime

x = 1
if __name__ == '__main__':
    print(f'started in {datetime.now()}')

    while x == 1:
        y = input("1 = ЗП. 2 = Все. 3 = Пока.")
        if y == '1':
            calculate_salary()
        elif y == '2':
            get_employees()
        elif y == '3':
            break
        else:
            print('Попробуй еще раз')