"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    c=0
    for i in range(3):
        for j in range(3):
            if board[i][j]!=EMPTY :
                c+=1
    if c%2:
        return O
    else:
        return X

def actions(board):
    action = list()
    for i in range(3):
        for j in range(3):
            if (board[i][j]==O) or (board[i][j]==X) :
                            pass
            else :
                action.append((i,j))
    return action
def result(board, action):
    i=(action[0])
    j=(action[1])
    board1=copy.deepcopy(board)
    board1[i][j]=player(board)
    """
    Returns the board that results from making move (i, j) on the board.
    """
    return board1
def winner(board):
    ans=utility(board)
    if ans==1 :
        return X
    elif ans==-1:
        return O
    else :
        return None
def terminal(board):
    #checks if board full
    #checks 2 diagonals 3 rows 3 colunmns
    c=0
    for i in range(3):
        for j in range(3):
            if board[i][j]!=EMPTY :
                c+=1
    if c==9 :
            return True
    c=0
    for i in range(3):
        ans=board[i][0]
        c=0
        for j in range(3):
            if board[i][j]==ans :
                c+=1
        if c==3 and ans!=EMPTY:
            return True
    for i in range(3):
        c=0
        ans=board[0][i]
        for j in range(3):
            if board[j][i]==ans :
                c+=1
        if c==3 and ans!=EMPTY:
            return True
        if ((board[0][0]==board[1][1] and board[1][1]==board[2][2]) or (board[0][2]==board[1][1] and board[1][1]==board[2][0]))and (board[1][1]!=EMPTY):
            return True
    return False
def utility(board):
    if (board[0][0]==board[1][1] and board[1][1]==board[2][2]) or (board[0][2]==board[1][1] and board[1][1]==board[2][0]) :
        ans=board[1][1]
        if ans== O:
            return -1
        elif ans==X:
            return 1
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][0]==board[i][2]):
            ans=board[i][0]
            if ans==O:
                return -1
            elif ans==X:
                return 1
    for i in range(3):
        if(board[0][i]==board[1][i] and board[0][i]==board[2][i]):
            ans=board[0][i]
            if ans==O:
                return -1
            elif ans==X:
                return 1
    return 0

def minimax(board):
    if(player(board)==X):
        act=maxi(board)
    else:
        act=mini(board)
    return act
def maxi(board):
    v= -2
    for action in actions(board):
        m=min_value(result(board,action))
        if v < m:
                v=m
                act=action
    return act
def mini(board):
    v= 2
    for action in actions(board):
     m=max_value(result(board,action))
     if v > m:
        v=m
        act=action
    return act
def max_value(board):
    if (terminal(board)):
        return utility(board)
    v = -2
    for action in actions(board):
        v=max(v,min_value(result(board,action)))
    return v
def min_value(board):
    if (terminal(board)):
        return utility(board)
    v=2
    for action in actions(board):
        v=min(v,max_value(result(board,action)))
    return v
