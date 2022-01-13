'''Week 02: Tic-Tac-Toe Game by Emily Castillo'''

from tkinter import *
from tkinter import messagebox
from pygame import mixer


clickable = True
count = 0


def create_window():
    '''Creates GUI window'''
    # Create the Tk root object.
    root = Tk()
    # Title
    root.title('Tic-Tac-Toe')

    # Create buttons
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    btn1 = Button(root, text='', height=5, width=11, fg='#4a7abc',
                  font=('Times New Roman', 18), command=lambda: click(btn1))
    btn2 = Button(root, text='', height=5, width=11, fg='#4a7abc',
                  font=('Times New Roman', 18), command=lambda: click(btn2))
    btn3 = Button(root, text='', height=5, width=11, fg='#4a7abc',
                  font=('Times New Roman', 18), command=lambda: click(btn3))
    btn4 = Button(root, text='', height=5, width=11, fg='#4a7abc',
                  font=('Times New Roman', 18), command=lambda: click(btn4))
    btn5 = Button(root, text='', height=5, width=11, fg='#4a7abc',
                  font=('Times New Roman', 18), command=lambda: click(btn5))
    btn6 = Button(root, text='', height=5, width=11, fg='#4a7abc',
                  font=('Times New Roman', 18), command=lambda: click(btn6))
    btn7 = Button(root, text='', height=5, width=11, fg='#4a7abc',
                  font=('Times New Roman', 18), command=lambda: click(btn7))
    btn8 = Button(root, text='', height=5, width=11, fg='#4a7abc',
                  font=('Times New Roman', 18), command=lambda: click(btn8))
    btn9 = Button(root, text='', height=5, width=11, fg='#4a7abc',
                  font=('Times New Roman', 18), command=lambda: click(btn9))

    # Grid
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=0, column=2)
    btn4.grid(row=1, column=0)
    btn5.grid(row=1, column=1)
    btn6.grid(row=1, column=2)
    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)

    # Start the tkinter loop that processes user events
    root.mainloop()


def click(btn):
    '''Makes buttons clickable'''
    global clickable, count
    # btn.config(text='something') can be type as code bellow
    # Add X
    if btn['text'] == '' and clickable == True:
        btn['text'] = 'X'
        clickable = False
        count += 1
        winner()

    # Add O
    elif btn['text'] == '' and clickable == False:
        btn['text'] = 'O'
        clickable = True
        count += 1
        winner()

    # Box already taken
    else:
        messagebox.showerror('Tic-Tac-Toe', 'Choose an empty box.')


def winner():
    '''Determines winner'''
    win = False

    # X player wins
    if btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'X Player wins!')
    elif btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'X Player wins!')
    elif btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'X Player wins!')

    elif btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'X Player wins!')
    elif btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'X Player wins!')
    elif btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'X Player wins!')

    elif btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'X Player wins!')
    elif btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'X Player wins!')

    # 0 player wins
    elif btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'O Player wins!')
    elif btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'O Player wins!')
    elif btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'O Player wins!')

    elif btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'O Player wins!')
    elif btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'O Player wins!')
    elif btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'O Player wins!')

    elif btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'O Player wins!')
    elif btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', 'O Player wins!')


def main():
    create_window()


if __name__ == "__main__":
    main()
