import pygame
import random
pygame.init()

white = (255,255,255)
screen_width = 900
screen_height = 500
play_width = 700
play_height = 400
fps=30
font = pygame.font.Font(None,34)
score=0
black=(0,0,0)



gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Conga Conga")
pygame.display.update()
clock = pygame.time.Clock()



exit_game=False
game_over=False

sprite_sheet_image = pygame.image.load("character_sheet.png").convert_alpha()
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image,(play_width,play_height))


def get_image(sheet,row,column):
    image = pygame.Surface((16,24)).convert_alpha()
    image.blit(sheet,(0,0),(16*row,24*column,16*row+16,24*row+24))
    image = pygame.transform.scale(image,(32,48))
    image.set_colorkey((0,0,0))
    return image

def over(x,y):
    global exit_game
    if x<((screen_width - play_width)/2) or x>(play_width + (screen_width - play_width)/2-32):
        exit_game=True
    if y<((screen_height - play_height)/2) or y>(play_height + (screen_height - play_height)/2-48):
        exit_game=True    


class line:
    def __init__(self,x,y):
        self.o=0
        self.p=0
        self.x=x
        self.y=y
        self.velx=0
        self.vely=0
        self.image=get_image(sprite_sheet_image,4,10)
        self.rect=self.image.get_rect()
        self.image_collec=[]
        for m in range(8):
            for n in range(3):
                self.image_collec.append(get_image(sprite_sheet_image,m,n+9))
    def dr(self):
        gameWindow.blit(self.image,(self.x,self.y))
        if self.velx!=0 or self.vely!=0:
            self.image=self.image_collec[int(self.p*3+int(self.o))]
        if self.o>2:
            self.o=0
        self.o+=0.16

    def moving(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.p=6
            self.velx=-5
            self.vely=0
        if keys[pygame.K_RIGHT]:
            self.p=2
            self.velx=5
            self.vely=0
        if keys[pygame.K_UP]:
            self.p=0
            self.velx=0
            self.vely=-5
        if keys[pygame.K_DOWN]:
            self.p=4
            self.velx=0
            self.vely=5
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.p=7
            self.velx=-3
            self.vely=-4
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.p=1
            self.velx=3
            self.vely=-4
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.p=5
            self.velx=-3
            self.vely=4
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.p=3
            self.velx=3
            self.vely=4
        




class friend:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.image=get_image(sprite_sheet_image,4,6)
    def draw(self):
        gameWindow.blit(self.image,(self.x,self.y))
    def collision(self):
        if abs(player.x - self.x)<22 and abs(player.y - self.y)<32:
            self.x=random.randint((screen_width - play_width)/2,play_width + (screen_width - play_width)/2-32)
            self.y=random.randint((screen_height - play_height)/2,play_height + (screen_height - play_height)/2-48)
            global score
            global foll
            foll=True
            score+=1
            



player=line(screen_width/2-16,screen_height/2-24)
frnd=friend(random.randint((screen_width-play_width)/2,play_width+(screen_width-play_width)/2-32),random.randint((screen_height-play_height)/2,play_height+(screen_height-play_height)/2-48))
follow=[player]


while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
    
    player.moving()
    player.x+=player.velx
    player.y+=player.vely
    gameWindow.fill(white)


    gameWindow.blit(background_image,((screen_width - play_width)/2,(screen_height - play_height)/2))
    player.dr()
    frnd.draw()
    frnd.draw()
    score_text = font.render(f"Followers: {score}",True,(black))
    frnd.collision()
    gameWindow.blit(score_text,(screen_width/2-18*4,(screen_height-play_height)/2+play_height+15))
    over(player.x,player.y)
    pygame.display.update()
    clock.tick(fps)
    

pygame.quit()
quit()            