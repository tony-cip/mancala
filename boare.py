import tkinter as tk

def button_click(num):
    print(f"Button {num} clicked")  # Placeholder for button functionality
    temp = num + 1
    leftM = True
    for run in range(button_list[0 if num < 6 else 1][num % 6].cget("text")):
        if temp == 12:
            right_mancala.config(text=right_mancala.cget("text") + 1)
            temp = 0
            continue
        if temp == 6 and leftM:  # if temp is 6 AND left mancala board hasn't been used yet
            left_mancala.config(text=left_mancala.cget("text") + 1)
            leftM = False
            continue
        elif temp == 6:  # if temp is 6 and it already went
            button_list[0][temp % 6].config(text=button_list[0][temp % 6].cget("text") + 1)
            temp += 1
            leftM = True
            continue
        button_list[0 if temp < 6 else 1][temp % 6].config(text=button_list[0 if temp < 6 else 1][temp % 6].cget("text") + 1)
        temp += 1
    button_list[0 if num < 6 else 1][num % 6].config(text=0)

def lock_row(row):
    #Lock a specific row of buttons."""
    for button in button_list[row]:
        button.config(state="disabled")

def unlock_row(row):
    #Unlock a specific row of buttons
    for button in button_list[row]:
        button.config(state="normal")

# Initialize the game window
game = tk.Tk()
game.title("Mancala")

# Variables
button_list = [[], []]  # 2D list for buttons (2 rows for the board)

# Left Mancala Button
left_mancala = tk.Button(game,
                         text=0,
                         font=('Arial', 32),
                         width=6,
                         height=9)
left_mancala.grid(row=0, column=0, rowspan=2, padx=2, pady=2)

# Row 0 (Player 0's side)
for col in range(6):
    button_number = col
    button = tk.Button(game,
                       text=4,
                       font=('Arial', 32),
                       width=6,
                       height=3,
                       command=lambda num=button_number: button_click(num))
    button.grid(row=0, column=6 - col, padx=2, pady=2)
    button_list[0].append(button)

# Row 1 (Player 1's side)
for col in range(6):
    button_number = col + 6
    button = tk.Button(game,
                       text=4,
                       font=('Arial', 32),
                       width=6,
                       height=3,
                       command=lambda num=button_number: button_click(num))
    button.grid(row=1, column=col + 1, padx=2, pady=2)
    button_list[1].append(button)

# Right Mancala Button
right_mancala = tk.Button(game,
                          text=0,
                          font=('Arial', 32),
                          width=6,
                          height=9)
right_mancala.grid(row=0, column=8, rowspan=2, padx=2, pady=2)

# Lock Player 1's row initially
lock_row(0)

# Run the game
game.mainloop()
