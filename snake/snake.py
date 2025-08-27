import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)   # updating the existing postion of cube to a new postion

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows  # tells the distance or width(hight) of each cube
        i = self.pos[0]  # stores the x cordinate of cube
        j = self.pos[1]  # stores the y cordinate of cube

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        # here (i*dis+1, j*dis+1, dis-2, dis-2) is the (x1, y1, x2, y2) & the rectangle will be drawn from top left corner(x1, y1) till bottom right corner(x2, y2) of rectangle
       
        # if eyes falg is true, then we need to draw eyes on the head cube of snake
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)  # first eye is at the postion at (x, y) as (centre-3, 8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)  # second eye is at the postion at (x, y) as (dis - 6, 8)
            # we choose the above positions randomly, to make the eyes more centred
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)



class snake(object):
    body = []   # contains the snake body, i.e, the set of cubes(nothing but cube objects) in a list
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)  # This represents the head cube of the snake  # this is a cube object
        self.body.append(self.head)  # Appending the head to snake body
        # self.dirnx and self.dirny represnts the direction in which snake is moving, if dirnx = 0 and dirny = 0 then cube will not move
        #  only one value in both should be true, cause snake can move in either x dir(horizontal) or y dir(vertical) at any point of time
        self.dirnx = 0  
        self.dirny = 1
   

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1   # moving left on the screen is like going to -ve x dir, thats why self.dirnx = -1
                    self.dirny = 0  # no need to move in y dir, thats why self.driny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    # above statement will give head postion as key & direction(dirnx & dirny) as value & store it in turns dict
                    # for ex. if we print turns dict, we get {(10, 10): [-1, 0]} -- which tells us, the head cube at (10, 10) turns in left dir - (-1, 0)
                    # We are using above line(# 37) is to store the postion(x cordinate & y cordinate) of head (cube obj) & the direction it moved (dirnx & dirny)

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0   # no need to move in x dir (cause this condition is for moving up), thats why self.drinx = 0
                    self.dirny = -1  # moving up on the screen is like going to -ve y dir, thats why self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # Turning each cube of snake body to a particular direction (same as head cube's direction)

        for i, cubee in enumerate(self.body):  # enumerate through the body list
            p = cubee.pos[:]  # will get the postion (x, y) of each cube

            if p in self.turns:  # checking if that cube's postion is in turns dict (we already filled turns dict with head positions & dir it moved)
                turn = self.turns[p]  # storing the dirnx & dirny in turn set (for example, turn = (-1, 0) represents the left turn)
                cubee.move(turn[0], turn[1])  # providing x cor (turn[0]) & y cordinate (turn[1]) to move() method of cube class
                if i == len(self.body) - 1:
                    self.turns.pop(p)  
                    # in above line, removing that turn (key value pair) from turns list, when ever last cube got turned
                    # if not, if our snake hits that postion at any time, regardless of whether we turned it or not, the cubes starts turning
           
            # checking if the snake hit the edges & making it to start over on the other side of the screen
            else:
                if cubee.dirnx == -1 and cubee.pos[0] <= 0: cubee.pos = (cubee.rows-1, cubee.pos[1])  
                # if snake(list of cubes) hit the left edge, then need to start snake on right side (i.e, chaneg its postion to right most cube)
               
                elif cubee.dirnx == 1 and cubee.pos[0] >= cubee.rows-1: cubee.pos = (0,cubee.pos[1])
               
                elif cubee.dirny == 1 and cubee.pos[1] >= cubee.rows-1: cubee.pos = (cubee.pos[0], 0)
               
                elif cubee.dirny == -1 and cubee.pos[1] <= 0: cubee.pos = (cubee.pos[0],cubee.rows-1)

                # if none of the above condtions are true then simply moving the xube in same x dir & y dir
                else: cubee.move(cubee.dirnx,cubee.dirny)


    def addCube(self):
        tail = self.body[-1]
        dx, dy = self.dirnx, self.dirny

        # Adding an extra cube at the end of snake
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
            # in above line, we are adding a cube at the end of snake \
            # (i.e, "last cube's x postion-1" ( need to subtract one to get left side cube of tail of snake)), if snake is moving to right dir(+ve x dir)
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
 
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy


    def draw(self, surface):
        # is to draw each & every cube on the surface
        for i, cubee in enumerate(self.body):
            if i == 0:  # we are draiwng eyes for the head/first cube
                cubee.draw(surface, eyes=True)
            else:
                cubee.draw(surface)  


    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1        



def drawGrid(w, rows, surface):
    # to draw grid(game console), where snake game is going to run
    sizeBtwn = w // rows
    # sizeBtwn is to specify the size of each grid in the window/surface
    x = 0
    y = 0
    for i in range(rows):
        x += sizeBtwn
        y += sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))   # To draw vertical lines
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))   # To draw horizontal lines


def redrawWindow(surface):
    # To draw snake game window everytime, when snake cubes or food cubes get updated
    global rows, width, s, food
    surface.fill((0, 0, 0))   # providing black color value(0, 0, 0) to the window
    drawGrid(width, rows, surface)
    s.draw(surface)
    food.draw(surface)
    pygame.display.update()


def randomFood(snakee):
    # to pop random food cube on the snake game console
    global rows
    postions = snakee.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        # this condition is to check, if random cube(food) is on the snake body cubes
        # for all the snake body cubes, we are checking is the positions is same as randomly generated cube pos, if yes then keeping those cubes in a list
        # checking if the list's len is > 0 then again randomly choosing food cube's postions
        if len(list(filter(lambda z:z.pos == (x,y), postions))) > 0:
            continue
        else:
            break
    return (x, y)


def message_box(subject, content):
    # To provide a pop up msg, if game over
    root = tk.Tk()
    root.attributes("-topmost", True)  # to keep the message box pop up window on top of all other windows
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()   # this will reopen/restart the gaming console
    except:
        pass



def main():
    global width, rows, s, food
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))  # creating the game surface, with 500 X 500 size
    s = snake((255, 0, 0), (10, 10))   # provided red color(255, 0, 0) to the snake & starting the snake at (10, 10) position
    food = cube(randomFood(s), color=(0, 255, 0))  # providing green color (0, 255, 0) & random position(through randomFood function) to food cube

    flag = True
    pygame.init()
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(5)  # our snake moves 5 cubes per sec
        s.move()
        if s.body[0].pos == food.pos:
            s.addCube()
            food = cube(randomFood(s), color=(0, 255, 0))
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                print('Score: ', len(s.body) - 1)
                message_box("You Lost!", f"Your score is {len(s.body) - 1} \n Play again...")
                s.reset((10, 10))
                break
       
        redrawWindow(win)
        for event in pygame.event.get():   # Without this for loop, our pygame console goes into not responsing state
            # (if we are not engaging pygame console continuously then pygame thinks our game carshed & puts it in not responsing state)
            if event.type == pygame.QUIT:
                flag = False


main()