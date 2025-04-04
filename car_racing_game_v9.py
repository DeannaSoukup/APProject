#import pygame and initialize it
#and import the random library
import pygame, random
pygame.init()

#from the car file, import the Car class
from car import Car

#define the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)   
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
HOT_PINK = (255,105,180)
GREY = (128,128,128)
PURPLE = (128,0,128)

colors = [BLACK, WHITE, GREEN, BLUE, YELLOW, PURPLE, ORANGE, HOT_PINK, PURPLE]

# Set the height and width of the screen (width, height).
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing Game")

all_sprites_list = pygame.sprite.Group()

# create a car object in the memory
player1car = Car(RED, 20, 30, 70)
player1car.rect.x = 200/700 * SCREEN_WIDTH
player1car.rect.y = 400/500 * SCREEN_HEIGHT
all_sprites_list.add(player1car)

player2car = Car(PURPLE, 20, 30, 70)
player2car.rect.x = 400/700 * SCREEN_WIDTH
player2car.rect.y = 400/500 * SCREEN_HEIGHT
all_sprites_list.add(player2car)

car1 = Car(YELLOW, 20, 30, random.randint(50, 100) )
car1.rect.x = random.randint(0, SCREEN_WIDTH - 20)
car1.rect.y = random.randint(-150, -50)
all_sprites_list.add(car1)

car2= Car(GREEN, 20, 30, random.randint(50, 100) )
car2.rect.x = random.randint(0, SCREEN_WIDTH - 20)
car2.rect.y = random.randint(-150, -50)
all_sprites_list.add(car2)

car3 = Car(GREEN, 20, 30, random.randint(50, 100) )
car3.rect.x = random.randint(0, SCREEN_WIDTH - 20)
car3.rect.y = random.randint(-150, -50)
all_sprites_list.add(car3)

car4 = Car(GREEN, 20, 30, random.randint(50, 100) )
car4.rect.x = random.randint(0, SCREEN_WIDTH - 20)
car4.rect.y = random.randint(-150, -50)
all_sprites_list.add(car4)

oncoming_cars = pygame.sprite.Group()
oncoming_cars.add(car1)
oncoming_cars.add(car2)
oncoming_cars.add(car3)
oncoming_cars.add(car4)


#sets the starting speed of the car before the game loop
playerCarSpeed = 5

#create a clock to control the frame rate
clock = pygame.time.Clock()

player1crashes = 0
player2crashes = 0

# Loop until the user clicks the close button

running = True
while running:
    #main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #hitting the x in the corner of the window
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1car.rect.x > SCREEN_WIDTH * 1/6:
        player1car.moveLeft(5)
    if keys[pygame.K_RIGHT] and player1car.rect.x < SCREEN_WIDTH * 5/ 6 -20:
        player1car.moveRight(5)
    if keys[pygame.K_UP] and player1car.rect.y > 0:
        player1car.moveUp(5)
    if keys[pygame.K_DOWN] and player1car.rect.y < SCREEN_HEIGHT - 20:
        player1car.moveDown(5)
        
    if keys[pygame.K_a] and player2car.rect.x > SCREEN_WIDTH * 1/6:
        player2car.moveLeft(5)
    if keys[pygame.K_d] and player2car.rect.x < SCREEN_WIDTH * 5/ 6 -20:
        player2car.moveRight(5)
    if keys[pygame.K_w] and player2car.rect.y > 0:
        player2car.moveUp(5)
    if keys[pygame.K_s] and player2car.rect.y < SCREEN_HEIGHT - 20:
        player2car.moveDown(5)
    
    #game logic goes here
    for car in oncoming_cars:
        car.moveForward(5)
        if car.rect.y > SCREEN_HEIGHT:
            car.changeSpeed(random.randint(20, 50))
            car.repaint(random.choice(colors))
            car.rect.y = random.randint(-200, -100)
            car.rect.x = random.randint( int(SCREEN_WIDTH * 1/6) , int(SCREEN_WIDTH * 5/6)- 20)
            
    
    
    all_sprites_list.update()
    
    
    player1car_collision_list = pygame.sprite.spritecollide(player1car, oncoming_cars, False)
    player2car_collision_list = pygame.sprite.spritecollide(player2car, oncoming_cars, False)
    
    for car in player1car_collision_list:
        player1crashes +=1
        print("Player 1 crashes " + str(player1crashes))
        car.rect.y = random.randint(-200, -100)
        
        
    
    
    
    
    #Draw code goes here
    #clear the screen to white
    screen.fill(GREEN)
    
    #draw a rectangle that is 4/6 the size of the screen
    pygame.draw.rect(screen, GREY, [SCREEN_WIDTH * 1/6 , 0 , SCREEN_WIDTH * 4/6, SCREEN_HEIGHT] )
    for i in range(1, 6):
        pygame.draw.line(screen, WHITE, [SCREEN_WIDTH * i/6, 0], [SCREEN_WIDTH * i/6, SCREEN_HEIGHT], 5)  
        
        
    #draw all the sprites
    all_sprites_list.draw(screen)
    
    font = pygame.font.Font(None, 36)
    text1 = font.render("Player 1 Crashes: " + str(player1crashes), 1, (10, 10, 10))
    screen.blit(text1, (50,50))
    
    #update the screen with what we've drawn
    pygame.display.flip()
    
    clock.tick(60)


pygame.quit()
    
