# RGB Color definitions
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

#Square
HEIGHT = 30
WIDTH = HEIGHT

#Border
OFFSET = 30
MARGIN_TOP = 10

#Board
ROWS = 50
COLS = 50
CARDINALS = {"up": (0,-1), "left": (-1,0), "down": (0,1), "right": (1,0)}
PATH_COLORS = [(232, 201, 245),(201, 242, 245),(245, 201, 206),(240, 245, 201),(201, 245, 210)]

#window
WINDOW_SIZE = ((COLS * WIDTH) + (2 * OFFSET), (ROWS * HEIGHT) + (4 * OFFSET))
TEXT_OFFSET_Y = (ROWS * HEIGHT) + (2 * OFFSET)
TEXT_OFFSET_X = (COLS * WIDTH)/4.0
FRAMERATE = 50
ANIMATION_DELAY = 6
FONT_SIZE = 30

#game
TIME_MULTIPLIER = 1.0/(FRAMERATE*4)
LIVES = 3

#this is a comment so we can push to git ;)
