from constants import COLORS
import random
# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    
    [[1, 0, 0],
     [1, 1, 1]],     # J
     
    [[0, 0, 1],
     [1, 1, 1]],     # L
     
    [[1, 1],
     [1, 1]],        # O
     
    [[0, 1, 1],
     [1, 1, 0]],     # S
     
    [[0, 1, 0],
     [1, 1, 1]],     # T
     
    [[1, 1, 0],
     [0, 1, 1]]      # Z
]

def get_random_piece():
    """Return a random piece with its color"""
    shape_idx = random.randint(0, len(SHAPES) - 1)
    return SHAPES[shape_idx], COLORS[shape_idx]