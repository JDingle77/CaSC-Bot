#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:11:12 2021

@author: jamesdingle
"""

import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
        
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))
    
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
            
    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
            
    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    
    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
            
def return_coords():
    
    
    tuple1 = (81, 81)
    tuple2 = (81, 243)
    tuple3 = (81, 405)
    tuple4 = (81, 567)
    tuple5 = (81, 729)
    tuple6 = (81, 891)
    tuple7 = (81, 1053)
    tuple8 = (243, 81)
    tuple9 = (243, 243)
    tuple10 = (243, 405)
    tuple11 = (243, 567)
    tuple12 = (243, 729)
    tuple13 = (243, 891)
    tuple14 = (243, 1053)
    tuple15 = (405, 81)
    tuple16 = (405, 243)
    tuple17 = (405, 405)
    tuple18 = (405, 567)
    tuple19 = (405, 729)
    tuple20 = (405, 891)
    tuple21 = (405, 1053)
    tuple22 = (567, 81)
    tuple23 = (567, 243)
    tuple24 = (567, 405)
    tuple25 = (567, 567)
    tuple26 = (567, 729)
    tuple27 = (567, 891)
    tuple28 = (567, 1053)
    tuple29 = (729, 81)
    tuple30 = (729, 243)
    tuple31 = (729, 405)
    tuple32 = (729, 567)
    tuple33 = (729, 729)
    tuple34 = (729, 891)
    tuple35 = (729, 1053)
    tuple36 = (891, 81)
    tuple37 = (891, 243)
    tuple38 = (891, 405)
    tuple39 = (891, 567)
    tuple40 = (891, 729)
    tuple41 = (891, 891)
    tuple42 = (891, 1053)
    
    firsttuple = (tuple1, tuple2, tuple3, tuple4, tuple5, tuple6, tuple7)
    secondtuple = (tuple8, tuple9, tuple10, tuple11, tuple12, tuple13, tuple14)
    thirdtuple = (tuple15, tuple16, tuple17, tuple18, tuple19, tuple20, tuple21)
    fourthtuple = (tuple22, tuple23, tuple24, tuple25, tuple26, tuple27, tuple28)
    fifthtuple = (tuple29, tuple30, tuple31, tuple32, tuple33, tuple34, tuple35)
    sixthtuple = (tuple36, tuple37, tuple38, tuple39, tuple40, tuple41, tuple42)
    
    tupleboard = (firsttuple, secondtuple, thirdtuple, fourthtuple, fifthtuple, sixthtuple)
    
    return tupleboard
    
board = create_board()
print_board(board)
game_over = False
turn = 0;

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6): "))
        
        if col > 6 or col < 0:
            continue
            
        if not is_valid_location(board, col):
            print("This column is full.")
            continue
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            
            if winning_move(board, 1):
                print("PLAYER 1 WINS !!!")
                game_over = True
                break
    # Ask for Player 2 Input
    else:
        col = int(input("Player 2 Make your Selection (0-6): "))
        
        if col > 6 or col < 0:
            continue
            
        if not is_valid_location(board, col):
            print("This column is full.")
            continue
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            
            if winning_move(board, 2):
                print("PLAYER 2 WINS !!!")
                game_over = True
                break
    
    print_board(board)
    turn += 1
    turn = turn % 2
    
    