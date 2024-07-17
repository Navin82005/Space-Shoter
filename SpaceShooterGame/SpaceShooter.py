import pygame, random
from buffermodule import buffermodule
from tkinter import messagebox
from config import save_high_score, load_high_score

clk = pygame.time.Clock()

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(10)

font = pygame.font.SysFont("Times new Roman", 72)
scorefnt = pygame.font.SysFont("Times new Roman", 54-18)
scorefnt1 = pygame.font.SysFont("Times new Roman", 32)

try:
    height = 800
    width = 600  
    display_surface = pygame.display.set_mode((height, width))  
    score = 0
    gamecolor = (0, 20, 255)
    pygame.display.set_caption('Spacegame')
    
    icon = pygame.image.load(r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\ufo.png")
    pygame.display.set_icon(icon)
    image = pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\spaceship.png')
    bgimage = pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\spacebg.jpg')
    enemy = pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\spaceenemy.png')
    enemy1 = pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\spaceenemy.png')
    shieldpower = pygame.image.load(r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png")
    lifepower = pygame.image.load(r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\life.png")

    spx, spy = random.randint(10, height-50), 0
    spyc = 0

    lpx, lpy = random.randint(10, height-50), 0
    lpyc = 0
    lstate = False
    score4 = 0
    lifeup = False

    x, y = 400-32, 500-32
    xc, yc = 0, 0

    rx, ry = random.randint(10, height-70), 0
    ryc = 1.7

    rx1 = random.randint(10, height-70)
    ry1 = 0
    ry1c = 1.3

    streak = 0
    state = False
    cor = False
    score1 = 0
    highscore = load_high_score()  # Load the high score from the config file

    bx, by = x, y-10
    
    bulletcrash = pygame.mixer.Sound(r"C:\Program Files (x86)\PandaGames\SpaceShooter\sounds\impact-explode.wav")
    explode = pygame.mixer.Sound(r"C:\Program Files (x86)\PandaGames\SpaceShooter\sounds\impact-explode.wav")
    bulletfire = pygame.mixer.Sound(r"C:\Program Files (x86)\PandaGames\SpaceShooter\sounds\laser-effect-contact.wav")
    ebulletfire = pygame.mixer.Sound(r"C:\Program Files (x86)\PandaGames\SpaceShooter\sounds\072782_bullet-39717.wav")
    allout = pygame.mixer.Sound(r"C:\Program Files (x86)\PandaGames\SpaceShooter\sounds\game-over1.wav")
    powerupmsc = pygame.mixer.Sound(r"C:\Program Files (x86)\PandaGames\SpaceShooter\sounds\retro_gaming-fpowerup.wav")
    powerupchannel1 = pygame.mixer.Channel(6)
    powerupchannel2 = pygame.mixer.Channel(7)
    powerupchannel3 = pygame.mixer.Channel(8)

    spp = False
    score2 = 0
    simstate = False
    eby = 0
    score5 = 0
    
    speedpower = buffermodule.speeder()
    shieldpower = buffermodule.shielder()

    enemy1state = False

    def lifepowerup():
        global x, y, xc, yc, lpyc, lpx, lpy, score, lstate, score4, lifeup, streak, powerupchannel3
        if lifeup == True and score != 0:
            display_surface.blit(lifepower, (lpx, lpy))
            lpyc = 2.7
            powerupcatch(lpx, lpy, x, y, "life")
            if int(lpy) >= width - 30:
                lifeup = False

        else:
            if lifeup == False:
                if score % 20 == 0 and score > score4:
                    lpyc = 0
                    lpx, lpy = random.randint(10, height - 70), 0
                    lifeup = True

        score4 = score

    speedcnt = 0

    def speedpowerup():
        global x, y, xc, yc, spyc, spx, spy, score, spp, score2, powerupchannel1, xxc, yyc, simstate, speedcnt
        if spp == True:  # and score != 0:
            display_surface.blit(speedpower[0], (spx, spy))
            spyc = 2.7
            powerupcatch(spx, spy, x, y, "speed")
            if int(spy) >= width - 30:
                spp = False

        else:
            if spp == False:
                if simstate == True:
                    if speedcnt >= len(speedpower) - 1:
                        speedcnt = 0
                    speedcnt += 0.1
                    display_surface.blit(speedpower[int(speedcnt)], (x + 16, y + 16))

                if score % 15 == 0 and score > score2:
                    spyc = 0
                    spx, spy = random.randint(10, height - 70), 0
                    spp = True
                if powerupchannel1.get_busy() == 0:
                    xxc = 3.5
                    yyc = 3.5
                    simstate = False

        score2 = score

    shield = False
    score3 = 0
    hpx, hpy, hpyc = random.randint(10, height - 50), 0, 0
    collcon = True
    shimstate = False
    shieldcnt = 0
    scoreing = 0

    def shieldpowerup():
        global x, y, hpyc, hpx, hpy, score, score3, powerupchannel2, shield, collcon, rx, ry, shimstate, eby, ebyc, edis, estate, shieldcnt
        if shield == True and score != 0:
            display_surface.blit(shieldpower[0], (hpx, hpy))
            hpyc = 2.7
            powerupcatch(hpx, hpy, x, y, "shield")
            if int(hpy) >= width - 30:
                shield = False

        else:
            if shield == False:
                if score % 14 == 0 and score > score3:
                    hpyc = 0
                    hpx, hpy = random.randint(10, height - 70), 0
                    shield = True
                if collcon == False and powerupchannel2.get_busy() == 1:
                    if shimstate == True:
                        if shieldcnt >= len(shieldpower) - 1:
                            shieldcnt = 0
                        shieldcnt += 0.1
                        display_surface.blit(
                            shieldpower[int(shieldcnt)], (x + 16, y + 16)
                        )
                    dis = ((x - rx) ** 2 + (y - ry) ** 2) ** 0.5
                    if int(dis) <= 50:
                        rx = random.randint(10, height - 70)
                        ry = 0
                        pygame.mixer.Channel(1).play(explode)
                        collcon = True
                        shimstate = False
                        powerupchannel2.stop()
                    edis = ((rx - x) ** 2 + (eby - y) ** 2) ** 0.5
                    if int(edis) <= 50:
                        ebyc = 2
                        edis = 0
                        estate = True
                        shimstate = False
                        powerupchannel2.stop()
                else:
                    collcon = True

        score3 = score

    def powerupcatch(x1, y1, x2, y2, mode):
        global xc, yc, spp, xxc, yyc, collcon, shield, simstate, shimstate, streak, lifeup
        powdis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if mode == "speed" and int(powdis) <= 60:
            xxc = 4.2
            yyc = 4.2
            if not powerupchannel1.get_busy():
                powerupchannel1.play(powerupmsc)
                spp = False
                simstate = True

        if mode == "shield" and int(powdis) <= 60:
            collcon = False
            shield = False
            shimstate = True
            if not powerupchannel2.get_busy():
                powerupchannel2.play(powerupmsc)
        if mode == "life" and int(powdis) <= 60:
            if streak != 0:
                streak -= 1
            lifeup = False
            if not powerupchannel3.get_busy():
                powerupchannel3.play(powerupmsc)

    def bultfir():
        global state, cor, bx, by, x, y, rx, ry, score, ryc, score1, highscore, estate, ebyc
        if not cor:
            cor = True
            bx = x
            by = y
            bulletfire.set_volume(0.6)
            pygame.mixer.Channel(1).play(bulletfire)
            if y <= width - 100:
                y += 5
        by -= 10
        bullet = pygame.image.load(
            r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\bullet.png"
        )
        display_surface.blit(bullet, (bx, by))
        if int(by) <= 0:
            state = False
            cor = False
        if state:
            dis1 = ((rx - bx) ** 2 + (ry - by) ** 2) ** 0.5
            if int(dis1) <= 45:
                score += 1
                rx = random.randint(10, height - 70)
                ry = 0
                state = False
                cor = False
                bulletcrash.set_volume(0.45)
                pygame.mixer.Channel(1).play(bulletcrash)
                estate = False
        if score > highscore:
            highscore = score
            save_high_score(highscore)

        if score % 15 == 0 and score > score1:
            ryc += 0.2
            ebyc += 0.2
        score1 = score

    ebyc = 2
    x11 = 0
    y11 = 0
    estate = False

    def enemyfire():
        global score, rx, ry, ebyc, x, y, xc, yc, streak, game, state, cor, estate, collcon, eby, x11, y11
        if score % 5 == 0 and game == False and estate == False and score != 0:
            eby = ry + ebyc
            if ebyc == 2:
                ebulletfire.set_volume(0.4)
                pygame.mixer.Channel(2).play(ebulletfire)
            bullete = pygame.image.load(
                r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\ebullet.png"
            )
            display_surface.blit(bullete, (rx, eby))
            ebyc += 2
            if int(eby) == 550:
                ebyc = 2
                enemyfire()
            edis = ((rx - x) ** 2 + (eby - y) ** 2) ** 0.5
            if int(edis) <= 50 and collcon == True and x11 == x and y11 == y:
                x, y = 400 - 32, 500 - 32
                xc = 0
                yc = 0
                rx = random.randint(10, height - 70)
                ry = 0
                streak += 1
                ebyc = 2
                explode.set_volume(0.5)
                pygame.mixer.Channel(1).play(explode)

            ebdis = ((rx - bx) ** 2 + (eby - by) ** 2) ** 0.5
            if int(ebdis) <= 50:
                eby = ry
                state = False
                cor = False
                ebyc = 2
                estate = True
                bulletcrash.set_volume(0.5)
                pygame.mixer.Channel(1).play(bulletcrash)
            x11, y11 = x, y
        else:
            ebyc = 2

    def rectfall(y):
        global rx, ry, streak
        display_surface.blit(enemy, (rx, y))
        if int(y) == 600 - 70:
            rx = random.randint(10, height - 70)
            ry = 0
            streak += 1

    dis = 0

    def colletion(x1, y1, x2, y2):
        global xc, yc, x, y, streak, rx, ry, dis, collcon
        if collcon == True:
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if dis <= 50:
                x, y = 400 - 32, 500 - 32
                xc = 0
                yc = 0
                rx = random.randint(10, height - 70)
                ry = 0
                streak += 1
                pygame.mixer.Channel(4).play(explode)

    def bgsplay():
        global voice
        voice = pygame.mixer.Channel(0)
        if not voice.get_busy():
            sound = pygame.mixer.Sound(
                r"C:\Program Files (x86)\PandaGames\SpaceShooter\sounds\flying-saucer-26373.wav"
            )
            sound.set_volume(0.5)
            voice.play(sound, 1000)

    def doubleenemy():
        global rx1, ry1, streak, xc, yc, x, y, dis, collcon, score5, enemy1state, score, cor, state, mod, highscore, ry1c
        if score % 12 == 0 and score5 < score:
            enemy1state = True
        else:
            if enemy1state == False:
                rx1 = random.randint(10, height - 70)
                ry1 = 0

        if enemy1state == True:
            display_surface.blit(enemy1, (rx1, ry1))
            ry1c = 1.3
            if int(ry1) == 520:
                rx1 = random.randint(10, height - 70)
                ry1 = 0
                streak += 1

            dis2 = ((bx - rx1) ** 2 + (by - ry1) ** 2) ** 0.5
            if int(dis2) <= 45:
                score += 1
                rx1 = random.randint(10, height - 70)
                ry1 = 0
                ry1c = 0
                enemy1state = False
                cor = False
                state = False
                pygame.mixer.Channel(4).play(explode)

        if collcon == True:
            x1 = int(x)
            x2 = int(rx1)
            y1 = int(y)
            y2 = int(ry1)
            dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if dis <= 50:
                x, y = 400 - 32, 500 - 32
                xc = 0
                yc = 0
                rx1 = random.randint(10, height - 70)
                ry1 = 0
                streak += 1
                enemy1state = False
                pygame.mixer.Channel(4).play(explode)
            x1, x2, y1, y2 = 0, 0, 0, 0
        if score > highscore:
            highscore = score

        score5 = score

    game = False
    voice = None
    xxc = 3.5
    yyc = 3.5
    run = True

    while run:
        display_surface.blit(bgimage, (0, 0))
        pygame.draw.rect(
            display_surface, gamecolor, pygame.Rect(0, 0, height, width), 10
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type:
                if event.type == pygame.KEYDOWN:
                    key_name = pygame.key.name(event.key).upper()
                    if key_name == "ESCAPE":
                        run = False
                    if key_name == "UP":
                        yc = -yyc
                    if key_name == "DOWN":
                        yc = yyc
                    if key_name == "LEFT":
                        xc = -xxc
                    if key_name == "RIGHT":
                        xc = xxc
                    if key_name == "SPACE":
                        if not state:
                            state = True
                    if key_name in ["SPACE", "RIGHT", "LEFT", "DOWN", "UP"]:
                        pass
                    if game == True:
                        if key_name in ["ENTER", "RETURN"]:
                            bx, by = x, y - 10
                            rx, ry = random.randint(10, height - 70), 0
                            ryc = 1.7
                            x, y = 400 - 32, 500 - 32
                            xc, yc = 0, 0
                            game = False
                            streak = 0
                            score = 0

                if event.type == pygame.KEYUP:
                    key_name = pygame.key.name(event.key).upper()
                    if key_name in ["UP", "DOWN"]:
                        yc = 0
                    if key_name in ["LEFT", "RIGHT"]:
                        xc = 0

        x += xc
        y += yc
        spy += spyc
        hpy += hpyc
        lpy += lpyc
        ry1 += ry1c

        if x >= 800 - 70 or x <= 6:
            xc = 0
        if y >= 600 - 70 or y <= 6:
            yc = 0

        if streak < 3:
            rectfall(ry)
            display_surface.blit(image, (x, y))
        else:
            game = True
            voice.stop()
            state = False
            pygame.mixer.Channel(4).stop()
            if not pygame.mixer.Channel(5).get_busy() and out == 0:
                allout.set_volume(0.5)
                pygame.mixer.Channel(5).play(allout)
                out = 1
            if score != 0:
                scoreing = score
                score = 0
            xxc = 3.5
            yyc = 3.5
            ebyc = 10
            simstate = False
            shimstate = False
            life = False
            spp = False
            shield = False
            enemy1state = False
            powerupchannel1.stop()
            powerupchannel2.stop()
            powerupchannel3.stop()
            txt = font.render("Game Over", True, (255, 0, 0))
            scoretxt1 = scorefnt.render(f"Your Score {scoreing}", True, (0, 0, 255))
            scoretxt2 = scorefnt.render(f"High Score {highscore}", True, (0, 0, 255))
            display_surface.blit(
                txt,
                (
                    (height / 2) - txt.get_width() // 2,
                    (width / 2) - (txt.get_height() // 2) - 50,
                ),
            )
            display_surface.blit(
                scoretxt1,
                (
                    (height / 2) - scoretxt1.get_width() // 2,
                    (width / 2) - scoretxt1.get_height() // 2 + 10,
                ),
            )
            display_surface.blit(
                scoretxt2,
                (
                    (height / 2) - scoretxt2.get_width() // 2,
                    (width / 2) - scoretxt2.get_height() // 2 + 50,
                ),
            )
            replaytxt = scorefnt.render(
                "Press enter to play again | esc to exit", True, (0, 255, 255)
            )
            display_surface.blit(
                replaytxt,
                (
                    (height / 2) - replaytxt.get_width() // 2,
                    (width) - replaytxt.get_height() - 20,
                ),
            )

        colletion(x, y, rx, ry)

        if not game:
            out = 0
            scoretxt = scorefnt1.render(f"Score: {score}", True, (0, 255, 255))
            display_surface.blit(scoretxt, (20, 20))
            streaktxt = scorefnt1.render("Life: ", True, (0, 255, 255))
            display_surface.blit(streaktxt, (height - streaktxt.get_width() - 120, 20))
            highscoretxt = scorefnt1.render(
                f"Highscore: {highscore}", True, (0, 255, 255)
            )
            display_surface.blit(
                highscoretxt, ((height // 2) - highscoretxt.get_width() // 2, 20)
            )

            if streak == 0:
                j = 32
                for i in range(3):
                    life = pygame.image.load(
                        r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\life.png"
                    )
                    display_surface.blit(
                        life, (height - streaktxt.get_width() - 80 + j, 25)
                    )
                    j += 32
            if streak == 1:
                j = 32
                for i in range(2):
                    life = pygame.image.load(
                        r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\life.png"
                    )
                    display_surface.blit(
                        life, (height - streaktxt.get_width() - 80 + j, 25)
                    )
                    j += 32
                life = pygame.image.load(
                    r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\life-dead.png"
                )
                display_surface.blit(
                    life, (height - streaktxt.get_width() - 80 + j, 25)
                )
            if streak == 2:
                j = 32
                for i in range(1):
                    life = pygame.image.load(
                        r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\life.png"
                    )
                    display_surface.blit(
                        life, (height - streaktxt.get_width() - 80 + j, 25)
                    )
                    j += 32
                for i in range(2):
                    life = pygame.image.load(
                        r"C:\Program Files (x86)\PandaGames\SpaceShooter\images\life-dead.png"
                    )
                    display_surface.blit(
                        life, (height - streaktxt.get_width() - 80 + j, 25)
                    )
                    j += 32
            pygame.draw.rect(
                display_surface, gamecolor, pygame.Rect(0, width - 10, 1000, 20)
            )
            pygame.draw.rect(display_surface, gamecolor, pygame.Rect(0, 70, 1000, 6))

        if state:
            bultfir()

        doubleenemy()

        speedpowerup()
        shieldpowerup()
        lifepowerup()

        bgsplay()

        enemyfire()

        ry += ryc
        pygame.display.update()
        clk.tick(60)

except Exception as error:
    messagebox.showerror(message=error)
