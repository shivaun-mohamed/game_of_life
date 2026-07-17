# grid_setup.py deals with the game states of each generation

# LOGIC:
# first it generate the dimensions of the grid randomly (num_rows, num_cols)
# create empty 2D array
# iterate through rows and columns and build cells
# for each cell, give 25% mortality rate - alive(1) or dead(0)
# Once row is built, append to empty 2D array
# Once all rows are built, return grid

from random import randint, random

def create_grid():
    
    # generate dimensions
    num_rows = randint(20,100)
    num_cols = randint(20,100)

    # create empty 2D array to hold grid
    grid = []

    # iterate through rows and columns and build cells
    for i in range(num_rows):

        # build array to hold current row
        current_row = []
        for j in range(num_cols):
            
            # random float between 0 and 1
            mortality = random()

            # add mortality value to current row for 25% mortality rate
            if mortality <= 0.25:
                current_row.append(1)
            else:
                current_row.append(0)

        # add current row to grid
        grid.append(current_row)

    # return grid
    return grid
    