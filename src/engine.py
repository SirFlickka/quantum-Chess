# engine.py
from .board import Board
from .evaluation import evaluate
from .search import minimax

class QuantumChessEngine:
    def __init__(self):
        self.board = Board()
        
    def uci_loop(self):
        # TODO: implement UCI (Universal Chess Interface) loop

    def play_move(self, move):
        self.board.make_move(move)
        evaluation = evaluate(self.board)
        best_move = minimax(self.board)
        return best_move, evaluation
