import tkinter as tk


game = tk.Tk()
game.title("Mancala")

button_list = []
theboard = ["" for _ in range(9)]
# row of buttons
for row in range (2):
    # column of buttons
    for col in range(8):
        number = row + 8 +col + 1
        button_number = row * 2 + col   # Calculate button number (1 to 6)
        button = tk.Button(game,
                           text = " ",
                           font = ('Arial', 32),
                           width = 6,
                           height = 3,
                           command = lambda
                            num=button_number: button_click(num))
        button.grid( row = row, column = col, padx =2, pady = 2)
        button_list.append(button)

#run
game.mainloop()