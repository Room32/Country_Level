from ttkwidgets.autocomplete import AutocompleteCombobox
import tkinter as tk
from tkinter import *


def read2list(file):
    file = open('countries (ENG).txt', 'r', encoding='utf-8')
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    file.close()
    return lines


def cancel_btn():
    global x, y
    probe = txt.get(f'{y-1}.0', END)
    if '1' in probe:
        x[5] -= 1
        passed_lbl['text'] = f'Passed: {x[5]}'
    elif '2' in probe:
        x[4] -= 1
        stopped_lbl['text'] = f'Stopped: {x[4]}'
    elif '3' in probe:
        x[3] -= 1
        visited_lbl['text'] = f'Visited: {x[3]}'
    elif '4' in probe:
        x[2] -= 1
        stayed_lbl['text'] = f'Stayed: {x[2]}'
    elif '5' in probe:
        x[1] -= 1
        lived_lbl['text'] = f'Lived: {x[1]}'

    y -= 1
    txt.delete(f'{y}.0', END)
    x[0] -= 1
    if x[0] < 0:
        x[0] += 1
    total_countries_lbl['text'] = f'Total countries: {x[0]}'


def ok_btn():
    your_country = []
    ch_country = entry.get()
    your_country.append(ch_country)

    txt.configure(state='normal')
    txt.insert(tk.END, f'{your_country[0]}:')
    new_win = tk.Toplevel(window, bg='#261d2c')
    new_win.geometry('320x320+100+100')
    new_win.resizable(width=FALSE, height=FALSE)

    def btn_5():
        global x, y, totals
        x[0] += 1
        x[1] += 1
        total_countries_lbl['text'] = f'Total countries: {x[0]}'
        lived_lbl['text'] = f'Lived: {x[1]}'
        y += 1
        totals[0] += 5
        txt.configure(state='normal')
        txt.insert(tk.END, ' 5' + '\n')
        new_win.destroy()

    def btn_4():
        global x, y, totals
        x[0] += 1
        x[2] += 1
        total_countries_lbl['text'] = f'Total countries: {x[0]}'
        stayed_lbl['text'] = f'Stayed: {x[2]}'
        y += 1
        totals[1] += 4
        txt.configure(state='normal')
        txt.insert(tk.END, ' 4' + '\n')
        new_win.destroy()

    def btn_3():
        global x, y, totals
        x[0] += 1
        x[3] += 1
        total_countries_lbl['text'] = f'Total countries: {x[0]}'
        visited_lbl['text'] = f'Visited: {x[3]}'
        y += 1
        totals[2] += 3
        txt.configure(state='normal')
        txt.insert(tk.END, ' 3' + '\n')
        new_win.destroy()

    def btn_2():
        global x, y, totals
        x[0] += 1
        x[4] += 1
        total_countries_lbl['text'] = f'Total countries: {x[0]}'
        stopped_lbl['text'] = f'Stopped: {x[4]}'
        y += 1
        totals[3] += 2
        txt.configure(state='normal')
        txt.insert(tk.END, ' 2' + '\n')
        new_win.destroy()

    def btn_1():
        global x, y, totals
        x[0] += 1
        x[5] += 1
        total_countries_lbl['text'] = f'Total countries: {x[0]}'
        passed_lbl['text'] = f'Passed: {x[5]}'
        y += 1
        totals[4] += 1
        txt.configure(state='normal')
        txt.insert(tk.END, ' 1' + '\n')
        new_win.destroy()

    tk.Label(new_win, text='Choose your level:', font=('Calibri', 18, 'bold'), bg='#261d2c', fg='#f7f3ef').pack()
    tk.Button(new_win, bg='red', text='5 Lived Here', font=('Calibri', 18), width=30, command=btn_5).pack(
        anchor='w', pady=3)
    tk.Button(new_win, bg='DarkOrange1', text='4 Stayed Here', font=('Calibri', 18), width=30, command=btn_4).pack(
        anchor='w', pady=3)
    tk.Button(new_win, bg='gold', text='3 Visited Here', font=('Calibri', 18), width=30, command=btn_3).pack(
        anchor='w', pady=3)
    tk.Button(new_win, bg='spring green', text='2 Stopped Here', font=('Calibri', 18), width=30, command=btn_2).pack(
        anchor='w', pady=3)
    tk.Button(new_win, bg='purple1', text='1 Passed Here', font=('Calibri', 18), width=30, command=btn_1).pack(
        anchor='w', pady=3)


