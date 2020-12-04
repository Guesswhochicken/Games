import random, sys, copy, os, pygame
pygame.init()
pygame.font.init()

win = pygame.display.set_mode((500,500))
run = True
x = 230
y = 230
q = 255
w = 151
e = 255
a = 0
color = 0
x_other = 100
y_other = 100
speed = 10
rect1 = pygame.draw.rect(win, (q,w,e), (x,y,20,20))
rect2 = pygame.draw.rect(win, (w,q,e), (x_other,y_other,20,20))

while run:
  pygame.time.delay(25)
  win = pygame.display.set_mode((500,500))
  myfont = pygame.font.SysFont('Comic Sans MS', 100)
  textsurface = myfont.render('{}'.format(a), False, (255, 255, 255))
  myFont = pygame.font.SysFont('Comic Sans MS', 1)
  textSurface = myfont.render("GAME OVER", False, (color, 0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()
      sys.exit()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    x += speed
  if keys[pygame.K_LEFT]:
    x -= speed
  if keys[pygame.K_UP]:
    y -= speed
  if keys[pygame.K_DOWN]:
    y += speed
  if keys[pygame.K_d]:
    x += speed - 1
  if keys[pygame.K_a]:
    x -= speed - 1
  if keys[pygame.K_w]:
    y -= speed - 1
  if keys[pygame.K_s]:
    y += speed - 1
  if keys[pygame.K_SPACE]:
    x = 230
    y = 230
    q = 255
    w = 151
    e = 255
    x_other = 100
    y_other = 100
    rect1 = pygame.draw.rect(win, (q,w,e), (x,y,20,20))
    rect2 = pygame.draw.rect(win, (w,q,e), (x_other,y_other,20,20))
    a = 0  
    color = 0
    speed = 10
  if x >= 481:
    q = 0
    w = 0
    e = 0
    color = 255
    speed = 0
  if x <= -1:
    q = 0
    w = 0
    e = 0
    color = 255
    speed = 0
  if y >= 491:
    q = 0
    w = 0
    e = 0
    color = 255
    speed = 0
  if y <= -1:
    q = 0
    w = 0
    e = 0
    color = 255
    speed = 0
  if x_other >= 481:
    x_other = 480
  if x_other <= -1:
    x_other = 0
  if y_other >= 481:
    y_other = 480
  if y_other <= -1:
    y_other = 0
  if rect1.colliderect(rect2):
    x_other = random.randint(-500,500)
    y_other = random.randint(-500,500)
    a += 1
  win.blit(textSurface,(20,200))
  rect1 = pygame.draw.rect(win, (q,w,e), (x,y,20,20))
  rect2 = pygame.draw.rect(win, (w,q,e), (x_other,y_other,20,20))
  win.blit(textsurface,(210,0))
  
  pygame.display.update()
