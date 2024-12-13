import tkinter as tk

def button_click(num):
    global last_position
    mancalaAdd = True
    temp = num + 1
    seeds = int(button_list[num].cget("text"))
    button_list[num].config(text=0)  # empty the selected pit

    for run in range(seeds):
        # check for right mancala (player 1's mancala)
        if temp == 12:  # right Mancala
            right_mancala.config(text=int(right_mancala.cget("text")) + 1)
            last_position = 12  # update last position
            temp = 0  # go around
            continue

        # check for left mancala (player 2's mancala)
        if temp == 6 and mancalaAdd:  # left Mancala
            left_mancala.config(text=int(left_mancala.cget("text")) + 1)
            last_position = 6  # update last position
            mancalaAdd = False
            continue
        elif temp == 6:
            mancalaAdd = True

        # add seed to regular pits
        button_list[temp].config(text=int(button_list[temp].cget("text")) + 1)
        last_position = temp  # update last position
        temp += 1
        print("next pit will be temp", temp)

    # check if stealing is possible after placing the last seed
    if 0 <= last_position < 6 and user and int(button_list[last_position].cget("text")) == 1:  # player 1's side
        steal_seeds(last_position, is_left_mancala=True)
    elif 6 <= last_position < 12 and not user and int(button_list[last_position].cget("text")) == 1:  # player 2's side
        steal_seeds(last_position, is_left_mancala=False)

    # Check for winner before changing turns
    if check_winner():
        print("Game end!")
        print("Player one had", left_mancala.cget("text"), "!")
        print("Player two had", right_mancala.cget("text"), "!")
        if int(left_mancala.cget("text")) > int(right_mancala.cget("text")):
            win_popup("Player one ")
            print("Player one wins!")
        elif int(right_mancala.cget("text")) > int(left_mancala.cget("text")):
            print("Player two wins!")
            win_popup("Player two ")
        else:
            print("Draw")
            win_popup(3)
        return  # Stop further actions as the game ends

    # Change turn unless the last seed is in a Mancala
    if last_position != 6 and last_position != 12:
        change_turn()
    elif temp == 7:
        change_turn()
    else:
        print("Extra turn granted!")

def check_winner():
    global winPlayer
    isEmpty = True
    for i in range(6):  # Check player 1's side
        if int(button_list[i].cget("text")) != 0:
            isEmpty = False
    if isEmpty:
        return True
    isEmpty = True
    for i in range(7, 12):  # Check player 2's side
        if int(button_list[i].cget("text")) != 0:
            isEmpty = False
    return isEmpty


def steal_seeds(pos, is_left_mancala):
    # stealing logic
    global user
    opposite_pos = 11 - pos  # find the opposite pit
    stolen_seeds = int(button_list[opposite_pos].cget("text"))

    if stolen_seeds > 0:  # steal only if there are seeds
        # Clear the opposite pit and the current pit
        button_list[opposite_pos].config(text=0)
        button_list[pos].config(text=0)

        # Add the seeds to the player's mancala
        if is_left_mancala:  # player 1 (left Mancala)
            left_mancala.config(text=int(left_mancala.cget("text")) + stolen_seeds + 1)
        else:  # player 2 (right Mancala)
            right_mancala.config(text=int(right_mancala.cget("text")) + stolen_seeds + 1)
        print(f"Player {'1' if is_left_mancala else '2'} stole {stolen_seeds} seeds.")

def change_turn():
    global user
    lock_row()  # Lock the current player's row
    user = not user  # Switch to the other player
    unlock_row()  # Unlock the next player's row
    print("Turn changed")

def lock_row():
    if user:
        # print ("one")
        for i in range(6):  # Lock the top row (indices 0 to 5)
            # print ("two")
            button_list[i].config(state="disabled")
    else:
        for i in range(6, 12):  # Lock the bottom row (indices 6 to 11)
            button_list[i].config(state="disabled")

def unlock_row():
    if user:
        # print("one")
        for i in range(6):  # Lock the top row (indices 0 to 5)
            button_list[i].config(state="normal")
    else:
        # print("two")
        for i in range(6, 12):  # Lock the bottom row (indices 6 to 11)
            button_list[i].config(state="normal")

def win_popup(player):
    # Create a new pop-up window
    popup = tk.Toplevel()
    popup.title("Winner")

    # Add a label to the pop-up
    label = tk.Label(popup, text= player + "wins!", font=(24))
    label.pack(padx=40, pady=30)

    close = tk.Button(popup, text="Close", command=popup.destroy, font=(24))
    close.pack(pady=5)

    # restart = tk.Button(popup, text="Restart", command=lambda: [popup.destroy(), restart_game()])
    #restart.pack(pady=10)


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

for i in range(6,12):  # Lock the top row (indices 0 to 5)
    button_list[i].config(state="disabled")

# Run the game
game.mainloop()