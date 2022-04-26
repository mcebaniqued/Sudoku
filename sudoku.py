import tkinter as tk
import random
import settings
from cell import Cell

class Game(tk.Frame):
    cells = []
    matrix = []
    number_input = []
    numberList=[1,2,3,4,5,6,7,8,9]

    def __init__(self):
        #Initiate window
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Sudoku")

        self.main_grid = tk.Frame(
            self,
            bg = settings.GAME_COLOR,
            bd = 2,
        )
        self.main_grid.grid(pady = (50, 50)) #offset of 100 pixels from the top (this is where we put the score, buttons, etc)

        for _ in range(9):
            self.matrix.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        
        self.make_GUI()
        self.start_game()
        self.update_GUI()
        self.mainloop()
    
    #Makes the the grid of the game by using frames and labels
    def make_GUI(self):
        #Make the 9x9 grid
        for i in range(9):
            row = []
            for j in range(9):
                c = Cell(i,j)
                c.createCellObject(self.main_grid, i, j)
                row.append(c)
            self.cells.append(row)

        #Make the timer frame and label on top
        time_frame = tk.Frame(self)
        time_frame.place(relx = 0.9, y = 25, anchor = "center")
        self.time_label = tk.Label(
            time_frame,
            text = "00:00",
            font = ("", 20)
        )
        self.time_label.grid(row = 0)

        #TODO:
        #Make the number frame and label at the bottom
        number_frame = tk.Frame(self,
            bg = "#b7cee5",
        )
        number_frame.place(relx = 0.5, rely = .957, anchor = "center")
        for i in range(1,10):
            number_label = tk.Label(
                number_frame,
                bg = "#b7cee5",
                fg = settings.DEFAULT_NUMBER_COLOR,
                font = ("", 25),
                text = str(i),
            )
            number_label.grid(row = 0, column = i, padx=14)
            self.number_input.append(number_label)
    
    #Remove the numbers of (81-x) number of cells, where x is number of cells based on difficulty
    def start_game(self):
        self.fill_grid(self.matrix)

        diff = settings.DIFFICULTY[1]
        for _ in range(81-random.choice(diff)):
            row = random.randint(0,8)
            col = random.randint(0,8)
            while(self.matrix[row][col] == 0):
                row = random.randint(0,8)
                col = random.randint(0,8)
            self.matrix[row][col] = 0

    #Randomly populate the grid with a completed game
    def fill_grid(self, grid):
        #Algorithm from https://www.101computing.net/sudoku-generator-algorithm/
        for i in range(0,81):
            row=i//9
            col=i%9
            if grid[row][col]==0:
                random.shuffle(self.numberList)      
                for value in self.numberList:
                    #Check that this value has not already be used on this row
                    if not(value in grid[row]):
                        #Check that this value has not already be used on this column
                        if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                            #Identify which of the 9 squares we are working on
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[grid[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[grid[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[grid[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[grid[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[grid[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[grid[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[grid[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[grid[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[grid[i][6:9] for i in range(6,9)]
                            #Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                grid[row][col]=value
                                if self.checkGrid(grid):
                                    return True
                                else:
                                    if self.fill_grid(grid):
                                        return True
                break
        grid[row][col] = 0

    #A function to check if the grid is full
    def checkGrid(self, grid):
        for row in range(0,9):
            for col in range(0,9):
                if grid[row][col]==0:
                    return False

        #We have a complete grid!  
        return True 

    #Updates the GUI
    #TODO: check for valid/invalid inputs and change the colors of numbers/cell accordingly
    def update_GUI(self):
        for i in range(9):
            for j in range(9):
                Cell.updateCell(self.cells[i][j], self.matrix[i][j])
        
def main():
    root = tk.Tk()
    #root.resizable(False, False)
    Game()

if __name__ == "__main__":
    main()