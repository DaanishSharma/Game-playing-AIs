# AI Game Agents
Game Agents

1)Nim Agent Qlearning Agent

2)TicTacToe Minimax Agent

3)Minesweeper

4)Sliding Puzzle Solver  (A* Graph Search) : Always use admissible heuristic to get optimal solution h(n)<=d(n) i.e. h(n) always underestimates the distance/cost to goal  

Example ip output of Sliding Puzzle Solver
INPUT

================================


3


0 3 8 4 1 7 2 6 5

================================
START OF PUZZLE

[[0 3 8]
 [4 1 7]
 [2 6 5]]

ANSWER IS AT DEPTH OF 20 NODES

[[4 3 8]
 [0 1 7]
 [2 6 5]]
 
[[4 3 8]
 [2 1 7]
 [0 6 5]]
 
[[4 3 8]
 [2 1 7]
 [6 0 5]]
 
[[4 3 8]
 [2 0 7]
 [6 1 5]]
 
[[4 3 8]
 [0 2 7]
 [6 1 5]]
 
[[0 3 8]
 [4 2 7]
 [6 1 5]]
 
[[3 0 8]
 [4 2 7]
 [6 1 5]]
 
[[3 2 8]
 [4 0 7]
 [6 1 5]]
 
[[3 2 8]
 [4 1 7]
 [6 0 5]]
 
[[3 2 8]
 [4 1 7]
 [6 5 0]]
 
[[3 2 8]
 [4 1 0]
 [6 5 7]]
 
[[3 2 0]
 [4 1 8]
 [6 5 7]]
 
[[3 0 2]
 [4 1 8]
 [6 5 7]]
 
[[3 1 2]
 [4 0 8]
 [6 5 7]]
 
[[3 1 2]
 [4 5 8]
 [6 0 7]]
 
[[3 1 2]
 [4 5 8]
 [6 7 0]]
 
[[3 1 2]
 [4 5 0]
 [6 7 8]]
 
[[3 1 2]
 [4 0 5]
 [6 7 8]]
 
[[3 1 2]
 [0 4 5]
 [6 7 8]]
ANSWER

=======================


[[0 1 2]                     
 [3 4 5]                     
 [6 7 8]]
 
============================
