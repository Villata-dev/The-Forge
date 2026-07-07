class PuzzleManager:
    def __init__(self):
        self.solved_puzzles = set()

    def check_combination(self, puzzle_id: str, input_sequence: list, solution: list) -> bool:
        if input_sequence == solution:
            self.solved_puzzles.add(puzzle_id)
            return True
        return False
