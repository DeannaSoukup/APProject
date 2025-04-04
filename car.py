import pygame

WHITE = (255,255,255)

class Car(pygame.sprite.Sprite):
    
    #write a constructor that initializes a car
    def __init__(self, color, width, height, speed):
        #calling the parent class construtor to initialze the sprite
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        #make the surface transparent so you can see the background.  
        #The fill color and thed colorkey have to be the same
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        
        #create and initialize attributes/properties for the car objects
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.crashes = 0
        
        #draw the car on the surface
        pygame.draw.rect(self.image, color, [0,0, width, height])
        
        #fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        
    #write methods that moves the cars
    def moveRight(self, pixels):
        self.rect.x = self.rect.x + pixels
        
    def moveLeft(self, pixels):
        self.rect.x = self.rect.x - pixels
    
    def moveUp(self, pixels):
        self.rect.y = self.rect.y - pixels
    
    def moveDown(self, pixels):
        self.rect.y = self.rect.y + pixels
    
    #methods that we will use for the obstacle cars
    def moveForward(self, speed):
        self.rect.y += self.speed * speed /20
    
    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed /20
        
    def changeSpeed(self, speed):
        self.speed = speed
    
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])
    
    
    
        
        
    
    
    
    
    
        
        
        
        
        