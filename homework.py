"""Написать программу используя функции input() и print().
    Программа запрашивает ввести произвольную строку.
Затем необходимо создать 2 строковые переменные, первая из которых состоит только из чётных символов
введённой строки, а вторая состоит из введённой строки написанной в обратной последовательности,
при этом все буквы должны быть написаны в верхнем регистре.
В качестве результата вывести введённую строку и 2 получившиеся новые строки,
каждую с новой строчки.
"""
stroka = input('ввести произвольную строку: ')
chetn_symbl_stroki = stroka[1::2]
obratn_posled_stroki = stroka[::-1]
print(stroka)
print(chetn_symbl_stroki.upper())
print(obratn_posled_stroki.upper())

