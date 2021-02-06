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
    tuple1 = (13.5, 823.5)
    tuple2 = (175.5, 823.5)
    tuple3 = (337.5, 823.5)
    tuple4 = (499.5, 823.5)
    tuple5 = (661.5, 823.5)
    tuple6 = (823.5, 823.5)
    tuple7 = (985.5, 823.5)
    tuple8 = (13.5, 661.5)
    tuple9 = (175.5, 661.5)
    tuple10 = (337.5, 661.5)
    tuple11 = (499.5, 661.5)
    tuple12 = (661.5, 661.5)
    tuple13 = (823.5, 661.5)
    tuple14 = (985.5, 661.5)
    tuple15 = (13.5, 499.5)
    tuple16 = (175.5, 499.5)
    tuple17 = (337.5, 499.5)
    tuple18 = (499.5, 499.5)
    tuple19 = (661.5, 499.5)
    tuple20 = (823.5, 499.5)
    tuple21 = (985.5, 499.5)
    tuple22 = (13.5, 337.5)
    tuple23 = (175.5, 337.5)
    tuple24 = (337.5, 337.5)
    tuple25 = (499.5, 337.5)
    tuple26 = (661.5, 337.5)
    tuple27 = (823.5, 337.5)
    tuple28 = (985.5, 337.5)
    tuple29 = (13.5, 175.5)
    tuple30 = (175.5, 175.5)
    tuple31 = (337.5, 175.5)
    tuple32 = (499.5, 175.5)
    tuple33 = (661.5, 175.5)
    tuple34 = (823.5, 175.5)
    tuple35 = (985.5, 175.5)
    tuple36 = (13.5, 13.5)
    tuple37 = (175.5, 13.5)
    tuple38 = (337.5, 13.5)
    tuple39 = (499.5, 13.5)
    tuple40 = (661.5, 13.5)
    tuple41 = (823.5, 13.5)
    tuple42 = (985.5, 13.5)
    
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
    
    