import pygame
import time
import random
import math

pygame.init()

display_width = 300
display_height = 300
radius = 30

black = (0,0,0) # RGB
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tic Tac Toe - Cyberlabs')


def textObjects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def message_display(text, locx, locy,size):
	largeText = pygame.font.Font('freesansbold.ttf', size) # Font(font name, font size)
	TextSurf, TextRec = textObjects(text, largeText)
	TextRec.center = (locx,locy)
	gameDisplay.blit(TextSurf, TextRec)
	pygame.display.update()
    


def resetScreen(gameDisplay):
    gameDisplay.fill(black)
    pygame.display.flip()
    
def initScreen(gameDisplay):
    gameDisplay.fill(black)
    pygame.draw.line(gameDisplay,white,(display_width/3,0),(display_width/3,display_height))
    pygame.draw.line(gameDisplay,white,(2*display_width/3,0),(2*display_width/3,display_height))
    pygame.draw.line(gameDisplay,white,(0,display_height/3),(display_width, display_height/3))
    pygame.draw.line(gameDisplay,white,(0,2*display_height/3),(display_width,2*display_height/3))
    pygame.display.flip()
    
def getBlock(spot):
    x = math.ceil((spot[0]/display_width) * 3)
    y = math.ceil((spot[1]/display_height) * 3)
    return (x-1,y-1)

def createMatrix():
    m = []
    for i in range(3):
        m.append([0,0,0])
    return m

def checkMatrix(matrix):
    #check rows and columns
    for i in range(3):
        if matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2] and matrix[i][0] != 0: return matrix[i][0]
        if matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i] and matrix[0][i] != 0: return matrix[0][i]
    #check left-to-right diagonal
    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[0][0] != 0: return matrix[0][0]
    #check right to left diagonal
    if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[0][2] != 0: return matrix[0][2]
    return 0
    

def gameLoop():
    gameExit = False
    turn = 1
    LMBPressed = False
    winner = 0
    matrix = createMatrix()
    initScreen(gameDisplay)
    counter = 0
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
        if pygame.mouse.get_pressed()[0] and not LMBPressed:
            LMBPressed = True
            spot = pygame.mouse.get_pos()
            i, j = getBlock(spot)
            if matrix[i][j] == 0:
                matrix[i][j] = turn
                if turn == 1: color = white
                else: color = red
                xx = display_width/3
                yy = display_height/3
                xpos = int((xx*(i+1)) - xx/2)
                ypos = int((yy*(j+1)) - yy/2)
                pygame.draw.circle(gameDisplay,color,(xpos,ypos),radius)
                pygame.display.flip()
                winner = checkMatrix(matrix)
                if turn == 2: turn = 1
                else: turn = 2
                counter += 1
        
        if LMBPressed and not pygame.mouse.get_pressed()[0]:
            LMBPressed = False
        
        if winner !=0:
            time.sleep(1)
            resetScreen(gameDisplay)
            message_display("Winner is Player: "+str(winner),int(display_width/2), int(display_height/2), 20)
            time.sleep(5)
            gameExit = True
            continue
        
        if counter == 9:
            time.sleep(1)
            resetScreen(gameDisplay)
            message_display("No Winner ",int(display_width/2), int(display_height/2), 20)
            time.sleep(5)
            gameExit = True
            
        
gameLoop()   
pygame.quit()