import tkinter as tk


def button_click(num):
    print(f"Button {num} clicked")  # Placeholder for button functionality
    temp = num+1
    leftM = True
    for run in range(button_list[num].cget("text")):
        if temp == 12:
            right_mancala.config(text=right_mancala.cget("text")+1)
            temp = 0
            continue
        if temp == 6 and leftM: #if temp is 6 AND left mancala board hasnt been used yet
            left_mancala.config(text=left_mancala.cget("text")+1)
            leftM = False
            continue
        elif temp == 6: #if temp is 6 and it already went
            button_list[temp].config(text=button_list[temp].cget("text") + 1)
            temp+= 1
            leftM = True
            continue
        button_list[temp].config(text=button_list[temp].cget("text")+1)
        temp+=1
    button_list[num].config(text = 0)



def change_turn():
    global user
    user = not user
    unlock_row()

def lock_row():
    for row in button_list:
        for button in row:
            button.config(state="disabled")

def unlock_row():
    for row in button_list:
        for button in row:
            button.config(state="enabled")



game = tk.Tk()
game.title("Mancala")

button_list = []
theboard = ["" for _ in range(14)]  # 14 slots (12 pits + 2 Mancalas)

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

# Run the gamed
game.mainloop()
