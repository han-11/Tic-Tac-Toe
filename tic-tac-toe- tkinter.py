from tkinter import *
from tkinter import messagebox


window = Tk()
window.title('Tic-Tac-Toe')

clicked = True
count = 0


# Disable all buttons

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# Check win

def check_win():
    global winner
    winner = False

    if b1["text"] == b2["text"] == b3["text"] and b1["text"] != " ":
        b1.config(bg="green")
        b1.config(bg="green")
        b1.config(bg="green")
        winner = True
        messagebox.showinfo(
            "Tic Tac Toe", f"Congratulations, winner is {b1['text']}.")
        disable_all_buttons()

    elif b4["text"] == b5["text"] == b6["text"] and b4["text"] != " ":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo(
            "Tic Tac Toe", f"Congratulations, winner is {b4['text']}.")
        disable_all_buttons()

    elif b7["text"] == b8["text"] == b9["text"] and b7["text"] != " ":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo(
            "Tic Tac Toe", f"Congratulations, winner is {b7['text']}.")
        disable_all_buttons()

    elif b1["text"] == b4["text"] == b7["text"] and b1["text"] != " ":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo(
            "Tic Tac Toe", f"Congratulations, winner is {b1['text']}.")
        disable_all_buttons()

    elif b2["text"] == b5["text"] == b8["text"] and b2["text"] != " ":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo(
            "Tic Tac Toe", f"Congratulations, winner is {b2['text']}.")
        disable_all_buttons()

    elif b3["text"] == b6["text"] == b9["text"] and b3["text"] != " ":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo(
            "Tic Tac Toe", f"Congratulations, winner is {b3['text']}.")
        disable_all_buttons()

    elif b1["text"] == b5["text"] == b9["text"] and b1["text"] != " ":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo(
            "Tic Tac Toe", f"Congratulations, winner is {b1['text']}.")
        disable_all_buttons()

    elif b3["text"] == b5["text"] == b7["text"] and b3["text"] != " ":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo(
            "Tic Tac Toe", f"Congratulations, winner is {b3['text']}.")
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        disable_all_buttons()


# Button clicked command


def button_click(button):
    global clicked, count

    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        check_win()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        check_win()
    else:
        messagebox.showerror(
            "Tic Tac Toe", "That button has already been clicked,\n please click another button that unclicked ")


# Create reset button
def game_reset():

    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = False
    count = 0

    # create 9 buttons
    b1 = Button(window, text=" ", font=('Arial', 20), height=5,
                width=6, bg='grey', command=lambda: button_click(b1))
    b2 = Button(window, text=" ", font=('Arial', 20), height=5,
                width=6, bg='grey', command=lambda: button_click(b2))
    b3 = Button(window, text=" ", font=('Arial', 20), height=5,
                width=6, bg='grey', command=lambda: button_click(b3))

    b4 = Button(window, text=" ", font=('Arial', 20), height=5,
                width=6, bg='grey', command=lambda: button_click(b4))
    b5 = Button(window, text=" ", font=('Arial', 20), height=5,
                width=6, bg='grey', command=lambda: button_click(b5))
    b6 = Button(window, text=" ", font=('Arial', 20), height=5,
                width=6, bg='grey', command=lambda: button_click(b6))

    b7 = Button(window, text=" ", font=('Arial', 20), height=5,
                width=6, bg='grey', command=lambda: button_click(b7))
    b8 = Button(window, text=" ", font=('Arial', 20), height=5,
                width=6, bg='grey', command=lambda: button_click(b8))
    b9 = Button(window, text=" ", font=('Arial', 20), height=5,
                width=6, bg='grey', command=lambda: button_click(b9))

    # grid the window
    b1.grid(column=0, row=0)
    b2.grid(column=1, row=0)
    b3.grid(column=2, row=0)

    b4.grid(column=0, row=1)
    b5.grid(column=1, row=1)
    b6.grid(column=2, row=1)

    b7.grid(column=0, row=2)
    b8.grid(column=1, row=2)
    b9.grid(column=2, row=2)


# reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
# reset_button.pack(side="top")


# Create menu
tk_menu = Menu(window)
window.config(menu=tk_menu)

# create options
options = Menu(tk_menu, tearoff=False)
tk_menu.add_cascade(label="Options", menu=options)
options.add_command(label="Reset Game", command=game_reset)


game_reset()

window.mainloop()
