# neighbour_count.py deals with computing the amount of neighbours for a particular cell

# LOGIC:
# get parameters passed from another function:
    # -> grid, number of rows (num_rows), number of cols (num_cols)
# gather position of neighbours
# create counter, set to 0
# iterate through neighbour positions
    # pull out row / col shifts
    # add to current position to determine neighbour's position relative to grid
    # check if neighbour is in bounds
# compute number of living neighbours from neighbour_pos
    # add to counter += 1 for each living neighbour
# return counter


def compute_live_neighbours(grid, row, col) -> int: # return an int

    # get number of rows and columns for validity check later on
    num_rows = len(grid)
    num_cols = len(grid[0])

    
    neighbour_count = 0

    neighbour_pos = ((-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1))


    return neighbour_count


# grid = [[0,1,1,0,1,0,1,1,1], [0,1,1,1,0,0,0,0,0], [0,0,0,0,1,0,0,1,0]]

# print(grid)


