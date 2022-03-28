# imports
import pygame, os, sys

# center pygame window on display
# technique found at https://stackoverflow.com/questions/5814125/how-to-designate-where-pygame-creates-the-game-window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# initialize pygame
pygame.init()

# constants
WIDTH = 400
HEIGHT = 400
FPS = 3

# RGB colors
white = (255, 255, 255)
black = (0, 0, 0)

skyBlue = (135, 206, 235)
pink = (255,192,203)
vanta = (0,1,0)
# variables
image_count = 0 # counter for images
clock = pygame.time.Clock() # clock object
running = True
timer = 0

# load images into pygame
my_images = [
  pygame.image.load('./assets/pyramid1.png'),
  pygame.image.load('./assets/pyramid2.png'),
  pygame.image.load('./assets/pyramid3.png')
]

# changes size of all images to fit screen
for i in range(len(my_images)):
    my_images[i] = pygame.transform.scale(my_images[i], 
    (300, 300))

# set Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pyramid Animation")
WINDOW.fill(skyBlue)


# set up your font
font = pygame.font.Font('./fonts/NunitoSans-Black.ttf', 15)

# create your text
text = font.render('Pyramids, drawn by Zayn Abada,', True, black, skyBlue)
text2 = font.render('animated by David Bates and Cade Fandl.', True, black, skyBlue)
text_rect = text.get_rect()
text2_rect = text2.get_rect()

# position the text
text_rect.center = (WIDTH // 2, HEIGHT // 12)
text2_rect.center = (WIDTH // 2, HEIGHT // 6)


# display text
WINDOW.blit(text, text_rect)
WINDOW.blit(text2, text2_rect)
pygame.display.flip()

# draw shape function
def drawShape():
  global my_images
  global image_count
  if (image_count == 3):
    image_count = 0
  WINDOW.blit(my_images[image_count], (55, 100))
  pygame.display.flip()
  image_count += 1
  
# main animation Loop that will run for 10 seconds
while running and timer < 50:

  # upadate screen according to FPS value
  clock.tick(FPS)

  # update timer
  timer += 1

  # check if "X" is clicked by user 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      sys.exit()

  # call to drawShape function
  drawShape()