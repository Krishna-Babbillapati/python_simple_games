import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')
   
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (Gives us the board with its index in the box)
        for row in [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]:
            print('|' + '|'.join(row) + '|')

   
    def available_moves(self):
        # To return available balnk spaces in board
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board
   
    def num_empty_squares(self):
        return len(self.available_moves())
        # or return self.board.count(' ')
   
    def make_move(self, sqaure, letter):
        # to make a move we need the square in which player want to move & the letter they want to keep
        # if the squre is valid then return Ture else return False
        if self.board[sqaure] == ' ':
            self.board[sqaure] = letter   # if the square in the baord is empty then keep the letter in that sqaure
            if self.winner(sqaure, letter):
                self.current_winner = letter
            return True
        return False
   
    def winner(self, square, letter):
        # To be a winner letter needs to be in a straight line .... we need to check all posibilities
        # check the rows
        row_ind = square // 3  # row ind will get 0 for 0, 1, 2 (first row) & 1 for 3, 4, 5 (sec row)... etc
        row = self.board[row_ind * 3: (row_ind+1) * 3]
        if all([spot == letter for spot in row]):   # if all the spots in that row is same as the letter, then the letter is winner
            return True

        # check the columns
        col_ind = square % 3 # col_ind gives 0 for 0, 3, 6 (first col) & 1 for 1, 4, 7 (sec col)... etc
        column = [self.board[col_ind+(i*3)] for i in range(3)]
        if all([spot == letter for spot in column]):  
            return True
       
        # check the diagonals
        # The only possiblity to win in a diagonal is to making a move in diagonal squares which are (0, 4, 8) and (2, 4, 6)
        # If we see, all the diagonal squares are of even numbers
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
           
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
       
        # if none of the above conditions are true then there is no winner(tie)
        return False


def play(game, x_player, o_player, print_game=True):
    # return the winner (the letter) if any one wins or else return None if its tie.
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting the game with X
   
    # Looping the game until no empty spaces in the board
    while game.empty_squares():
        if letter == 'X':
            square = x_player.get_move(game)
        elif letter == 'O':
            square = o_player.get_move(game)

        # We need to make a move & print the board if print_game falg is True
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes move to {square}')
                game.print_board()
                print('\n')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
        if print_game:
            time.sleep(1)  # to sleep for a sec, after every move
        # Need to alter the letter after one move is done.
        # Means, change the X's turn to O's turn after every move or viceversa
        letter = 'O' if letter == 'X' else 'X'    # Switching the player

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):
        x_player = RandomComputerPlayer('X')
        o_player = SmartComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins+=1
        elif result == 'O':
            o_wins+=1
        else:
            ties+=1
    print(f'After 1000 games, X wins for {x_wins} times, O wins for {o_wins} times and ties for {ties} times')
