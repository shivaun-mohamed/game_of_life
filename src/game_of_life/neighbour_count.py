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

    # initialize count
    neighbour_count = 0

    # gather potential positions of neighbour relative to cell
    neighbour_pos = ((-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1))

    # iterate through neighbour positions
    for pos in neighbour_pos:
        row_shift = pos[0]  # row offset value
        col_shift = pos[1]  # col offset value

        # get neighbour position relative to grid
        neighbour = (row_shift + row, col_shift + col)

        # validity check to make sure neighbour is in bounds relative to grid dimensions
        if 0 <= neighbour[0] < num_rows and 0 <= neighbour[1] < num_cols:
            if grid[neighbour[0]][neighbour[1]] == 1:
                neighbour_count += 1 # update count
    
    # return counter
    return neighbour_count


# grid = [[0,1,1,0,1,0,1,1,1], [0,1,1,1,0,0,0,0,0], [0,0,0,0,1,0,0,1,0]]

# print(grid)


