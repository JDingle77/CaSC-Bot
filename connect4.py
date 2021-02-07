# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:08:50 2021

@author: sammy
"""
import discord
import pygame
import numpy as np



class MyClient(discord.Client):
    async def on_ready(self):
        print('Bot is ready.')
    
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith("!connect4"):
            pygame.init()
            #create screen
            screen = pygame.display.set_mode((1134,972))
            #background
            background = pygame.image.load("Connect4Board.png")
            #title and icon
            pygame.display.set_caption("Connect 4")
            
            #Player 1
            playerImg1 = pygame.image.load("PuckSmiley.png")
            
            #Player 2
            playerImg2 = pygame.image.load("PuckHeart.png")
            
            
            
            def save_file():
                s=pygame.display.get_surface()
                pygame.image.save(s, "connect4.png")
                return
            
            
            ROW_COUNT = 6
            COLUMN_COUNT = 7
            
            
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
                
            def print_scene(board, coord):
                screen.fill((0, 0, 0))
                screen.blit(background, (0,0))
                
                for c in range(COLUMN_COUNT):
                    for r in range(ROW_COUNT):
                        if(board[r][c]==1):
                            screen.blit(playerImg1,(coord[r][c]))
                        if(board[r][c]==2):
                            screen.blit(playerImg2,(coord[r][c]))
            
                pygame.display.update()
                save_file()
                        
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
                        
            
            board = create_board()
            
            game_over = False
            turn = 0;
            coords = return_coords()
            def is_correct(x): 
                return int(x.content) <= 6 and int(x.content) >= 0 and x.content.isdigit()
            while not game_over:
                
               
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        save_file()
                        game_over = True
                print_scene(board, coords)
                await message.channel.send(file=discord.File('connect4.png'))
                # Ask for Player 1 Input
                if turn == 0:
                    await message.channel.send("Player 1 Make your Selection (0-6): ")
                    
                    col = await self.wait_for('message', check=is_correct)
                    col = int(col.content)
                            
                    if not is_valid_location(board, col):
                        await message.channel.send("This column is full.")
                        continue
                    
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                        
                        if winning_move(board, 1):
                            print_scene(board, coords)
                            await message.channel.send(file=discord.File('connect4.png'))
                            await message.channel.send("PLAYER 1 WINS !!!")
                            game_over = True
                            break
                # Ask for Player 2 Input
                else:
                    await message.channel.send("Player 2 Make your Selection (0-6): ")
                    
                    col = await self.wait_for('message', check=is_correct)
                    col = int(col.content)   
                    if not is_valid_location(board, col):
                        await message.channel.send("This column is full.")
                        continue
                    
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)
                        
                        if winning_move(board, 2):
                            print_scene(board, coords)
                            await message.channel.send(file=discord.File('connect4.png'))
                            await message.channel.send("PLAYER 2 WINS !!!")
                            game_over = True
                            break
                
                turn += 1
                turn = turn % 2
                
            pygame.display.quit()
            pygame.quit()
client = MyClient()
client.run('ODA3NDcyNTI2MjE3MDUyMTYw.YB4fZA.qof50jXFk1kKTyOnlEIaIIAJ8MI')
