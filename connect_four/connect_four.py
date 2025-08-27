import numpy as np
import pygame
import sys

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def create_board():
    # Creating a matix with 6 columns & 7 rows. Suitable for connect four game.
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def is_valid_move(board, col):
    # This will check if the column selected by player is valid or not.
    # For that, we need to check if top row of selected column is free or not
    # In board if we drop a piece, it will sit in last row(5th row), so we have to check if top row(0th) is free or not
    return board[0][col] == 0


def drop_piece(board, row, col, piece):
        board[row][col] = piece


def get_next_free_row(board, col):
    # This will give us the next row, on which the next players piece will sit
    # we need to return the row which is not filled (i.e, which is filled with zero)
    for r in range(ROW_COUNT-1, -1, -1):
        if board[r][col] == 0:
            return r


def winning_move(board, r, c, piece):
    is_winner = False
    # Check for Vertical st.line win
    for i in range(ROW_COUNT - 3):
        if board[i][c] == piece and board[i+1][c] == piece and board[i+2][c] == piece and board[i+3][c] == piece:
            is_winner = True
   
    # Check for Horizontal st.line win
    for i in range(COLUMN_COUNT - 3):
        if board[r][i] == piece and board[r][i+1] == piece and board[r][i+2] == piece and board[r][i+3] == piece:
            is_winner = True
   
    # Check for diagonal wins
    for i in range(ROW_COUNT - 3):
        for j in range(COLUMN_COUNT - 3):
            if board[i][j] == piece and board[i+1][j+1] == piece and board[i+2][j+2] == piece and board[i+3][j+3] == piece:
                is_winner = True
   
    for j in range(COLUMN_COUNT-3):
         for i in range(3, ROW_COUNT):
              if board[i][j] == piece and board[i-1][j+1] == piece and board[i-2][j+2] == piece and board[i-3][j+3] == piece:
                  is_winner = True
    return is_winner


def draw_board(board):
    global SQUARESIZE, RADIUS, screen
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, (r+1) * SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (c * SQUARESIZE + SQUARESIZE/2, (r+1) * SQUARESIZE + SQUARESIZE/2), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c * SQUARESIZE + SQUARESIZE/2, (r+1) * SQUARESIZE + SQUARESIZE/2), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c * SQUARESIZE + SQUARESIZE/2, (r+1) * SQUARESIZE + SQUARESIZE/2), RADIUS)

    pygame.display.update()



def main():
    global SQUARESIZE, RADIUS, screen
    board = create_board()
    print(board)
    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 100
    RADIUS = int(SQUARESIZE / 2 - 5)
    width = COLUMN_COUNT * SQUARESIZE
    hight = (ROW_COUNT + 1)* SQUARESIZE

    size = (width, hight)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()
    myFont = pygame.font.SysFont("monospace", 75)

    while not game_over:

        for event in pygame.event.get():   # Without this for loop, our pygame console goes into not responsing state
                # (if we are not engaging pygame console continuously then pygame thinks our game carshed & puts it in not responsing state)
            if event.type == pygame.QUIT:
                sys.exit()
           
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    c = posx // SQUARESIZE
                    pygame.draw.circle(screen, RED, (c * SQUARESIZE + SQUARESIZE/2, SQUARESIZE/2), RADIUS)
                else:
                    c = posx // SQUARESIZE
                    pygame.draw.circle(screen, YELLOW, (c * SQUARESIZE + SQUARESIZE/2, SQUARESIZE/2), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                print(event.pos)
                # Ask for Player 1 Input. In connect four game, player have to select one coloum out of 0 to 6 (as we have total 7 columsn in our board)
                if turn == 0:
                    posx = event.pos[0]
                    col = posx // SQUARESIZE
                    # col = int(input("Player 1, to make your move, sleect from 0-6: "))
                    if is_valid_move(board, col):
                        row = get_next_free_row(board, col)
                        drop_piece(board, row, col, 1)
                        is_winner = winning_move(board, row, col, 1)
                        if is_winner:
                            # print("Yay! Player 1 Won the game")
                            label = myFont.render("Player 1 Wins!!!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True
                   
                # # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = posx // SQUARESIZE
                    # col = int(input("Player 2, to make your move, sleect from 0-6: "))
                    if is_valid_move(board, col):
                        row = get_next_free_row(board, col)
                        drop_piece(board, row, col, 2)
                        is_winner = winning_move(board, row, col, 2)
                        if is_winner:
                            # print("Yay! Player 2 Won the game")
                            label = myFont.render("Player 2 Wins!!!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True

                turn += 1   # increasing turn value after every loop
                turn = turn % 2  # if turn is even (=0) then its Player 1's move & if its odd (=1) then its Player 2's move
                print(board)
                draw_board(board)

                if game_over:
                    pygame.time.wait(3000)

main()
