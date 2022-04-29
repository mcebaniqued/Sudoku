from tkinter import *
import settings
import random

class Cell:
    cell_object_list = []

    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.cell_frame = None
        self.cell_label = None
        self.is_editable = False
        self.number = number
        Cell.cell_object_list.append(self)

    def createCellObject(self, location, i, j, number):
        #Frame of each cell
        self.cell_frame = Frame(
            location,
            bg = settings.EMPTY_CELL_COLOR,
            width = 50,
            height = 50,
        )
        #BORDERS
        #Create a thicker border for big grids
        if i == 2 or i == 5:
            self.cell_frame.grid(row = i, column = j, padx = 1, pady = (1, 2))
        elif j == 2 or j == 5:
            self.cell_frame.grid(row = i, column = j, padx = (1, 2), pady = 1)
        else:
            self.cell_frame.grid(row = i, column = j, padx = 1, pady = 1)

        #Label of each cell
        self.cell_label = Label(
            location,
            bg = settings.EMPTY_CELL_COLOR,
            fg = settings.DEFAULT_NUMBER_COLOR,
            font = ("", 25),
            #text = number
        )
        if(self.number == 0):
            self.cell_label.configure(text = "")
            self.is_editable = True
        else:
            self.cell_label.configure(text = str(number))

        self.cell_label.grid(row = i, column = j)

        #BINDS
        self.cell_frame.bind("<Button-1>", self.leftClickCell)
        self.cell_label.bind("<Button-1>", self.leftClickCell)

    def leftClickCell(self, event):
        self.highlightCells()

        if self.is_editable == True:
            #Needed for keyboard bind to work
            self.cell_frame.focus_set()
            self.cell_label.focus_set()

            #BUG: pressing an editable cell, then clicking an uneditable cell, then pressing a number key puts a number on the last editable key clicked
            #Configure frame and labels of each grid
            #For-loop doesn't work idk why
            self.cell_frame.bind("1", lambda event: self.cell_label.configure(text = "1"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.cell_label.bind("1", lambda event: self.cell_label.configure(text = "1"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.number = 1
            self.cell_frame.bind("2", lambda event: self.cell_label.configure(text = "2"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.cell_label.bind("2", lambda event: self.cell_label.configure(text = "2"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.number = 2
            self.cell_frame.bind("3", lambda event: self.cell_label.configure(text = "3"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.cell_label.bind("3", lambda event: self.cell_label.configure(text = "3"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.number = 3
            self.cell_frame.bind("4", lambda event: self.cell_label.configure(text = "4"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.cell_label.bind("4", lambda event: self.cell_label.configure(text = "4"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.number = 4
            self.cell_frame.bind("5", lambda event: self.cell_label.configure(text = "5"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.cell_label.bind("5", lambda event: self.cell_label.configure(text = "5"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.number = 5
            self.cell_frame.bind("6", lambda event: self.cell_label.configure(text = "6"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.cell_label.bind("6", lambda event: self.cell_label.configure(text = "6"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.number = 6
            self.cell_frame.bind("7", lambda event: self.cell_label.configure(text = "7"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.cell_label.bind("7", lambda event: self.cell_label.configure(text = "7"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.number = 7
            self.cell_frame.bind("8", lambda event: self.cell_label.configure(text = "8"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.cell_label.bind("8", lambda event: self.cell_label.configure(text = "8"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.number = 8
            self.cell_frame.bind("9", lambda event: self.cell_label.configure(text = "9"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.cell_label.bind("9", lambda event: self.cell_label.configure(text = "9"), self.cell_label.configure(fg = settings.VALID_NUMBER_COLOR))
            self.number = 9
            self.cell_frame.bind("<BackSpace>", lambda event: self.cell_label.configure(text = ""))
            self.cell_label.bind("<BackSpace>", lambda event: self.cell_label.configure(text = ""))
            self.number = 0
            
        self.isNumberValid()
    
    #Highlights the cells accordingly (same grid, same row, same column, same number)
    def highlightCells(self):
        #Unhighlights all cells
        for cell in self.cell_object_list:
            cell.cell_frame.configure(bg = settings.EMPTY_CELL_COLOR)
            cell.cell_label.configure(bg = settings.EMPTY_CELL_COLOR)

        #Highlight the big grids
        #Highlight first nonant
        if self.x in range(0,3) and self.y in range(0,3):
            for cell in self.cell_object_list:
                if cell.x in range(0,3) and cell.y in range(0,3):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight second nonant
        elif self.x in range(0,3) and self.y in range(3,6):
            for cell in self.cell_object_list:
                if cell.x in range(0,3) and cell.y in range(3,6):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight third nonant
        elif self.x in range(0,3) and self.y in range(6,9):
            for cell in self.cell_object_list:
                if cell.x in range(0,3) and cell.y in range(6,9):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight fourth nonant
        elif self.x in range(3,6) and self.y in range(0,3):
            for cell in self.cell_object_list:
                if cell.x in range(3,6) and cell.y in range(0,3):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight fifth nonant
        elif self.x in range(3,6) and self.y in range(3,6):
            for cell in self.cell_object_list:
                if cell.x in range(3,6) and cell.y in range(3,6):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight sixth nonant
        elif self.x in range(3,6) and self.y in range(6,9):
            for cell in self.cell_object_list:
                if cell.x in range(3,6) and cell.y in range(6,9):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight seventh nonant
        elif self.x in range(6,9) and self.y in range(0,3):
            for cell in self.cell_object_list:
                if cell.x in range(6,9) and cell.y in range(0,3):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight eighth nonant
        elif self.x in range(6,9) and self.y in range(3,6):
            for cell in self.cell_object_list:
                if cell.x in range(6,9) and cell.y in range(3,6):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        #Highlight ninth nonant
        elif self.x in range(6,9) and self.y in range(6,9):
            for cell in self.cell_object_list:
                if cell.x in range(6,9) and cell.y in range(6,9):
                    cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                    cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
        
        #Highlight the same row/column
        for cell in self.cell_object_list:
            if cell.x == self.x:
                cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)
            if cell.y == self.y:
                cell.cell_frame.configure(bg = settings.ADJACENT_CELL_COLOR)
                cell.cell_label.configure(bg = settings.ADJACENT_CELL_COLOR)

        #Highlight cells with the same number
        for cell in self.cell_object_list:
            if self.number == cell.number and self.number != 0:
                cell.cell_frame.configure(bg = settings.SAME_NUMBER_CELL_COLOR)
                cell.cell_label.configure(bg = settings.SAME_NUMBER_CELL_COLOR)

        #Highlights clicked cell
        self.cell_frame.configure(bg = settings.SELECTED_CELL_COLOR)
        self.cell_label.configure(bg = settings.SELECTED_CELL_COLOR)

    def isNumberValid(self, event):
        #BUG: not highlighting properly
        for cell in self.cell_object_list:
            if cell.x == self.x and cell.number == self.number:
                self.cell_frame.configure(bg = settings.INVALID_CELL_COLOR)
                self.cell_label.configure(bg = settings.INVALID_CELL_COLOR)
                self.cell_label.configure(fg = settings.INVALID_NUMBER_COLOR)
            if cell.y == self.y and cell.number == self.number:
                self.cell_frame.configure(bg = settings.INVALID_CELL_COLOR)
                self.cell_label.configure(bg = settings.INVALID_CELL_COLOR)
                self.cell_label.configure(fg = settings.INVALID_NUMBER_COLOR)
        
        #TODO: same nonant
                