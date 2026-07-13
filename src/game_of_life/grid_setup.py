# grid_setup.py deals with the game states of each generation

# LOGIC:
# first it determines the dimensions of the grid (number of rows, number of columns)
    # -> on initial state it does this
# iterates through rows and columns in which i and j coordinates are placed in a 2D array list
    # -> gets info from compute_next generation after initial state
# determines where the living cell is (need to determine if cell is living, maybe if cell contains something, then it is living)
# send info to display_grid

# NOTE: update logic