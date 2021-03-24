# Minesweeper Solver

Solver for minesweeper game.

## Notes

How to solve:

Go over every open number tile on the board:

- Distribute their probabilities to all neighboring unselected tiles

- If any empty tile is given a 100% chance of bomb:

  - flag it.

  - update the weights of neighbors