def finish_btn():
    finish_win = tk.Toplevel(window, bg='#261d2c')
    finish_win.geometry('381x420+100+100')
    finish_win.resizable(width=FALSE, height=FALSE)

    def save_btn():
        with open('RESULTS.txt', 'w') as file:
            file.write(f'Lived Here (5pts):  {totals[0]}' + '\n' +
                       f'Stayed Here (4pts):  {totals[1]}' + '\n' +
                       f'Visited Here (3pts):  {totals[2]}' + '\n' +
                       f'Stopped Here (2pts):  {totals[3]}' + '\n' +
                       f'Passed Here (1pt):  {totals[4]}' + '\n' +
                       f'TOTAL: {sum(totals)}')

    tk.Label(finish_win, text=f'Lived Here (5pts):  {totals[0]}', font=('Calibri', 18), bg='red', width=31,
             height=2).grid(row=0)
    tk.Label(finish_win, text=f'Stayed Here (4pts):  {totals[1]}', font=('Calibri', 18), bg='DarkOrange1', width=31,
             height=2).grid(row=1)
    tk.Label(finish_win, text=f'Visited Here (3pts):  {totals[2]}', font=('Calibri', 18), bg='gold', width=31,
             height=2).grid(row=2)
    tk.Label(finish_win, text=f'Stopped Here (2pts):  {totals[3]}', font=('Calibri', 18), bg='spring green', width=31,
             height=2).grid(row=3)
    tk.Label(finish_win, text=f'Passed Here (1pt):  {totals[4]}', font=('Calibri', 18), bg='purple1', width=31,
             height=2).grid(row=4)
    tk.Label(finish_win, text=f'TOTAL: {sum(totals)}', font=('Calibri', 18, 'bold'), bg='#261d2c', fg='#f7f3ef',
             width=29, height=2).grid(row=5)
    tk.Button(finish_win, text='Save to file as RESULTS.txt', command=save_btn).grid(row=6)


y = 1
x = [0, 0, 0, 0, 0, 0]
totals = [0, 0, 0, 0, 0]

window = tk.Tk()
window.title('Country level')
window.iconbitmap(default='globe.ico')
window.geometry('600x400+200+200')
window['bg'] = '#261d2c'
window.resizable(width=FALSE, height=FALSE)
label = tk.Label(text='Country', font=('Calibri', 10, 'bold'), bg='#392f3c', fg='#f7f7ef', width=19, height=2)
entry = AutocompleteCombobox(width=15, height=20, font=('Calibri', 12), completevalues=read2list('countries (ENG).txt'))
txt = tk.Text(height=10, width=30, font=('Calibri', 18), bg='#362f3f', fg='#f7f3ef', state='disabled')
button = tk.Button(text='OK', font=('Calibri', 12, 'bold'), width=4, command=ok_btn, bg='#52aec6', fg='#f7f3ef')
cancel_btn = tk.Button(text='Cancel', font=('Calibri', 12), width=4, command=cancel_btn, bg='#39313f', fg='#f7f3ef')
total_countries_lbl = tk.Label(text=f'Total countries: {x[0]}', font=('Calibri', 12,'bold'), bg='#362f3f', fg='#f7f3ef')
lived_lbl = tk.Label(text=f'Lived: {x[0]}', font=('Calibri', 12, 'bold'), bg='#362f3f', fg='#f7f3ef')
stayed_lbl = tk.Label(text=f'Stayed: {x[0]}', font=('Calibri', 12, 'bold'), bg='#362f3f', fg='#f7f3ef')
visited_lbl = tk.Label(text=f'Visited: {x[0]}', font=('Calibri', 12, 'bold'), bg='#362f3f', fg='#f7f3ef')
stopped_lbl = tk.Label(text=f'Stopped: {x[0]}', font=('Calibri', 12, 'bold'), bg='#362f3f', fg='#f7f3ef')
passed_lbl = tk.Label(text=f'Passed: {x[0]}', font=('Calibri', 12, 'bold'), bg='#362f3f', fg='#f7f3ef')
finish_btn = tk.Button(text='FINISH', font=('Calibri', 12, 'bold'), relief=RIDGE, width=44, bg='#52aec6', fg='#f7f3ef',
                       command=finish_btn)

label.grid(row=0, column=0)
entry.grid(row=1, column=0, sticky='n', pady=5)
button.grid(row=1, column=1, sticky='n', ipadx=10, padx=10)
txt.grid(row=1, rowspan=8, column=2, sticky='n')
cancel_btn.grid(row=2, column=1, sticky='n', ipadx=10, padx=10)
total_countries_lbl.grid(row=3, column=0, sticky='w')
lived_lbl.grid(row=4, column=0, sticky='w')
stayed_lbl.grid(row=5, column=0, sticky='w')
visited_lbl.grid(row=6, column=0, sticky='w')
stopped_lbl.grid(row=7, column=0, sticky='w')
passed_lbl.grid(row=8, column=0, sticky='w')
finish_btn.grid(row=9, column=1, columnspan=2, sticky='se', pady=10)
window.mainloop()
