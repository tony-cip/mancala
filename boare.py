import tkinter as tk

def button_click(num):
   print(f"Button {num} clicked")  # Placeholder for button functionality



game = tk.Tk()
game.title("Mancala")

button_list = []
theboard = ["" for _ in range(14)]  # 14 slots (12 pits + 2 Mancalas)

# Left Mancala Button
left_mancala = tk.Button(game,
                         text=" ",
                         font=('Arial', 32),
                         width=6,
                         height=9,
                         command=lambda: button_click(-1))
left_mancala.grid(row=0, column=0, rowspan=2, padx=2, pady=2)

#hi nahom

# Pits (6 per row)
for row in range(2):
    for col in range(6):
        button_number = row * 6 + col  # Adjust button number (0 to 11)
        button = tk.Button(game,
                           text="4",
                           font=('Arial', 32),
                           width=6,
                           height=3,
                           command=lambda num=button_number: button_click(num))
        button.grid(row=row, column=col + 1, padx=2, pady=2)  # Shift by 1 for left Mancala
        button_list.append(button)

# Right Mancala Button
right_mancala = tk.Button(game,
                          text=" ",
                          font=('Arial', 32),
                          width=6,
                          height=9,
                          command=lambda: button_click(-2))
right_mancala.grid(row=0, column=8, rowspan=2, padx=2, pady=2)

# Run the gamed
game.mainloop()
