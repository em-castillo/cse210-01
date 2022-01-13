'''Week 02: Tic-Tac-Toe Game by Emily Castillo'''

from tkinter import *
from tkinter import messagebox


def create_window():
    '''Creates GUI window'''
    # Create the Tk root object.
    root = Tk()
    # Title
    root.title('Tic-Tac-Toe')
    # Size
    root.geometry('450x300')
    # color
    root.configure(background='#4a7abc')

    # header
    header = Frame(root)
    header.place(x=5, y=5)

    # panel
    panel = Frame(root)
    panel.place(x=30, y=30)


def main():
    create_window()


if __name__ == "__main__":
    main()
