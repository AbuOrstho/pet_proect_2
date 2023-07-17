from mtranslate import translate  # Библиотека для перевода(имеет ограничение)
import tkinter as tk  # Библиотека для отрисовки окон
from tkinter.ttk import Combobox  # Виджет Combobox

lan = {'Английский': 'en',
       'Испанский': 'es',
       'Французский': 'fr',
       'Немецкий': 'de',
       'Итальянский': 'it',
       'Португальский': 'pt',
       'Китайский (упрощенный)': 'zh-CN',
       'Японский': 'ja',
       'Корейский': 'ko',
       'Русский': 'ru',
       'Арабский': 'ar',
       'Турецкий': 'tr',
       'Вьетнамский': 'vi',
       'Тайский': 'th',
       'Греческий': 'el',
       'Иврит': 'he',
       'Шведский': 'sv',
       'Нидерландский': 'nl',
       'Датский': 'da',
       'Норвежский': 'no',
       'Финский': 'fi',
       'Польский': 'pl',
       'Украинский': 'uk',
       'Чешский': 'cs',
       'Венгерский': 'hu',
       'Туркменский': 'tk'}  # Список содержащий в себе языки и их сокращения для библиотеки mtranslate


def transl():  # Функция для перевода и вывода текста в виджете output
    lang = combo.get()  # Переменная, которая хранит выбранный язык
    inp = input_block.get("1.0", tk.END)  # Текст, который нужно перевести
    trans = translate(inp, lan[lang])  # Перевод текста
    output_block.delete('1.0', tk.END)  # Удаление прошлого вывода
    output_block.insert(tk.END, '\n' + trans)  # Вывод нового текста


window = tk.Tk()  # Создание окна
window.title('Переводчик')  # Титульная надпись
window.configure(bg='#202020')  # Цвет заднего фона окна
ob = tk.Frame(window, bg='#202020')  # Фрайм в который помещены все виджеты
ob.pack()

input_block = tk.Text(master=ob, width=30, height=10, font=('Times New Roman', 13), bg='#4E5754', fg='#ffffff')
input_block.grid(row=0, column=0, padx=4, pady=1)  # Виджет для ввода текста

output_block = tk.Text(master=ob, width=30, height=10, font=('Times New Roman', 13), bg='#4E5754', fg='#ffffff')
output_block.grid(row=0, column=1, padx=4, pady=3)  # Виджет для вывода текста

combo = Combobox(master=ob, width=13)  # Виджет Combobox со списком языком
combo['values'] = ('Английский', 'Испанский', 'Французский', 'Немецкий', 'Итальянский', 'Португальский',
                   'Китайский (упрощенный)', 'Японский', 'Корейский', 'Русский', 'Арабский', 'Турецкий',
                   'Вьетнамский', 'Тайский', 'Греческий', 'Иврит', 'Шведский', 'Нидерландский', 'Датский',
                   'Норвежский', 'Финский', 'Польский', 'Украинский', 'Чешский', 'Венгерский',
                   'Туркменский')  # Список языком для Combobox
combo.current(0)  # Язык который бывает установлен по умолчанию в Combobox
combo.place(x=459, y=3)  # Координаты Combobox

button = tk.Button(width=8, height=2, bg='#76b9ed', fg='#213442', font=('Times New Roman', 13), text='Перевод',
                   command=transl)  # Создание кнопки
button.pack()  # Вывод кнопки

window.mainloop()  # Отображения окна и запуск всех циклов действий
