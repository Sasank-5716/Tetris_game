import pygame
from constants import *
from game_logic import GameLogic

class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.game = GameLogic()
        self.fall_time = 0
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.current_x -= 1
                    if self.game.check_collision():
                        self.game.current_x += 1
                if event.key == pygame.K_RIGHT:
                    self.game.current_x += 1
                    if self.game.check_collision():
                        self.game.current_x -= 1
                if event.key == pygame.K_DOWN:
                    self.game.current_y += 1
                    if self.game.check_collision():
                        self.game.current_y -= 1
                if event.key == pygame.K_UP:
                    self.game.rotate_piece()
                if event.key == pygame.K_SPACE:  # Hard drop
                    while not self.game.check_collision():
                        self.game.current_y += 1
                    self.game.current_y -= 1
                    self.game.merge_piece()
                    self.game.clear_lines()
                    if not self.game.new_piece():
                        return False
        return True
    
    def update(self, dt):
        self.fall_time += dt
        if self.fall_time >= FALL_SPEED:
            self.fall_time = 0
            self.game.current_y += 1
            if self.game.check_collision():
                self.game.current_y -= 1
                self.game.merge_piece()
                self.game.clear_lines()
                if not self.game.new_piece():
                    return False
        return True
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.game.grid[y][x]:
                    pygame.draw.rect(self.screen, self.game.grid[y][x], 
                                   (x * BLOCK_SIZE, y * BLOCK_SIZE, 
                                    BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, WHITE, 
                                   (x * BLOCK_SIZE, y * BLOCK_SIZE, 
                                    BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # Draw current piece
        if self.game.current_piece:
            for y, row in enumerate(self.game.current_piece):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, self.game.current_color, 
                                       ((self.game.current_x + x) * BLOCK_SIZE, 
                                        (self.game.current_y + y) * BLOCK_SIZE, 
                                        BLOCK_SIZE, BLOCK_SIZE))
                        pygame.draw.rect(self.screen, WHITE, 
                                       ((self.game.current_x + x) * BLOCK_SIZE, 
                                        (self.game.current_y + y) * BLOCK_SIZE, 
                                        BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.game.score}", True, WHITE)
        self.screen.blit(score_text, (GRID_WIDTH * BLOCK_SIZE + 10, 20))
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60) / 1000
            running = self.handle_events()
            if running:
                running = self.update(dt)
                self.draw()
        pygame.quit()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()