
#Имя пользователя
username = input('Напишите ваше имя: ')

#Пользователь вводит заголовки
titles = [
title0 := input('Напишите несколько заголовков, введите первый заголовок: '),   #Ввод заголовков заметки
title1 := input('Ввведите второй заголовок: '),
title2 := input('Ввведите третий заголовок: '),
]

#Примечание к заметкам
content = input('Напишите описание заметки: '),  #Описание заметки
status = input('Введите статус заметки "Выполнено/В работе/В ожидании": '),  #Ввод статуса заметки

#Ввод дат
created_date = input('Введите дату создания заметки "день.месяц.год": '),  #дата создания
temp_created_date = (created_date[:5])
issue_date = input('Введите дату дедлайн  "день.месяц.год": '),    #Дата дедлайна
temp_issue_date =  (issue_date[:5])


all_data = {'Имя пользователя': username, 'Заголовки': titles, 'Описание': content, 'Статус': status,
            'Дата создания': temp_created_date, 'Дата дедлайна': temp_issue_date }

print('Введеные данные: ',  all_data)
#temp_created_date = (created_date[:5]) #Отделяем день и месяц от года
#created_date = datetime.datetime.strptime(created_date, '%d.%m.%y')    #Переводим дату создания заметки из стр в дату
#temp_issue_date =  (issue_date[:5]) #Отделяем день и месяц от года
#issue_date = datetime.datetime.strptime(issue_date, '%d.%m.%y')    #Переводим дату дедлайна заметки из стр в дату


#print('Дата создания: ' ,created_date)    #Вывод для проверки
#print('Дата дедлайна: ' ,issue_date)    #Вывод для проверки
