#import datetime #Импорт модуля для использования дат и времени

username = input('Введите имя пользователя: ')   #Ввод имени пользователя
title = input('Напишите заголовок заметки: ')   #Ввод заголовка заметки
content = input('Напишите описание заметки: ')  #Описание заметки
status = input('Введите статус заметки "Готово/В работе/В ожидании":')  #Ввод статуса заметки
created_date = input('Введите дату создания заметки "день.месяц.год": ')    #Дата создания заметки
issue_date = input('Введите дату дедлайн  "день.месяц.год": ')    #дата дедлайна







#created_date = datetime.datetime.strptime(created_date, '%d.%m.%y')    #Переводим дату создания заметки из стр в дату
#issue_date = datetime.datetime.strptime(issue_date, '%d.%m.%y')    #Переводим дату дедлайна заметки из стр в дату
#print('Дата создания: ' ,created_date)    #Вывод для проверки
#print('Дата дедлайна: ' ,issue_date)    #Вывод для проверки

