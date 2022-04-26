import tkinter as tk
import random
import settings

class Cell:
    all = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cell_frame = None
        self.cell_label = None
        self.is_clicked = False
        self.number = 0

        Cell.all.append(self)
    
    def createCellObject(self, location, i, j):
        cell = tk.Frame(
            location,
            bg = settings.EMPTY_CELL_COLOR,
            width = 50,
            height = 50
        )
        cell.grid(row = i, column = j, padx = 1, pady = 1)

        #Create a thicker border for big grids
        if i == 2 or i == 5:
            cell.grid(row = i, column = j, padx = 1, pady = (1, 2))
        if j == 2 or j == 5:
            cell.grid(row = i, column = j, padx = (1, 2), pady = 1)

        self.cell_label = tk.Label(
            location,
            bg = settings.EMPTY_CELL_COLOR,
            fg = settings.DEFAULT_NUMBER_COLOR
        )
        self.cell_label.grid(row = i, column = j)
        
        #bind left click to both frame and label so it can click the whole square
        self.cell_label.bind("<Button-1>", self.leftClick)
        cell.bind("<Button-1>", self.leftClick)
        
        self.cell_frame = cell
    
    #When a cell is left clicked, player can choose what number that goes in the cell
    def leftClick(self, event):
        self.highlightCells()
        self.checkValidNumber()

    #Highlights the cells accordingly (same grid, same row, same column, same number)
    def highlightCells(self):
        #Unhighlights all cells
        for cell in Cell.all:
            cell.cell_frame.configure(bg = settings.EMPTY_CELL_COLOR)
            cell.cell_label.configure(bg = settings.EMPTY_CELL_COLOR)

        #Highlight the big grids
        #Highlight first nonant
        if self.x in range(0,3) and self.y in range(0,3):
            for cell in Cell.all:
                if cell.x in range(0,3) and cell.y in range(0,3):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight second nonant
        elif self.x in range(0,3) and self.y in range(3,6):
            for cell in Cell.all:
                if cell.x in range(0,3) and cell.y in range(3,6):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight third nonant
        elif self.x in range(0,3) and self.y in range(6,9):
            for cell in Cell.all:
                if cell.x in range(0,3) and cell.y in range(6,9):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight fourth nonant
        elif self.x in range(3,6) and self.y in range(0,3):
            for cell in Cell.all:
                if cell.x in range(3,6) and cell.y in range(0,3):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight fifth nonant
        elif self.x in range(3,6) and self.y in range(3,6):
            for cell in Cell.all:
                if cell.x in range(3,6) and cell.y in range(3,6):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight sixth nonant
        elif self.x in range(3,6) and self.y in range(6,9):
            for cell in Cell.all:
                if cell.x in range(3,6) and cell.y in range(6,9):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight seventh nonant
        elif self.x in range(6,9) and self.y in range(0,3):
            for cell in Cell.all:
                if cell.x in range(6,9) and cell.y in range(0,3):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight eighth nonant
        elif self.x in range(6,9) and self.y in range(3,6):
            for cell in Cell.all:
                if cell.x in range(6,9) and cell.y in range(3,6):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight ninth nonant
        elif self.x in range(6,9) and self.y in range(6,9):
            for cell in Cell.all:
                if cell.x in range(6,9) and cell.y in range(6,9):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        
        #Highlight the same row/column
        for cell in Cell.all:
            if cell.x == self.x:
                cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
            if cell.y == self.y:
                cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)

        #Highlight cells with the same number
        for cell in Cell.all:
            if self.number == cell.number and self.number != 0:
                cell.cell_frame.configure(bg = settings.SAME_NUMBER_CELL_COLOR)
                cell.cell_label.configure(bg = settings.SAME_NUMBER_CELL_COLOR)

        #Highlights clicked cell
        self.cell_frame.configure(bg = settings.SELECTED_CELL_COLOR)
        self.cell_label.configure(bg = settings.SELECTED_CELL_COLOR)

    #Checks if the number that the user put in the cell is valid
    #Highlights red if the same number is in the same row/column
    #That same number also gets highlighted
    def checkValidNumber(self):
        pass

    def updateCell(self, number):
        if number == 0:
            self.cell_label.configure(
                    fg = settings.DEFAULT_NUMBER_COLOR,
                    font = ("", 25),
                    text = ""
                )
        else:
            self.number = number
            self.cell_label.configure(
                    fg = settings.DEFAULT_NUMBER_COLOR,
                    font = ("", 25),
                    text = str(number)
                )