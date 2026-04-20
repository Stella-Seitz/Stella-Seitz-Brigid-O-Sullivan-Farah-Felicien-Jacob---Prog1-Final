import pygame
import sys
from Numbers import Numbers
from Screen import Screen
from sudoku_generator import *


def main():
    #Initilizing Screen and Pygame
    pygame.init()
    game_screen = Screen()
    #Using a state tracker type method
    state = "START"

    sudoku_board = None
    game_numbers = None
    selected_cell = None
    sketched_value = None

    game_screen.StartScreen()

    while True:
        action = game_screen.ButtonEventCheck()

        if state == "START":
            #Allows user to pick difficulty
            if action in ["easy", "medium", "hard"]:
                if action == "easy":
                    cells_to_remove = 30
                elif action == "medium":
                    cells_to_remove = 40
                elif action == "hard":
                    cells_to_remove = 50
                sudoku_board = generate_sudoku(9, cells_to_remove)

                game_numbers = Numbers(sudoku_board, game_screen)

                game_screen.ClearScreen()
                game_screen.GameScreen()
                game_numbers.update_screen()
                #sets a default starting cell
                selected_cell = (0, 0)
                game_numbers.select(0, 0)
                game_screen.displayTempNum( 0, 0, 0)
                state = "PLAYING"


        elif state == "PLAYING":
            #Menu options for restart, exit or reset
            if action in ["Restart", "Exit", "reset"]:
                if action == "Restart":
                    game_screen.ClearScreen()
                    game_screen.StartScreen()
                    state = "START"

                if action == "Exit":
                    pygame.quit()
                    sys.exit()

                if action == "reset":

                    game_screen.ClearScreen()
                    game_screen.GameScreen()
                    game_numbers.reset()

            elif type(action) == tuple:
                selected_cell = action
                sketched_value = None

                game_numbers.select(action[1], action[0])

            #Here I check if the input is a number and if it is in the range to accepted
            elif type(action) == str and action.isdigit() and int(action) in range(1, 10):
                if selected_cell is not None:
                    sketched_value = int(action)
                    col = selected_cell[0]
                    row = selected_cell[1]
                    game_screen.displayTempNum(sketched_value, row, col)

            elif action == "Enter":
                if selected_cell is not None and sketched_value is not None:
                    game_numbers.sketch(sketched_value)
                    sketched_value = None
                    game_screen.ClearScreen()
                    game_screen.GameScreen()
                    game_numbers.update_screen()

                    #Win or lose logic
                    if game_numbers.full_board():
                        game_screen.ClearScreen()

                        if game_numbers.check_board():
                            game_screen.WinningScreen()

                        else:
                            game_screen.LosingScreen()

                        state = "GAME_OVER"
            #Arrow Key movement
            elif action in ["Up", "Down", "Left", "Right"]:
                if selected_cell is not None:
                    col = selected_cell[0]
                    row = selected_cell[1]

                    if action == "Up":
                        new_row = row - 1
                        new_col = col
                    elif action == "Down":
                        new_row = row + 1
                        new_col = col
                    elif action == "Left":
                        new_row = row
                        new_col = col - 1
                    elif action == "Right":
                        new_row = row
                        new_col = col + 1
                    #Boundary
                    if new_col in range(0, 9) and new_row in range(0, 9):
                        selected_cell = (new_col, new_row)
                        game_numbers.select(new_row, new_col)
                        game_screen.ClearScreen()
                        game_screen.GameScreen()
                        game_numbers.update_screen()
                        game_screen.displayTempNum(0, new_row, new_col)
            #Delete option
            elif action == "Delete":
                if selected_cell is not None:
                    sketched_value = None
                    game_numbers.clear_cell()
                    game_screen.ClearScreen()
                    game_screen.GameScreen()
                    game_numbers.update_screen()

        #Gameover state game ends and offers restart or exit
        elif state == "GAME_OVER":

            if action == "Exit":
                pygame.quit()
                sys.exit()

            elif action == "Restart":
                game_screen.ClearScreen()
                game_screen.StartScreen()
                state = "START"


if __name__ == "__main__":
    main()