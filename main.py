import sys
import os
import pygame
pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Game Title")

walkRight = [pygame.image.load(os.path.join('assets', 'R1.png')), pygame.image.load(os.path.join('assets', 'R2.png')), pygame.image.load(os.path.join('assets', 'R3.png')), pygame.image.load(os.path.join('assets', 'R4.png')), pygame.image.load(os.path.join('assets', 'R5.png')), pygame.image.load(os.path.join('assets', 'R6.png')), pygame.image.load(os.path.join('assets', 'R7.png')), pygame.image.load(os.path.join('assets', 'R8.png')), pygame.image.load(os.path.join('assets', 'R9.png'))]

walkLeft = [pygame.image.load(os.path.join('assets', 'L1.png')), pygame.image.load(os.path.join('assets', 'L2.png')), pygame.image.load(os.path.join('assets', 'L3.png')), pygame.image.load(os.path.join('assets', 'L4.png')), pygame.image.load(os.path.join('assets', 'L5.png')), pygame.image.load(os.path.join('assets', 'L6.png')), pygame.image.load(os.path.join('assets', 'L7.png')), pygame.image.load(os.path.join('assets', 'L8.png')), pygame.image.load(os.path.join('assets', 'L9.png'))]

bg = pygame.image.load(os.path.join('assets', 'bg.jpg'))
char = pygame.image.load(os.path.join('assets', 'standing.png'))
bulletSound = pygame.mixer.Sound(os.path.join('assets','bullet.mp3'))
hitSound = pygame.mixer.Sound(os.path.join('assets', 'hit.mp3'))
music = pygame.mixer.music.load(os.path.join('assets', 'music.mp3'))
pygame.mixer.music.play(-1)
font = pygame.font.SysFont("comicsans", 30, True)
clock = pygame.time.Clock()
score = 0

