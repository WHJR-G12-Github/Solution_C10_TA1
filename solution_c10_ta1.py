import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
bird=pygame.Rect(100,250,30,30)
groundx=0
# Creating a variable 'speed' and initializing it to 0
speed=0
# Defining a function to make the bird move down
def movedown():
    # Declaring the variable 'speed' as global
    global speed
    # Creating a variable 'gravity' and initialize it to 0.2
    gravity=0.2
    # Incrementing 'speed' by 'gravity'
    speed=speed+gravity
    # Incrementing 'bird.y' by 'speed'
    bird.y=bird.y+speed

while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-550:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  # Calling the function 'movedown()' before displaying the bird image
  movedown()
  screen.blit(images["bird"],bird)
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
      
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
