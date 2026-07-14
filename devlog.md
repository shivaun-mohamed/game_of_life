# DevLog

Entries organized by decision and date

## Project Purpose (2026-07-08)

Because most of my programming skill and experiences are based off of what I have learned in class, I have decided to build an interesting beginner project that I can work on by myself and learn more about project design, debugging, structuring logic, and making my projects more professional looking. I just finished my first year of Computer Science and felt that Conway's Game of Life would be an interesting, simple, and fun beginner project to work on as it is unique in the fact that it is a zero player game. The game also has state representation, logic updates, and rendering. 

## Grid Representation: 2D List vs Coordinate Set (Incomplete Code) (2026-07-08)

I considered two ways to represent the game board:
- A 2D list, every cell (dead or alive) has a slot
- A set of only the live cell coordinates

Initially, I considered combining both but decided against it because information would overlap between both data structures and it would make it too overly complicated. I decided to go with the 2D list so that it would be easier to lookup neighbours by index regardless if they are dead or alive. Maybe later will change to a set of only the live cell coordinates as it may be memory efficient for boards with less live cells. 

## Board Size and Seeding (Incomplete Code) (2026-07-08)

Rows and columns are randomly chosen independently between 20 and 100 (game board not forced to be square). This makes it more interesting than just having a fixed square game board and it still makes it small enough for the board to fit inside the terminal. Initial cells are seeded with a 25% independent chance of being alive when starting out. I chose this to control the population density so there are fewer cases of instant death from the 1st to 2nd generation and less overcrowding as well.

## Old Grid vs New Grid (2026-07-08)

I can not update the current grid while computing the next generation. This is because some cells check already updated neighbours (N+1 generation) while others check pre-updated neighbours (Nth generation), this depending on loop order. So the next generation would be an inaccurate representation based on the rules of the game. 

To solve this, there will be a compute next generation function that takes the old grid (Nth geneation) as input and outputs the new grid (N+1 generation). Once the new grid is fully built, the old grid is discarded.

## Neighbour Counting as a Function (2026-07-08)

Decided to separate "count live neighbours for a given cell" into its own function to make it more independent and easier to test instead of just embedding it into the compute next generation logic. 

Signature: takes (grid, row, column) -> returns an integer (0-8)
- 8 because the most squares and therefore the most live neighbours a cell can have around it is 8

### Handling Corners and Edges (2026-07-08)

A middle cell has 8 neighbours, edge cells have 5, and corner cells have 3. Instead of just writing exceptions for edges and corner cells, there will be a check to see if the cell is within a certain row and column (i.e., an edge cell can be in the (0th or size - ith) row or (0th or jth - 1) column).

## Error: README.md not rendering properly (2026-07-08)

As this is my first time really using markdown language, my README was initially not rendering properly. For example, the formatting on the subheadings were not working as intended and my README text would show up as normal text when previewed. I later discovered that this was due to all of my lines being indented. Markdown was treating the text as a code block due to the leading whitespace

## Project Structure (2026-07-13)

Was deciding on a flat vs src/-package layout. Ultimately decided to use the src/-package layout as it made things look more professional. In addition, it allowed for proper imports to work and I decided to use this to gain practice for my future projects. I plan to continue this for my other projects as well. 

### Files Created:

- __init__.py
- compute_next_generation.py
- display_grid.py
- grid_setup.py
- main.py
- neighbour_count.py
- devlog.md
- pyproject.toml
- README.md

## grid_setup.py - Complete (2026-07-13)

Finally finished grid_setup.py. Initially ran into issues understanding nested loops and the random module. Also had trouble understanding the logic sequence. My original plan was to iterate through each cell and assign it a value of 1 (alive) or 0 (dead). Unfortunately I had no clue how to do this while considering the 25% mortality rate of the cell. I was also appending the wrong information to the wrong data structure. My grid would output the floating point numbers of the random float between 0 and 1 rather than just 0 and 1. I did not compare the values to 0.25 first. I also was checking the wrong parameter (current_row(0)) instead of the new value for each loop. 

I fixed this while spending some time away from coding for the remainder of the day. When I realized I should set the mortality rate as another variable and then give it a special casing to determine the cell's mortality, then I started to understand the logic. 

I learned more about nested loops and data containers through this function. I also wrapped the logic into the create_grid() function so that main.py can import the grid when needed. I used no parameters because all of the information was being made by the function itself rather than calling on outside information. All variables are local for testability and predictability reasons as they will not be affected by outside code.