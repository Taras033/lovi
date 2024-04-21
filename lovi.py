#Создай собственный Шутер!
from random import *
from pygame import *
from time import time as timer
mixer.init()
#mixer.music.load('c26baac1db252bd.mp3')
#mixer.music.play()




win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Лови!')
background = transform.scale(image.load('fon1.png'), (win_width, win_height))
FPS = 60
clock = time.Clock()



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x < 595:
            self.rect.x += 10
        if keys_pressed[K_d] and self.rect.x > 5:
            self.rect.x -= 10




player = Player('player.png', 295, 400, 5, 60, 60)
score = 0
lost = 0
font.init()
font1 = font.SysFont('Arial', 36)
font = font.SysFont('Arial', 70)
win = font.render('YOU WON!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (255, 215, 0))



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 400:
            self.rect.x = randint(80, 650)
            self.rect.y = 0
            lost = lost + 1          
monsters = sprite.Group()
for i in range(5):
    monster = Enemy('lovi1.png', randint(80, 650), 0, randint(2, 6), 60, 60)
    monsters.add(monster)
monsters2 = sprite.Group()
for i in range(5):
    monster2 = Enemy('lovi2.png', randint(80, 650), 0, randint(2, 6), 60, 60)
    monsters2.add(monster2)





ur1 = True
ur2 = False
ur3 = False


finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:  
            game = False
    if finish != True:
        window.blit(background,(0,0))
        player.reset()
        player.update()
        if ur1 == True:
            monsters.draw(window)
            monster.update()
            sprite_list = sprite.spritecollide(player, monsters, True)
            for i in sprite_list:
                score += 1
                monster = Enemy('lovi1.png', randint(80, 650), 0, randint(2, 6), 60, 60)
                monsters.add(monster)
            if  score >= 10:
                ur1 = False
                ur2 = True
                ur3 = False
                for monster in monsters:
                    monster.kill()



        # #if ur2 == True:
        #     sprite_list2 = sprite.spritecollide(player, monsters2, True)
        #     for i in sprite_list2:
        #         score += 1
        #         monster2 = Enemy('lovi1.png', randint(80, 650), 0, randint(2, 6), 60, 60)
        #         monsters2.add(monster2)



        text = font1.render("Счёт:" + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font1.render("Пропущено:" + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 30))
        window.blit(text, (10, 10))
        display.update()

    time.delay(15)