class player(object):
    def __init__(self, x, y, width, height):
      self.x = x
      self.y = y
      self.width = width
      self.height = height 
      self.vel = 5
      self.isJump = False
      self.left = False
      self.right = True
      self.walkCount = 0
      self.jumpCount = 10
      self.standing = True
      self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, DISPLAYSURF):
      if self.walkCount + 1>= 27:
        self.walkCount = 0
      if not (self.standing):
        if self.left:        
          DISPLAYSURF.blit(walkLeft[self.walkCount//3], (self.x, self.y))
          self.walkCount += 1
        elif self.right:
          DISPLAYSURF.blit(walkRight[self.walkCount//3], (self.x, self.y))
          self.walkCount += 1
      else:
        if self.right:
          DISPLAYSURF.blit(walkRight[0], (self.x, self.y))
        else:
          DISPLAYSURF.blit(walkLeft[0], (self.x, self.y))
      self.hitbox = (self.x + 17, self.y + 11, 29, 52)
      # pygame.draw.rect(DISPLAYSURF, (255,0,0), self.hitbox,2)
      
    def hit(self):
      self.isJump = False
      self.JumpCount = 10
      self.x = 60
      self.y = 410
      self.walkCount = 0
      font1 = pygame.font.SysFont('comicsans', 100)
      text = font1.render('-5', 1, (255,0,0))
      DISPLAYSURF.blit(text, (250 - (text.get_width()/2),200))
      pygame.display.update()
      i = 0
      while i < 50:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            i = 301
            pygame.quit()

    
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, DISPLAYSURF):
      pygame.draw.circle(DISPLAYSURF, self.color, (self.x, self.y), self.radius)

class enemy(object):
  walkRight = [pygame.image.load(os.path.join('assets', 'R1E.png')), pygame.image.load(os.path.join('assets', 'R2E.png')), pygame.image.load(os.path.join('assets', 'R3E.png')), pygame.image.load(os.path.join('assets', 'R4E.png')), pygame.image.load(os.path.join('assets', 'R5E.png')), pygame.image.load(os.path.join('assets', 'R6E.png')), pygame.image.load(os.path.join('assets', 'R7E.png')), pygame.image.load(os.path.join('assets', 'R8E.png')), pygame.image.load(os.path.join('assets', 'R9E.png')), pygame.image.load(os.path.join('assets', 'R10E.png')), pygame.image.load(os.path.join('assets', 'R11E.png'))]

  walkLeft = [pygame.image.load(os.path.join('assets', 'L1E.png')), pygame.image.load(os.path.join('assets', 'L2E.png')), pygame.image.load(os.path.join('assets', 'L3E.png')), pygame.image.load(os.path.join('assets', 'L4E.png')), pygame.image.load(os.path.join('assets', 'L5E.png')), pygame.image.load(os.path.join('assets', 'L6E.png')), pygame.image.load(os.path.join('assets', 'L7E.png')), pygame.image.load(os.path.join('assets', 'L8E.png')), pygame.image.load(os.path.join('assets', 'L9E.png')), pygame.image.load(os.path.join('assets', 'L10E.png')), pygame.image.load(os.path.join('assets', 'L11E.png'))]
  
  def __init__(self, x, y, width, height, end):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.path = [x, end] 
    self.walkCount = 0
    self.vel = 3
    self.health = 10
    self.visible = True
    self.hitbox = (self.x + 17, self.y + 2, 31, 57)
  # Goes inside the enemy class 
  def draw(self, DISPLAYSURF):
    self.move()
    if self.visible:
      if self.walkCount + 1>= 33: 
        self.walkCount = 0

      
      if self.vel > 0:
        DISPLAYSURF.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
        self.walkCount += 1
      else:
        DISPLAYSURF.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
        self.walkCount += 1
      self.hitbox = (self.x + 17, self.y + 2, 31, 57)
      pygame.draw.rect(DISPLAYSURF, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) # NEW
      pygame.draw.rect(DISPLAYSURF, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) # NEW


  def hit(self):
    if self.health > 0:
      self.health -= 1
    else:
      self.visible = False
      print('hit')
      hitSound.play()

  # Goes inside the enemy class
  def move(self):
    if self.vel > 0:
      if self.x < self.path[1] + self.vel:
        self.x += self.vel
      else:
        self.vel = self.vel * -1
        self.x += self.vel
        self.walkCount = 0
    else:
      if self.x > self.path[0] - self.vel:
        self.x += self.vel
      else:
        self.vel = self.vel * -1
        self.x += self.vel
        self.walkCount = 0

def redrawGameWindow():
    DISPLAYSURF.blit(bg, (0,0))
    #goblin3.draw(DISPLAYSURF)
    #goblin2.draw(DISPLAYSURF)
    goblin.draw(DISPLAYSURF)
    man.draw(DISPLAYSURF)
    text = font.render("Score:" +str(score), 1, (0,0,0))
    DISPLAYSURF.blit(text, (360,10))
    for bullet in bullets:
      bullet.draw(DISPLAYSURF)

    pygame.display.update()



  #mainloop
shootLoop = 0

goblin = enemy(100, 410, 64, 64, 450)
#goblin2 = enemy(50, 410, 64, 64, 450)
#goblin3 = enemy(150, 410, 64, 64, 450)
man = player(200, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)
    if goblin.visible == True:
      if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
          man.hit()
          score -= 5
    if shootLoop > 0:
      shootLoop += 1
    if shootLoop > 3:
      shootLoop = 0
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
  
    for bullet in bullets:
      
      if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]: 
        if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
          goblin.hit()
          bullets.pop(bullets.index(bullet))
          score += 1



      if bullet.x < 500 and bullet.x > 0:
          bullet.x += bullet.vel
      else:
          bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()
  
    if keys[pygame.K_SPACE] and shootLoop == 0:
      if man.left:
        facing = -1
      else:
        facing = 1
        bulletSound.play()
  
      if len(bullets) < 5:
          bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (66,0,0), facing))
          shootLoop = 1
  
    if keys[pygame.K_LEFT] and man.x > man.vel:
      man.x -= man.vel
      man.left = True
      man.right = False
      man.standing = False
      
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
      man.x += man.vel
      man.right = True
      man.left = False
      man.standing = False
    else: 
      man.standing = True
      man.walkCount = 0

  
    if not(man.isJump):
      if keys[pygame.K_UP]:
        man.isJump = True
        man.walkCount = 0
    else:
      if man.jumpCount >= -10:
        neg = 1
        if man.jumpCount < 0:
          neg = -1
        man.y -= (man.jumpCount ** 2) * 0.5 * neg
        man.jumpCount -= 1
      else:
        man.isJump = False
        man.jumpCount = 10
    
  

    redrawGameWindow()
   
pygame.quit()