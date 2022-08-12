import pygame, sys
from button import Button

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

click_sound = pygame.mixer.Sound('sfx/click_sound_menu.wav')
click_sound.set_volume(0.2)

fullscreen = False
music = True
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
BG_PSC = pygame.image.load("skins/backgrounds/testbackground.png")
BG_PSC = pygame.transform.scale(BG_PSC,( 1080, 620))
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def bgmusic():
    pygame.mixer.music.load('sfx/MainBackgroundSound.wav')
    pygame.mixer.music.set_volume(.1)
    pygame.mixer.music.play(-1,0.0)

def play():
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#2b2a2a")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_SOCCERCARDS = Button(image=None, pos=(640, 360), 
                            text_input="Play Soccer Cards", font=get_font(75), base_color="White", hovering_color="#0ba4e0")
        PLAY_SOCCERCARDS.changeColor(PLAY_MOUSE_POS)
        PLAY_SOCCERCARDS.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                click_sound.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_SOCCERCARDS.checkForInput(PLAY_MOUSE_POS):
                    click_sound.play()
                    play_soccercards()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    click_sound.play()
                    main_menu()

        pygame.display.update()

def play_soccercards():
    while True:
        SCREEN.blit(BG_PSC, (100, 50))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=None, pos=(50, 680), 
                            text_input="X", font=get_font(25), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    click_sound.play()
                    play()

        pygame.display.update()
    
def options():
    global fullscreen
    global music
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#2b2a2a")

        if fullscreen == True:
            fullscreentxt = "Windowed"
        else:
            fullscreentxt = "Fullscreen"

        if music == False:
            musictxt = "Muted"
        else:
            musictxt = "Music"

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "WHITE")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="WHITE", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        OPTIONS_FULLSCREEN = Button(image=None, pos=(640, 260), 
                            text_input=fullscreentxt, font=get_font(75), base_color="WHITE", hovering_color="Green")

        OPTIONS_FULLSCREEN.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_FULLSCREEN.update(SCREEN)
         
        OPTIONS_MUSIC = Button(image=None, pos=(640, 360), 
                            text_input=musictxt, font=get_font(75), base_color="WHITE", hovering_color="Green")

        OPTIONS_MUSIC.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MUSIC.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                click_sound.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_FULLSCREEN.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    if fullscreen == False:
                        pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
                        fullscreen = True
                    elif fullscreen == True:
                        pygame.display.set_mode((1280, 720))
                        fullscreen = False
                if OPTIONS_MUSIC.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    if music == True:
                        pygame.mixer.music.fadeout(3000)
                        music = False
                    else:
                        bgmusic()
                        music = True
                                    
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos() 
        MENU_TEXT = get_font(120).render("MENU", True, "#e0cfb1")
        MENU_RECT = MENU_TEXT.get_rect(center=(230, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(230, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#ffffff", hovering_color="#0ba4e0")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(230, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#ffffff", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(230, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#ffffff", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_sound.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_sound.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_sound.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

bgmusic()
main_menu()