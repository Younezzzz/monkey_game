import pygame
import random

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((563,337))
pygame.display.set_caption("Макака поймала банан")
#icon = pygame.image.load('')
# pygame.display.set_icon()

square = pygame.Surface((50,50))
square.fill('red')


bg = pygame.image.load('images/bg.jpg').convert()

# bg_sound = pygame.mixer.Sound('sound/bg_sound.mp3')
# bg_sound.play()


walk_left = [
    pygame.image.load('images/player_left/1.png'),
    pygame.image.load('images/player_left/2.png'),
    pygame.image.load('images/player_left/3.png'),
    pygame.image.load('images/player_left/4.png')]
walk_right = [
    pygame.image.load('images/player_right/1.png'),
    pygame.image.load('images/player_right/2.png'),
    pygame.image.load('images/player_right/3.png'),
    pygame.image.load('images/player_right/4.png')]
player_anim_count = 0
player_speed = 10
player_x = 150
player_y = 225
is_jump = False
jump_cnt = 7
bg_x = 0
banana = pygame.image.load('images/banana.png').convert_alpha()
grape = pygame.image.load('images/grape.png').convert_alpha()
bomb = pygame.image.load('images/bomb.png').convert_alpha()
fruits = [banana,grape]
banana_y = 0
banana_x = random.randint(50,500)
fruit_timer = pygame.USEREVENT + 1
bomb_timer = pygame.USEREVENT + 1
bomb_time = 10000
time = 10000
counter = 0
lose_counter = 0
pygame.time.set_timer(fruit_timer, time)
fruit_list_in_game = []
bomb_list_in_game = []
run = True
gameplay = 4
label = pygame.font.Font('Fonts/Roboto-Regular.ttf',40)
start_text = label.render('Начать игру',False,(193,196,199))
start_rect = start_text.get_rect(topleft = (150,150))
lose_text = label.render('Ты проиграл',False, (193,196,199))
restart_text = label.render('Играть снова',False, (115,132,148))
restart_text_rect = restart_text.get_rect(topleft = (180,200))
win_text = label.render('Ты выирал',False, (193,196,199))
next_level_text = label.render('Следующий уровень',False, (115,132,148))
next_level_rect = restart_text.get_rect(topleft = (100,150))
win_game_text = label.render('Ты прошел игру!!',False, (193,196,199))
label_cnt = pygame.font.Font('Fonts/Roboto-Regular.ttf',30)
lvl_1 = 50


while run:
    if gameplay == 4:
        screen.fill((87, 88, 89))
        # screen.blit(start_text, (180, 200))
        screen.blit(start_text, start_rect)
        mouse = pygame.mouse.get_pos()
        if start_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = 1
            fruit_list_in_game.clear()
            player_x = 150
            player_y = 225
            lose_counter = 0
    elif gameplay == 1:
        counter_text = label.render(f'{counter}/{lvl_1}', False, 'black')
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 563, 250))
        screen.blit(counter_text,(430,20))
        keys = pygame.key.get_pressed()
        screen.blit(walk_left[0], (player_x, player_y))
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        if keys[pygame.K_RIGHT]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        player_rect = walk_left[0].get_rect(topleft=(player_x,player_y))
        if bomb_list_in_game:
            for el_bomb in bomb_list_in_game:
                screen.blit(bomb,el_bomb)
                el_bomb.y += 7
            if player_rect.colliderect(el_bomb):
                gameplay = False
        if fruit_list_in_game:
            for (i,el) in enumerate(fruit_list_in_game):
                screen.blit(fruit, el)
                el.y+=5
                time+=2000
                if el.y>330:
                    fruit_list_in_game.pop(i)
                    lose_counter+=1
                    print(lose_counter)
                    if lose_counter == 8:
                        gameplay = False
            if player_rect.colliderect(el):
                fruit_list_in_game.pop(i)
                counter +=10
                if counter==150:
                    gameplay = 3
                if counter==50:
                    gameplay = 2
                    lvl_1 = 100

                print(counter)


        if keys[pygame.K_LEFT] and player_x > 10:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT]:
            player_x+=player_speed
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if  jump_cnt >= -7:
                if jump_cnt > 0:
                    player_y -= (jump_cnt**2)//2
                else:
                    player_y += (jump_cnt**2)//2
                jump_cnt -= 1
            else:
                is_jump = False
                jump_cnt = 7

        player_anim_count+=1
        if player_anim_count==3:
            player_anim_count=0
    elif gameplay == 2:
        screen.fill((87, 88, 89))
        screen.blit(win_text, (180, 100))
        screen.blit(next_level_text, next_level_rect)
        mouse = pygame.mouse.get_pos()
        bg = pygame.image.load('images/bg_2.png').convert()
        if next_level_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = 1
            fruit_list_in_game.clear()
            player_x = 150
            player_y = 280
            lose_counter = 0
    elif gameplay == 3:
        bg = pygame.image.load('images/bg.jpg').convert()
        screen.fill((87, 88, 89))
        screen.blit(win_game_text, (180, 100))
        screen.blit(restart_text, restart_text_rect)
        mouse = pygame.mouse.get_pos()
        screen.blit(restart_text, restart_text_rect)
        if restart_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = 1
            fruit_list_in_game.clear()
            player_x = 150
            player_y = 200
            counter = 0
            lose_counter = 0
    else:
        screen.fill((87,88,89))
        screen.blit(lose_text,(180,100))
        screen.blit(restart_text,restart_text_rect)

        mouse = pygame.mouse.get_pos()
        if restart_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = 1
            fruit_list_in_game.clear()
            player_x = 150
            player_y = 225
            counter = 0
            lose_counter = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == fruit_timer:
            fruit_list_in_game.append(banana.get_rect(topleft=(random.randint(50,500),banana_y)))
            fruit = fruits[random.randint(0, len(fruits) - 1)]
        if event.type == bomb_timer:
            bomb_list_in_game.append(bomb.get_rect(topleft=(random.randint(50,500),banana_y)))




    clock.tick(10)


