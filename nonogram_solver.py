from tkinter import *
from tkinter.font import Font


def configure_window(width=200, height=200):
    """Place tkinter window of set width and height in the center of the display.

    Args:
        width (int, optional): width of the tkinter window. Defaults to 200.
        height (int, optional): height of the tkinter window. Defaults to 200.
    """
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_pos = screen_width // 2 - width // 2
    y_pos = screen_height // 2 - height // 2
    root.geometry("{0}x{1}+{2}+{3}".format(width, height, x_pos, y_pos - 14))  # Substracts 14 from y_pos to account for the height of the window's title bar


def callback(selection):
    """Paint a nonogram puzzle and resize window according to the user selection.
    
    Each difficulty level requires a nonogram with a specific number of rows and columns.
    Furthermore, each difficulty level is different in size (pixels). Thus, this function, when 
    invoked by the OptionMenu widget, will paint a nonogram puzzle with the corresponding number of
    rows and columns for the specified difficulty and resize the tkinter window to fit the puzzle.

    Args:
        selection (str): chosen difficulty
    """
    if selection == "Easy":
        paint_nonogram(6, 6)
        configure_window(270, 270)

    elif selection == "Medium":
        paint_nonogram(11, 11)
        configure_window(420, 420)

    elif selection == "Hard":
        paint_nonogram(16, 16)
        configure_window(570, 570)

    elif selection == "Expert":
        paint_nonogram(21, 21)
        configure_window(720, 720)

    else:
        root.destroy()


def paint_nonogram(rows, columns):
    """Paint nonogram puzzle with the specified number of rows and columns.

    Args:
        rows (int): number of rows
        columns (int): number of columns
    """
    difficulty_menu.grid_remove()
    btn = [[None for i in range(rows)] for j in range(columns)]
    for i in range(rows):
        for j in range(columns):
            if i == 0 and j == 0:
                lbl_frm = Frame(main_frm)
                lbl_frm.pack_propagate(0)

                lbl = Label(lbl_frm)
                
                lbl.place(relx=.5, rely=.5, anchor='c')

            elif i == 0:
                lbl_frm = Frame(main_frm, width=30, height=80, borderwidth=1, relief="solid")
                lbl_frm.pack_propagate(0)

                lbl = Label(lbl_frm, text=(0, 1, 2), font=font, wraplength=16)
                
                lbl.place(relx=.5, rely=.5, anchor='c')

            elif j == 0:
                lbl_frm = Frame(main_frm, width=80, height=30, borderwidth=1, relief="solid")
                lbl_frm.pack_propagate(0)

                lbl = Label(lbl_frm, text=(0, 1, 2), font=font)
                
                lbl.place(relx=.5, rely=.5, anchor='c')

            else:
                lbl_frm = Frame(main_frm, width=30, height=30, borderwidth=1, relief="solid")
                lbl_frm.pack_propagate(0)

                btn[i][j] = Button(lbl_frm, width=18, height=18, image=unchecked_img, command=lambda: change_btn_img(btn[i][j]))
                global state
                state = "unchecked"

                btn[i][j].place(relx=.5, rely=.5, anchor='c')

            lbl_frm.grid(row=i + 1, column=j + 1)


def change_btn_img(btn):
    """Check and uncheck button by changing the button's image.

    Args:
        btn (tk.Button): tkinter button
    """
    global state
    if state == "checked":
        btn.configure(image=unchecked_img)
        state = "unchecked"

    elif state == "unchecked":
        btn.configure(image=checked_img)
        state = "checked"


root = Tk()
root.title("Nonogram Solver")
configure_window()

main_frm = Frame(root)

main_frm.place(relx=.5, rely=.5, anchor='c')

font = Font(family="Courier New")
checked_img = PhotoImage(file="btn_imgs/checked.png")
unchecked_img = PhotoImage(file="btn_imgs/unchecked.png")

difficulty_list = ("Easy", "Medium", "Hard", "Expert", "Exit")
var = StringVar(root)
var.set(difficulty_list[0])
difficulty_menu = OptionMenu(main_frm, var, *difficulty_list, command=callback)

difficulty_menu.grid()

root.mainloop()
