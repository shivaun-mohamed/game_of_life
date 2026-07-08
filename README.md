#   Conway's Game of Life

The Game of Life is a cellular automaton created by the British mathematician John Conway in 1970. It is played on a grid, each cell being one of two states: dead or alive. Cells evolve each generation depending on the amount of live and dead cells within their neighbourhood (their adjacent cells horizontally, vertically, and diagonally). This evolution is determined by a [Ruleset](#ruleset). 

The game is a zero-player game, meaning it does not require any input after its initial state. 

## Ruleset
Through each generation (a grid state), the following evolutions are made:
1. Live cells with less than two live neighbours die, caused by underpopulation.
2. Live cells with exactly two or three live neighbours live onto the next generation.
3. Live cells with more than three live neighbours die, caused by overpopulation.
4. Dead cells with exactly three live neighbours are born in the next generation, caused by reproduction.

## Purpose
Coming soon...

## Implementation / Design Decisions
Coming soon...

## How to Run
Coming soon...