# import the pygame library, all this learned from
# http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
from workspace.tile import tile
from workspace.executive import executive
from GUI.inputgui import inputGui
from tkinter import *

import pygame

import sys



def print_board2():
    screen.fill(DARKGREY)



    for i in range(row):
        for j in range(column):
            color = GREY

            if exe.cheatBoard.board[j][i].isVisible == False:
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])

            if exe.cheatBoard.board[j][i].isVisible == True:
                color = WHITE
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
            if exe.cheatBoard.board[j][i].isBomb == True and exe.cheatBoard.board[j][i].isVisible == True:
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
                temp = grid[j][i].move(-5, -5)
                screen.blit(bomb, temp)
            if exe.cheatBoard.board[j][i].adjBomb > 0 and exe.cheatBoard.board[j][i].isVisible == True:
                temp = grid[j][i].move(5, 5)
                screen.blit(font.render(str(exe.cheatBoard.board[j][i].adjBomb), True, BLACK), (temp))
            if exe.cheatBoard.board[j][i].isFlagged == True and exe.cheatBoard.board[j][i].isVisible == False:
                screen.blit(flag, grid[j][i])

    pygame.draw.rect(screen, (255, 255, 255),
                     ((column * 20 + MARGIN * column + MARGIN), 5, 100,20))
    screen.blit(font.render('cheatmode!', True, (255, 0, 0)), (column * 20 + MARGIN * column + MARGIN+5, 8))
    pygame.draw.rect(screen, (255, 255, 255),
                     ((column * 20 + MARGIN * column + MARGIN), 30, 100, (row-1)*(20+MARGIN)-5))

    screen.blit(font.render('Flag left:', True, (255, 0, 0)), (column * 20 + MARGIN * column + MARGIN+5, 32))
    screen.blit(font.render(str(exe.gameBoard.num_bombs-exe.gameBoard.num_flagged), True, (255, 0, 0)), (column * 20 + MARGIN * column + MARGIN+70, 32))




    pygame.display.flip()


pygame.init()
pygame.display.init()


def print_board():
    screen.fill(DARKGREY)




    for i in range(row):
        for j in range(column):
            color = GREY

            if exe.gameBoard.board[j][i].isVisible == False:
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])

            if exe.gameBoard.board[j][i].isVisible == True:
                color = WHITE
                grid[j][i] =  pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
            if exe.gameBoard.board[j][i].isBomb == True and exe.gameBoard.board[j][i].isVisible == True :
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
                temp = grid[j][i].move(-5, -5)
                screen.blit(bomb, temp)
            if exe.gameBoard.board[j][i].adjBomb >  0 and exe.gameBoard.board[j][i].isVisible == True:
                temp = grid[j][i].move(5,5)
                screen.blit(font.render(str(exe.gameBoard.board[j][i].adjBomb), True, BLACK), (temp))
            if exe.gameBoard.board[j][i].isFlagged == True and exe.gameBoard.board[j][i].isVisible == False:
                screen.blit(flag,grid[j][i])

    pygame.draw.rect(screen, (255, 255, 255),
                     ((column * 20 + MARGIN * column + MARGIN), 5, 100, 20))
    screen.blit(font.render('cheatmode!', True, (255, 0, 0)), (column * 20 + MARGIN * column + MARGIN + 5, 8))
    pygame.draw.rect(screen, (255, 255, 255),
                     ((column * 20 + MARGIN * column + MARGIN), 30, 100, (row - 1) * (20 + MARGIN) - 5))

    screen.blit(font.render('Flag left:', True, (255, 0, 0)), (column * 20 + MARGIN * column + MARGIN + 5, 32))
    screen.blit(font.render(str(exe.gameBoard.num_bombs - exe.gameBoard.num_flagged), True, (255, 0, 0)),
                (column * 20 + MARGIN * column + MARGIN + 70, 32))

    pygame.display.update()
    pygame.display.flip()



pygame.init()
pygame.display.init()

"""definition of colors
"""
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
BLACK = (0, 0, 0)
DARKGREY = (169, 169, 169)

# tile width and height constant
WIDTH = 20
HEIGHT = 20

# margin between tiles
MARGIN = 5

w=2
h=2
b=1
incorrect = True

winSound = pygame.mixer.Sound("soundEffect/Applause.wav")
loseSound = pygame.mixer.Sound("soundEffect/Explosion.wav")
revealSound = pygame.mixer.Sound("soundEffect/Click.wav")
flagSound = pygame.mixer.Sound("soundEffect/Ding.wav")
cheaterSound = pygame.mixer.Sound("soundEffect/Cheater.wav")

