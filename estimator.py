from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

basic_design = 7
basic_front = 5
basic_back = 6

def get_pages_num():
    pages_num = int(pages_num_g.get())
    return pages_num

def get_amt_design_pages():
    amt_des_pages = int(amt_des_pages_g.get())
    return amt_des_pages

def get_front():
    front = front_g.get()
    if front == 'react':
        front = basic_front
    elif front == 'vuejs':
        front = basic_front * 1.3
    elif front == 'Не будет использоваться':
        front = 0

    return front


def get_back():
    back = back_g.get()
    if back == 'laravel':
        back = basic_back * 1.6
    elif back == 'nodejs':
        back = basic_back / 1.8
    elif back == 'Не будет использоваться':
        back = 0

    return back

def get_dev_rate():
    dev_rate = int(dev_rate_g.get())
    return dev_rate

def get_des_rate():
    des_rate = int(des_rate_g.get())
    return des_rate

def get_qa_rate():
    qa_rate = int(qa_rate_g.get())
    return qa_rate

def get_mng_rate():
    mng_rate = int(mng_rate_g.get())
    return mng_rate

def calc():
    pages_num = get_pages_num()
    amt_des_pages = get_amt_design_pages()
    front = get_front()
    back = get_back()
    res_dev = (front + back) * pages_num
    res_des = basic_design * amt_des_pages
    res_qa = (res_dev / 3) + (res_des / 3)
    res_mng = (res_dev + res_des + res_qa) * 0.3
    final_result = res_dev + res_des + res_qa + res_mng
    min_hrs = round(final_result / 1.3)
    max_hrs = round(final_result * 1.3)

    dev_rate = get_dev_rate()
    dev_money_min = round(res_dev / 1.3) * dev_rate
    dev_money_max = round(res_dev * 1.3) * dev_rate

    des_rate = get_des_rate()
    des_money_min = round(res_des / 1.3) * des_rate
    des_money_max = round(res_des * 1.3) * des_rate

    qa_rate = get_qa_rate()
    qa_money_min = round(res_qa / 1.3) * qa_rate
    qa_money_max = round(res_qa * 1.3) * qa_rate

    mng_rate = get_mng_rate()
    mng_money_min = round(res_mng / 1.3) * mng_rate
    mng_money_max = round(res_mng * 1.3) * mng_rate

    return messagebox.showinfo('Estimation', f"Проект займет от {min_hrs} часов до {max_hrs} часов\n\n"
                                             f"Часы Девелопмента: от {round(res_dev / 1.3)} до {round(res_dev * 1.3)} часов\n\n"
                                             f"Часы Дизайнеров: от {round(res_des / 1.3)} до {round(res_des * 1.3)} часов\n\n"
                                             f"Часы QA: от {round(res_qa / 1.3)} до {round(res_qa * 1.3)} часов\n\n"
                                             f"Часы Менеджмента: от {round(res_mng / 1.3)} до {round(res_mng * 1.3)} часов\n\n"
                                             f"-------------------------------------------------------------------------------\n\n"
                                             f"Стоимость Девелоперов: от {dev_money_min}$ до {dev_money_max}$\n\n"
                                             f"Стоимость Дизайнеров: от {des_money_min}$ до {des_money_max}$\n\n"
                                             f"Стоимость QA: от {qa_money_min}$ до {qa_money_max}$\n\n"
                                             f"Стоимость Менеджмента: от {mng_money_min}$ до {mng_money_max}$\n\n"
                                             f"----------------------------------------------------------------------------\n\n"
                                             f"Общая стоимость проекта: от {dev_money_min + des_money_min + qa_money_min + mng_money_min}$ до "
                                             f"{dev_money_max + des_money_max + qa_money_max + mng_money_max}$")


window = Tk()
window.bind("<Return>", calc)
window.title('Estimator')
window.geometry("400x400")

# Текст слева от инпута с к-вом страниц
pages_num_label = Label(window, text="Сколько ~ планируется страниц?", bd=6,
               font=("Helvetica", 8), pady=5)
pages_num_label.place(x=10, y=20)

# Инпут для к-ва страниц
pages_num_g = Entry(window, bd=3)
pages_num_g.place(x=200, y=27)

# Текст слева от инпута с к-вом страниц для дизайна
amt_design_pages_label = Label(window, text="Для скольких ~ страниц потребуется дизайн?", bd=6,
               font=("Helvetica", 8), pady=5)
amt_design_pages_label.place(x=10, y=50)

# Инпут для к-ва страниц для дизайна
amt_des_pages_g = Entry(window, bd=3)
amt_des_pages_g.place(x=260, y=54)



# Текст слева от инпута с выбором языка для фронта
front_label = Label(window, text="Какой язык будет выбран для front-end?", bd=6,
               font=("Helvetica", 8), pady=5)
front_label.place(x=10, y=80)

# Инпут с выбором языка для фронта
data_front = ("vuejs", "react", "Не будет использоваться")
front_g = Combobox(window, values=data_front)
front_g.place(x=250, y=85)

# Текст слева от инпута с выбором языка для бека
back_label = Label(window, text="Какой язык будет выбран для back-end?", bd=6,
                    font=("Helvetica", 8), pady=5)
back_label.place(x=10, y=110)

# Инпут с выбором языка для бека
data_back = ("laravel", "nodejs", "Не будет использоваться")
back_g = Combobox(window, values=data_back)
back_g.place(x=250, y=120)

# Текст слева от инпута с выбором рейта для девов
dev_rate_label = Label(window, text="Введите рейт Девелоперов на данный проект", bd=6,
                    font=("Helvetica", 8), pady=5)
dev_rate_label.place(x=10, y=150)

# Инпут с выбором рейта для девов
dev_rate_g = Entry(window, bd=3)
dev_rate_g.place(x=270, y=155)

# Текст слева от инпута с выбором рейта для дизайнеров
des_rate_label = Label(window, text="Введите рейт Дизайнеров на данный проект", bd=6,
                    font=("Helvetica", 8), pady=5)
des_rate_label.place(x=10, y=180)

# Инпут с выбором рейта для дизайнеров
des_rate_g = Entry(window, bd=3)
des_rate_g.place(x=270, y=185)

# Текст слева от инпута с выбором рейта для QA
qa_rate_label = Label(window, text="Введите рейт QA на данный проект", bd=6,
                    font=("Helvetica", 8), pady=5)
qa_rate_label.place(x=10, y=220)

# Инпут с выбором рейта для QA
qa_rate_g = Entry(window, bd=3)
qa_rate_g.place(x=230, y=225)

# Текст слева от инпута с выбором рейта для Менеджмента
mng_rate_label = Label(window, text="Введите рейт Менеджеров на данный проект", bd=6,
                    font=("Helvetica", 8), pady=5)
mng_rate_label.place(x=10, y=250)

# Инпут с выбором рейта для Менеджеров
mng_rate_g = Entry(window, bd=3)
mng_rate_g.place(x=260, y=255)

# Кнопка
BUTTON = Button(bg="#000000", fg='#ffffff', bd=3, text="Рассчитать проект", padx=33, pady=10, command=calc,
                    font=("Helvetica", 10, "bold"))
BUTTON.grid(row=5, column=0, sticky=W)
BUTTON.place(x=115, y=300)

window.mainloop()