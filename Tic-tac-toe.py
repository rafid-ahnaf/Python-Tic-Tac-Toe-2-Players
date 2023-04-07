class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def draw_board(self):
        print("-------------")
        for i in range(0, 9, 3):
            print("|", self.board[i], "|", self.board[i+1], "|", self.board[i+2], "|")
            print("-------------")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        else:
            print("Sorry, that space is already taken. Try again.")    

    def check_for_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
            (0, 4, 8), (2, 4, 6)           # diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True

        return False

    def play_game(self):
        while not self.check_for_winner() and ' ' in self.board:
            self.draw_board()
            move = int(input(f"{self.current_player}'s turn. Enter a number between 0-8: "))
            self.make_move(move)

        self.draw_board()
        
        if self.check_for_winner():
            print(f"Congratulations, {self.current_player} wins!")
        else:
            print("It's a tie!")

game = TicTacToe()
game.play_game()