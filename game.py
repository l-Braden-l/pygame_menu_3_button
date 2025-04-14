# -- Imports -- #
import pygame
import sys

# -- Constants -- #
   # - Colors - # 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (153, 76, 0)
PURPLE = (204, 0, 204)
ORANGE =  (255, 128, 0)
SKY_BLUE = (0, 255, 255)

   # - Widow - #
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

   # - Title - # 
TITLE = "My Pygame Project"

   # - Frame Rate - #
FPS = 60


def init_game (): 
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True

def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here
   running = True
   while running:
      running = handle_events()
      screen.fill(WHITE) # Use color from config
      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()