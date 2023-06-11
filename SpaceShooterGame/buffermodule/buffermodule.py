import pygame
from tkinter import messagebox

try:
    def getimg(img, frame, width, height, scale, colorkey = (0, 0, 0)):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(img, (0, 0), ((frame)*width, 0, width, height))
        image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        image.set_colorkey(colorkey)
        return image

    def speeder():
        speedpower = [getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        ]

        for i in range(100):
            speedpower.insert(0, getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\speed.png'), 0, 32, 32, 1))
        
        return speedpower

    def shielder():
        shieldpower = [getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\bufferblinker.png'), 0, 32, 32, 1),
        ]

        for i in range(100):
            shieldpower.insert(0, getimg(pygame.image.load(r'C:\Program Files (x86)\PandaGames\SpaceShooter\images\shield.png'), 0, 32, 32, 1))
        
        return shieldpower

except Exception as e:
    messagebox.showerror(message=e)