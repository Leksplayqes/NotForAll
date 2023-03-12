import calendar
import datetime
month = input('Введите номер месяца: ')
month = int(month)

year = datetime.datetime.now().year
day = calendar.monthrange(year, month)
month_name = {
    1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель',
    5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
    9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
print('Месяц - ', month_name.get(month), '\nКолличество дней: ', day[1])
