VERSION = '0.1'
# A Python (pygame) companion to Mario Party Life
# github.com/chrhyman/mpl

import sys, os.path
import pygame
from pygame.locals import *
import spaces, constants

ROOTDIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES = os.path.join(ROOTDIR, 'resources')

FPS = 30
WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
MARGIN = 25
x2, y2 = (WINDOWWIDTH/4, WINDOWHEIGHT/3)
x3, y3 = (WINDOWWIDTH/2, WINDOWHEIGHT/3)
x4, y4 = (WINDOWWIDTH*3/4, WINDOWHEIGHT/3)
x5, y5 = (WINDOWWIDTH/3, WINDOWHEIGHT*2/3)
x6, y6 = (WINDOWWIDTH*2/3, WINDOWHEIGHT*2/3)
# colors            R    G    B
WHITE           = (255, 255, 255)
BLACK           = (  0,   0,   0)
DARKGRAY        = ( 65,  65,  65)
LIGHTGRAY       = (190, 190, 190)

BGCOLOR = WHITE
TEXTCOLOR = BLACK
VERCOLOR = DARKGRAY

def main():
    global FPSCLOCK, DISPLAYSURF, MAINFONT, BIGFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    MAINFONT = pygame.font.Font(os.path.join(ROOTDIR, 'Consolas.ttf'), 16)
    BIGFONT = pygame.font.Font('Consolas.ttf', 80)
    pygame.display.set_caption('Mario Party Life - v. ' + VERSION)
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        p = getPlayer()
        checkQuit()
        updateDisplay()

def getPlayer():
    rect2p = makeButton('2', DISPLAYSURF, top=y2, left=x2)
    rect3p = makeButton('3', DISPLAYSURF, top=y3, left=x3)
    rect4p = makeButton('4', DISPLAYSURF, top=y4, left=x4)
    rect5p = makeButton('5', DISPLAYSURF, top=y5, left=x5)
    rect6p = makeButton('6', DISPLAYSURF, top=y6, left=x6)

def makeButton(name, surface, top=None, left=None, bottom=None, right=None, midbottom=None):
    button = name + '.png'
    pressed = name + '_p.png'
    imgSurf = pygame.image.load(os.path.join(RESOURCES, 'button', button))
    imgRect = imgSurf.get_rect()
    if top: imgRect.top = top
    if left: imgRect.left = left
    if bottom: imgRect.bottom = bottom
    if right: imgRect.right = right
    if midbottom: imgRect.midbottom = midbottom
    if pygame.mouse.get_pressed()[0] and imgRect.collidepoint(pygame.mouse.get_pos()):
        imgSurf = pygame.image.load(os.path.join(RESOURCES, 'button', pressed))
    surface.blit(imgSurf, imgRect)
    return imgRect

def lineText(text, color, font, left=0, top=0):
    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.topleft = (left, top)
    return textSurf, textRect

def updateDisplay():
    verFont = pygame.font.Font('Consolas.ttf', 11)
    verSurf, verRect = lineText('(c) Chris Hyman v.' + VERSION, DARKGRAY, verFont)
    verRect.bottomright = (WINDOWWIDTH-2, WINDOWHEIGHT-2)
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, verRect)
    DISPLAYSURF.blit(verSurf, verRect)
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def checkQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
