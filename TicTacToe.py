from tkinter import *  # Importing tkinter package that allows me to create graphs of the GUI
from tkinter import Tk
from tkinter.messagebox import showinfo, askyesno
import warnings

warnings.filterwarnings("ignore")  # removes warnings from the output

root = Tk()  # Creates main window object
root.geometry("500x600")

root.title("Tik-Tak-Toe")  # Gives a title to the main window

cell_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_mark = " "  # move_mark ='X' for player1 and 'O' for player2
turns_played = 0  # what turn is it (the game hav 8 turns in total)
board = ["cell"] * 10  # Creates an array of 10 cells to store where the player played the mark


def results_of_game(board, mark):
    # For horizontal winning
    if (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (
            board[7] == board[8] == board[9] == mark):
        winner = True
    # For vertical winning
    elif (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (
            board[3] == board[6] == board[9] == mark):
        winner = True
    # For diagonal winning
    elif (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark):
        winner = True
    else:
        winner = False
    return winner


def define_sign(current_cell):
    global turns_played, player_mark, cell_numbers, mark
    # Create Dictionary with buttons
    buttons = {
        1: b1,
        2: b2,
        3: b3,
        4: b4,
        5: b5,
        6: b6,
        7: b7,
        8: b8,
        9: b9
    }

    if current_cell in cell_numbers:  # this checks if the cell played it is still available
        cell_numbers.remove(current_cell)  # if so, remove it to prevent override


        # The game will have 8 turns is total (9 cells starting at turn 0)
        if turns_played % 2 == 0:
            player_mark = "X"  # Player 1 will be X and will take every even turn - 0,2,4,6,8 ex. (0%2 = 0)->first turn
            color = "blue"
        else:
            player_mark = "O" # Player 2 will be O and will take every odd turn  -1,3,5,7  ex. (1%2 != 0)->second turn
            color = "green"
        board[current_cell] = player_mark
        buttons[current_cell].config(text=player_mark, fg=color, font="Helvetica")  # config() will write the mark X or O in the current cell place
        turns_played += 1  # increase turns played util reach turn # 8
        mark = player_mark

    if results_of_game(board, mark) and mark == "X":
        showinfo("Alert", "Player 1 wins")
        continue_or_stop()
    elif results_of_game(board, mark) and mark == "O":
        showinfo("Alert", "Player 2 wins")
        continue_or_stop()
    if turns_played > 8 and results_of_game(board, mark) is False:
        showinfo("Alert", "It is a tied")
        continue_or_stop()


def continue_or_stop():
    answer = askyesno(title='confirmation', message='Do you want to continue playing')
    if answer is True:
        reset_game()
    else:
        destroys()


def reset_game():   # Reset game if the player wants to play again
    global cell_numbers, player_mark, turns_played, board
    cell_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_mark = " "
    turns_played = 0
    board = ["cell"] * 10

    # Reset button texts (Removes X and O previously applied)
    for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        button.config(text=" ")


label_player1 = Label(root, text="player 1 : X", font=70)  # create the boxes where players place their X or O
label_player1.grid(row=0, column=1)
label_player2 = Label(root, text="player 2 : O", font=70)
label_player2.grid(row=0, column=2)


def destroys():
    # clears tkinter widgets and destroys them. At the end of the game the window will close
    root.destroy()


# Creating buttons for the 9 cells of the game
b1 = Button(root, width=15, height=10, highlightbackground="#825A9B", command=lambda: define_sign(1))
b1.grid(row=1, column=1)
b2 = Button(root, width=15, height=10, highlightbackground="#825A9B", command=lambda: define_sign(2))
b2.grid(row=1, column=2)
b3 = Button(root, width=15, height=10, highlightbackground="#825A9B", command=lambda: define_sign(3))
b3.grid(row=1, column=3)
b4 = Button(root, width=15, height=10, highlightbackground="#825A9B", command=lambda: define_sign(4))
b4.grid(row=2, column=1)
b5 = Button(root, width=15, height=10, highlightbackground="#825A9B", command=lambda: define_sign(5))
b5.grid(row=2, column=2)
b6 = Button(root, width=15, height=10, highlightbackground="#825A9B", command=lambda: define_sign(6))
b6.grid(row=2, column=3)
b7 = Button(root, width=15, height=10, highlightbackground="#825A9B", command=lambda: define_sign(7))
b7.grid(row=3, column=1)
b8 = Button(root, width=15, height=10, highlightbackground="#825A9B", command=lambda: define_sign(8))
b8.grid(row=3, column=2)
b9 = Button(root, width=15, height=10, highlightbackground="#825A9B", command=lambda: define_sign(9))
b9.grid(row=3, column=3)

root.mainloop()