while (incorrect == True):
    try:
        screen = Tk()
        screen.iconbitmap(r'GUI\MemoryLeakLogo.ico')
        inputScreen = inputGui(screen)
        screen.protocol("WM_DELETE_WINDOW", sys.exit)

        screen.mainloop()

        w = int(inputScreen.getWidth())
        h = int(inputScreen.getHeight())
        b = int(inputScreen.getBombNum())

        if (40>= w >= 2) and (72>= h >= 2) and (b >= 1) and 1 <= ((w*h)-b) <= 1088:
            incorrect = False
        if(incorrect == True):
            raise ValueError()
        break;
    except ValueError:
        badCase = Tk()
        badCase.iconbitmap(r'GUI\MemoryLeakLogo.ico')
        required = 1
        if ((w * h) > 1088):
            required = (w*h) - 1088
        Label(badCase, text="Please enter a valid integer.\n1<Width<73 and 1<Height<41\nMust "
                            "have at least " + str(required) + " bomb(s) with that size." , ).grid(row=0)
        Button(badCase, text="Ok", command=badCase.destroy).grid(row=1)
        badCase.mainloop()





"""calculate the required screen size based on amount of tiles
"""
screen_width = (int(w) * 20) + ((int(w)+1)*5)
screen_height = (int(h) * 20) + ((int(h)+1)*5 +100)

""" create the screen surface
"""
size =  screen_height, screen_width
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pysweeper")
icon = pygame.image.load("GUI/MemoryLeakLogo.png")
pygame.display.set_icon(icon)
"""create tile grid
"""
board = [[tile() for i in range(int(w))]for j in range(int(h))]

"""main draw loop
"""
program_end = False
font = pygame.font.SysFont('Ariel', 22)

"""looping multiple rects
"""
row = int(w)
column = int(h)

"""game logic grid
"""
grid = [[0] * row for i in range(column)]
bomb = pygame.image.load("GUI/bomb.png")
flag = pygame.image.load("GUI/flag.png")


"""Sets clock rate
"""
clock = pygame.time.Clock()
exe = executive(int(w), int(h), int(b))
exe.run()
gamestate = 0
cheatMode= 0


"""Main game loop
"""
while not program_end and gamestate == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_end = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1):

                pos = pygame.mouse.get_pos()
                originalc=pos[0]
                originald=pos[1]
                # originalr=pos[1]
                c = pos[0] // (WIDTH + MARGIN)
                r = pos[1] // (HEIGHT + MARGIN)
                if(c >= column):
                    c = column - 1
                if(r >= row):
                    r = row - 1
                if(originalc >(WIDTH+MARGIN)* column and originald<30):
                    if(cheatMode==0):
                        cheatMode=1
                        exe.cheatBoard .reveal_all()
                        cheaterSound.play()
                        cheaterSound.set_volume(1.0)
                        # print_board2()
                    else:
                        cheatMode=0
                elif(originalc >(WIDTH+MARGIN)* column and originald>30):
                    cheatMode=0;

                    cheat1 = Tk()
                    cheat1.iconbitmap('GUI/MemoryLeakLogo.ico')
                    Label(cheat1, text="wrong area!", ).grid(row=0)
                    cheat1.mainloop()
                else:
                    if(cheatMode==1):
                        cheat1 = Tk()
                        cheat1.iconbitmap('GUI/MemoryLeakLogo.ico')
                        Label(cheat1, text="please exit the cheatMode first!", ).grid(row=0)
                        cheat1.mainloop()
                    else:
                        exe.gameBoard.reveal_tile(c, r)
                        revealSound.play()
                        revealSound.set_volume(0.1)



            elif(event.button == 3):
                pos = pygame.mouse.get_pos()
                c = pos[0] // (WIDTH + MARGIN)
                r = pos[1] // (HEIGHT + MARGIN)

                exe.gameBoard.flag_tile(c,r)
                flagSound.play()
                flagSound.set_volume(0.1)

    # print_board()
    if(cheatMode==1):
        print_board2()
    else:
        print_board()
    gamestate = exe.checkWinLose()

    clock.tick(60)



if (gamestate == 2):
    exe.gameBoard.reveal_all()
    print_board()
    loseCase = Tk()
    loseCase.iconbitmap('GUI/MemoryLeakLogo.ico')
    Label(loseCase, text="YOU LOSE!!", ).grid(row=0)
    loseSound.play()
    loseSound.set_volume(1.0)
    loseCase.mainloop()
elif (gamestate == 1):
    winCase = Tk()
    winCase.iconbitmap('GUI/MemoryLeakLogo.ico')
    Label(winCase, text="YOU WIN!!", ).grid(row=0)
    winSound.play()
    winSound.set_volume(1.0)
    winCase.mainloop()
pygame.quit()
