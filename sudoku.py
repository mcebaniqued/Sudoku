import tkinter as tk
import settings
import random
import copy
from cell import Cell

class Game(tk.Frame):
    matrix = [] #initial matrix of the sudoku
    completed_matrix = []   #completed matrix of sudoku (solution)
    numberList = [1, 2, 3, 4, 5, 6, 7 ,8, 9] #the numbers that go on each cells

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Sudoku")

        self.main_frame = tk.Frame(
            self,
            bg = "#181818",
            width = 600,
            height = 600
        )
        self.main_frame.grid(pady = (50, 50))

        self.make_sudoku()
        self.make_GUI()
        self.mainloop()

    def make_GUI(self):
        for x in range(9):
            for y in range(9):
                c = Cell(x, y, self.matrix[x][y])
                c.createCellObject(self.main_frame, x, y, self.matrix[x][y])
                c.cell_frame.grid(row = x, column = y)
                c.cell_label.grid(row = x, column = y)

    #Remove the numbers of (81-x) number of cells, where x is number of cells based on difficulty
    def make_sudoku(self):
        for _ in range(9):
            self.matrix.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.fill_grid(self.matrix)
        self.completed_matrix = copy.deepcopy(self.matrix)

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
            row = i // 9
            col = i % 9
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

def main():
    root = tk.Tk()
    #root.geometry("600x600")
    root.resizable(False, False)
    Game()

if __name__ == "__main__":
    main()