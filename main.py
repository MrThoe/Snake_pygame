import pygame as p
import snake as s
import apple as a

#Globals:
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
gameExit = False
clock = p.time.Clock()
gameStop = False

# Pygame SETUP:
p.init()
WIDTH = 600
HEIGHT = 600
CELLS = 20
num = WIDTH/CELLS
p.display.set_caption("Mr. Thoe's Snake")
win = p.display.set_mode((WIDTH,HEIGHT))
font = p.font.Font('freesansbold.ttf', 32)
text = font.render('Mr. Thoe shakes his head...', True, green, blue)
textRect = text.get_rect()
textRect.center = (WIDTH//2, HEIGHT//2)
# Game Objects:
snake = s.Snake(num, CELLS)
apple = a.Apple(num)

# MAIN GAME
while not gameExit:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            quit()
        elif event.type == p.KEYDOWN:
            k = event.key
            if k == p.K_UP and snake.dir != "DOWN":
                snake.dir = "UP"
            elif k == p.K_DOWN and snake.dir != "UP":
                snake.dir = "DOWN"
            elif k == p.K_RIGHT and snake.dir != "LEFT":
                snake.dir = "RIGHT"
            elif k == p.K_LEFT and snake.dir != "RIGHT":
                snake.dir = "LEFT"

    if apple.x == snake.x[0] and apple.y == snake.y[0]:
        snake.x.append(apple.x)
        snake.y.append(apple.y)
        apple = a.Apple(num)

    #  Main drawing order
    win.fill(0)  #Background
    p.draw.rect(win, (255,0,0), [0,0,WIDTH, HEIGHT], 2)  #Border

    #Draw Objects    
    apple.show(win)    
    snake.show(win)  
    if not gameStop:
        snake.move()
        snake.follow()
    if snake.hits_wall() or snake.hits_self():  #Stop game but leaving window open
        gameStop = True
        win.blit(text, textRect)
  
    clock.tick(5)
    p.display.update()

