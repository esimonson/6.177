from constants import *
from imports import *
import helpers, path, math

class Actor(pygame.sprite.Sprite):
    directions = [(0,1), (-1,0), (0,-1), (1,0)] #in order going counterclockwise
    def __init__(self, imageFile, width=WIDTH, height=HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.rotation = (0, 1) #pointing up
        self.degrees = 0 #pointing up

        self.set_image(imageFile)
        self.rect = self.image.get_rect()
        
    def goto(self, col, row):
        if g.board and (col,row) not in g.board.path:
            return
        if col < COLS:
            self.col = col
        if row < ROWS:
            self.row = row
        self.rect.x = helpers.get_col_left_p(self.col)
        self.rect.y = helpers.get_row_top_p(self.row)

    def get_current_square(self):
        return g.board.get_square(self.col,self.row)
    
    def step_forward(self):
        """
        Step forward in current direction
        """
        self.goto(self.col+self.rotation[0],self.row-self.rotation[1])

    def set_image(self, imageFile):
        self.image = pygame.image.load("assets/"+imageFile).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.degrees == 180:
            self.image = pygame.transform.flip(self.image,True,False)
        else:
            self.image = pygame.transform.rotate(self.image,self.degrees)

    def update(self):
        self.img = self.transformations[(self.transformations.index(self.img)-1) % len(self.transformations)]
        self.set_image(self.img)

    def change_dir(self, direction):
        self.rotation = dict(zip(["up","left","down","right"],Actor.directions))[direction]
        self.degrees = math.degrees(math.atan2(self.rotation[1],self.rotation[0]))