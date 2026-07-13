# grid_setup.py deals with the game states of each generation

# LOGIC:
# first it determines the dimensions of the grid (number of rows, number of columns)
    # -> on initial state it does this
# iterates through rows and columns in which i and j coordinates are placed in a 2D array list
    # -> gets info from compute_next generation after initial state
# determines where the living cell is (need to determine if cell is living, maybe if cell contains something, then it is living)
# send info to display_grid

# NOTE: update logic

# LOGIC:
# first it generate the dimensions of the grid randomly (num_rows, num_cols)
# create empty 2D array
# iterate through rows and columns and build cells
# for each cell, give 25% mortality rate - alive(1) or dead(0)
# Once row is built, append to empty 2D array
# Once all rows are built, return grid

from random import randint, random

# generate dimensions
num_rows = randint(20,100)
num_cols = randint(20,100)

# create empty 2D array
grid = []

# iterate through rows and columns and build cells
for i in range(num_rows):
    current_row = []
    for j in range(num_cols):
        current_row.append(random())

        if current_row[0] <= 0.25:
            grid.append(1)
        else:
            grid.append(0)

print(grid)            
