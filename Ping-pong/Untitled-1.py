from pygame import*
from random import randint
mixer.init() 
mixer.music.load("04. Mii Plaza.mp3")
mixer.music.play()
ping = mixer.Sound("ping.mp3")
win_width = 700
win_height = 600
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load("table.png"), (700, 600)) 
game = True
finish = False
clock = time.Clock()
FPS = 60
countp1 = 0
countp2 = 0
scorer = 0 
scoreb = 0
counter = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def lreset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self): 
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= -5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y <= 430: 
            self.rect.y += self.speed 
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y <= 430: 
            self.rect.y += self.speed 
racket1 = Player("red.png", 30, 200, 6, 30, 200)
racket2 = Player("blue.png", 650, 200, 6, 30, 200)
ball = GameSprite("ball.png", 300, 350 , 1, 50, 50)
font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 35)
win1 = font1.render("PLAYER 1 WON", True, (0, 200, 0))
win2 = font1.render("PLAYER 2 WON", True, (0, 200, 0))
rscore = font2.render("Score:" + str(scorer), True, (255, 0, 0))
bscore = font2.render("Score:" + str(scoreb), True, (0, 0, 255))
while finish != True:
    e = randint(1,2)


speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))

        racket1.update_r()
        racket2.update_l()
        racket1.lreset()
        racket2.lreset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.update()
        ball.lreset()
        window.blit(bscore, (600, 0))
        window.blit(rscore, (0, 0))

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ping.play()
            speed_x *= -1.1
            speed_y *= -1.1
           
        if ball.rect.y > 550:  
            speed_y *= -1
        if ball.rect.y == 50:
            speed_x *= -1
         

        if ball.rect.x < -20:
            scoreb += 1
            window.blit(rscore, (0, 0))
            window.blit(bscore, (600, 0))
            rscore = font2.render("Score:" + str(scorer), True, (255, 0, 0))
            bscore = font2.render("Score:" + str(scoreb), True, (0, 0, 255))
            racket1 = Player("red.png", 30, 200, 6, 30, 200)
            racket2 = Player("blue.png", 650, 200, 6, 30, 200)
            ball.rect.x = 300
            ball.rect.y = 350
            speed_x = 3
            speed_y = 3
           
           
        if ball.rect.x > 650:
            window.blit(bscore, (600, 0))
            window.blit(rscore, (0, 0))
            scorer += 1
            rscore = font2.render("Score:" + str(scorer), True, (255, 0, 0))
            bscore = font2.render("Score:" + str(scoreb), True, (0, 0, 255))
            racket1 = Player("red.png", 30, 200, 6, 30, 200)
            racket2 = Player("blue.png", 650, 200, 6, 30, 200)
            ball = GameSprite("ball.png", 300, 350 , 1, 50, 50)
            speed_x = 3
            speed_y = 3
        if ball.rect.y < 0:
            speed_x *= -1.1
            speed_y *= -1.1
        if scorer >= 3 :
            window.blit(rscore, (0, 0))
            window.blit(win1, (200, 300))
            speed_x = 0
            speed_y = 0
            finish = True
        if scoreb >= 3:
            window.blit(bscore, (600, 0))
            window.blit(win2, (200, 300))
            speed_x = 0
            speed_y = 0
            finish = True
        

            
            


    display.update()  
    clock.tick(FPS)