from constants import GRID_WIDTH, GRID_HEIGHT
from tetriminos import get_random_piece

class GameLogic:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.current_color = None
        self.score = 0
        self.new_piece()
    
    def new_piece(self):
        self.current_piece, self.current_color = get_random_piece()
        self.current_x = GRID_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0
        return not self.check_collision()
    
    def check_collision(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    if (self.current_y + y >= GRID_HEIGHT or 
                        self.current_x + x < 0 or 
                        self.current_x + x >= GRID_WIDTH or 
                        self.grid[self.current_y + y][self.current_x + x]):
                        return True
        return False
    
    def merge_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_y + y][self.current_x + x] = self.current_color
    
    def rotate_piece(self):
        # Transpose and reverse each row to rotate 90 degrees
        rotated = [[self.current_piece[y][x] for y in range(len(self.current_piece))] 
                  for x in range(len(self.current_piece[0]) - 1, -1, -1)]
        old_piece = self.current_piece
        self.current_piece = rotated
        if self.check_collision():
            self.current_piece = old_piece
    
    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_cleared += 1
                for y2 in range(y, 0, -1):
                    self.grid[y2] = self.grid[y2 - 1][:]
                self.grid[0] = [0 for _ in range(GRID_WIDTH)]
        self.score += lines_cleared * 100
        return lines_cleared