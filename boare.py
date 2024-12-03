import tkinter as tk

def button_click(num):
    global last_position
    temp = num + 1
    leftM = True
    seeds = int(button_list[num].cget("text"))
    button_list[num].config(text=0)

    for run in range(seeds):
        if temp == 12:  # right Mancala
            if user:
                right_mancala.config(text=int(right_mancala.cget("text")) + 1)
            last_position = 12  # Update the last position
            temp = 0
            continue

        if temp == 6 and leftM:   #if temp is 6 AND left mancala board hasnt been used yet
            if not user:
                left_mancala.config(text=int(left_mancala.cget("text")) + 1)
            last_position = 6  # update the last position
            leftM = False
            temp += 1
            continue

        button_list[temp].config(text=int(button_list[temp].cget("text")) + 1)
        last_position = temp  # update the last position
        temp += 1

    print("Last seed landed in position: {last_position}")
    if last_position != 6 and last_position != 12:  # Change turn only if last seed is not in a Mancala
        change_turn()
    else:
        print("Extra turn granted!")


def change_turn():
    global user
    lock_row()  # Lock the current player's row
    user = not user  # Switch to the other player
    unlock_row()  # Unlock the next player's row
    print("Turn changed")

def lock_row():
    if user:
        print ("one")
        for i in range(6):  # Lock the top row (indices 0 to 5)
            print ("two")
            button_list[i].config(state="disabled")
    else:
        for i in range(6, 12):  # Lock the bottom row (indices 6 to 11)
            button_list[i].config(state="disabled")

def unlock_row():
    if user:
        print("one")
        for i in range(6):  # Lock the top row (indices 0 to 5)
            button_list[i].config(state="normal")
    else:
        print("two")
        for i in range(6, 12):  # Lock the bottom row (indices 6 to 11)
            button_list[i].config(state="normal")


game = tk.Tk()
game.title("Mancala")

button_list = []
theboard = ["" for _ in range(14)]  # 14 slots (12 pits + 2 Mancalas)

user = True

# Left Mancala Button
left_mancala = tk.Button(game,
                         text=0,
                         font=('Arial', 32),
                         width=6,
                         height=9)
left_mancala.grid(row=0, column=0, rowspan=2, padx=2, pady=2)


for col in range(6):
    button_number = col  # (1-5)
    button = tk.Button(game,
                       text= 4,
                       font=('Arial', 32),
                       width=6,
                       height=3,
                       command=lambda num=button_number: button_click(num))
    button.grid(row=0, column=6-col , padx=2, pady=2)  # Shift by 1 for right Mancala
    button_list.append(button)
for col in range(6):
    button_number = 6 + col # (6 to 11)
    button = tk.Button(game,
                       text= 4,
                       font=('Arial', 32),
                       width=6,
                       height=3,
                       command=lambda num=button_number: button_click(num))
    button.grid(row=1, column=col + 1, padx=2, pady=2)  # Shift by 1 for left Mancala
    button_list.append(button)

# Right Mancala Button
right_mancala = tk.Button(game,
                          text=0,
                          font=('Arial', 32),
                          width=6,
                          height=9)
right_mancala.grid(row=0, column=8, rowspan=2, padx=2, pady=2)
for i in range(6,12):
    button_list[i].config(state="disabled")
# Run the gamed
game.mainloop()
