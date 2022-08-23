import pygame, sys, random
from button import Button

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

clock = pygame.time.Clock()
music = True
click_sound = pygame.mixer.Sound('sfx/click_sound_menu.wav')
click_sound.set_volume(0.2)

def bgmusic():
    pygame.mixer.music.load('sfx/MainBackgroundSound.wav')
    pygame.mixer.music.set_volume(.1)
    pygame.mixer.music.play(-1,0.0)

fullscreen = False
SCREEN = pygame.display.set_mode((1280, 720))
BG_PSC_SELECT = 0
BG = pygame.image.load("assets/Background.png")

def BG_PSC_LOAD():
    # Lädt den Cardsoccer background und je nach einstellung ändert sich dieser
    global BG_PSC_SELECT
    print(BG_PSC_SELECT)
    if BG_PSC_SELECT == 0:
        BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield.png")
    elif BG_PSC_SELECT == 1:
        BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield fire and water.png")
    elif BG_PSC_SELECT == 2:
        BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield fire and ice.png")
    elif BG_PSC_SELECT == 3:
        BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/testbackground.png")
    else:
        BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield.png")

    BG_PSC = pygame.transform.scale(BG_PSC,( 1180, 620))
    SCREEN.blit(BG_PSC, (50, 50))

SPRITE_TP = (0, 0, 0)
sprite_sheet_image = pygame.image.load("assets/cards/testcards5.png").convert_alpha()

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def play():

    pygame.display.set_caption("Game Selection")

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

    global BG_PSC_SELECT
    
    pygame.display.set_caption("Card Soccer")

    P1 = 0
    P2 = 0
    G1 = 0
    G2 = 0
    F1 = 0
    F2 = 0
    R11 = 0
    R12 = 0
    R13 = 0
    R21 = 0
    R22 = 0
    R23 = 0
    R31 = 0
    R32 = 0
    R33 = 0
    R41 = 0
    R42 = 0
    R43 = 0
    CLICK = 0
    MOUSE_POS_P1 = False
    MOUSE_POS_P2 = False
    MOUSE_POS_G1 = False
    MOUSE_POS_G2 = False
    MOUSE_POS_F1 = False
    MOUSE_POS_F2 = False
    MOUSE_POS_R11 = False
    MOUSE_POS_R12 = False
    MOUSE_POS_R13 = False
    MOUSE_POS_R21 = False
    MOUSE_POS_R22 = False
    MOUSE_POS_R23 = False    
    MOUSE_POS_R31 = False
    MOUSE_POS_R32 = False
    MOUSE_POS_R33 = False
    '''CARDS_52 = [HERZ_2, HERZ_3, HERZ_4, HERZ_5, HERZ_6, HERZ_7, HERZ_8, HERZ_9, HERZ_10, HERZ_JACK, HERZ_QUEEN, HERZ_KING, HERZ_ASS,
            KARO_2, KARO_3, KARO_4, KARO_5, KARO_6, KARO_7, KARO_8, KARO_9, KARO_10, KARO_JACK, KARO_QUEEN, KARO_KING, KARO_ASS,
            KREUZ_2, KREUZ_3, KREUZ_4, KREUZ_5, KREUZ_6, KREUZ_7, KREUZ_8, KREUZ_9, KREUZ_10, KREUZ_JACK, KREUZ_QUEEN, KREUZ_KING, KREUZ_ASS,
            PIK_2, PIK_3, PIK_4, PIK_5, PIK_6, PIK_7, PIK_8, PIK_9, PIK_10, PIK_JACK, PIK_QUEEN, PIK_KING, PIK_ASS]'''
##################### HERZ KARTEN ###########################
    '''def DEFHERZ_2(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (135, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_2 = DEFHERZ_2(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_3(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (190, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_3 = DEFHERZ_3(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_4(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (245, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_4 = DEFHERZ_4(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_5(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (300, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_5 = DEFHERZ_5(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_6(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (355, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_6 = DEFHERZ_6(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
    '''
    def DEFHERZ_7(sheet, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (410, 110, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        #if MOUSE_POS_R11 == True:
            #image = pygame.transform.rotate(image, 90)
        image.set_colorkey(color)
        return image
    HERZ_7 = DEFHERZ_7(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_8(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (465, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_8 = DEFHERZ_8(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_9(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (520, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_9 = DEFHERZ_9(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_10(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (575, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_10 = DEFHERZ_10(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_JACK(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (630, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_JACK = DEFHERZ_JACK(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_QUEEN(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (685, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_QUEEN = DEFHERZ_QUEEN(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_KING(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (740, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_KING = DEFHERZ_KING(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFHERZ_ASS(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (80, 110, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    HERZ_ASS = DEFHERZ_ASS(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
##################### KARO KARTEN ###########################
    '''def DEFKARO_2(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (135, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_2 = DEFKARO_2(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_3(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (190, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_3 = DEFKARO_3(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_4(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (245, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_4 = DEFKARO_4(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_5(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (300, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_5 = DEFKARO_5(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_6(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (355, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_6 = DEFKARO_6(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
    '''
    def DEFKARO_7(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (410, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_7 = DEFKARO_7(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_8(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (465, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_8 = DEFKARO_8(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_9(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (520, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_9 = DEFKARO_9(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_10(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (575, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_10 = DEFKARO_10(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_JACK(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (630, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_JACK = DEFKARO_JACK(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_QUEEN(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (685, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_QUEEN = DEFKARO_QUEEN(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_KING(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (740, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_KING = DEFKARO_KING(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKARO_ASS(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (80, 175, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KARO_ASS = DEFKARO_ASS(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
##################### KREUZ KARTEN ##########################
    '''def DEFKREUZ_2(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (135, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_2 = DEFKREUZ_2(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_3(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (190, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_3 = DEFKREUZ_3(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_4(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (245, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_4 = DEFKREUZ_4(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_5(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (300, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_5 = DEFKREUZ_5(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_6(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (355, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_6 = DEFKREUZ_6(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
    '''
    def DEFKREUZ_7(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (410, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_7 = DEFKREUZ_7(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_8(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (465, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_8 = DEFKREUZ_8(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_9(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (520, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_9 = DEFKREUZ_9(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_10(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (575, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_10 = DEFKREUZ_10(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_JACK(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (630, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_JACK = DEFKREUZ_JACK(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_QUEEN(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (685, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_QUEEN = DEFKREUZ_QUEEN(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_KING(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (740, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_KING = DEFKREUZ_KING(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFKREUZ_ASS(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (80, 240, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    KREUZ_ASS = DEFKREUZ_ASS(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
##################### PIK KARTEN ##########################
    '''def DEFPIK_2(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (135, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_2 = DEFPIK_2(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_3(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (190, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_3 = DEFPIK_3(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_4(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (245, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_4 = DEFPIK_4(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_5(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (300, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_5 = DEFPIK_5(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_6(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (355, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_6 = DEFPIK_6(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
    '''
    def DEFPIK_7(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (410, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_7 = DEFPIK_7(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_8(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (465, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_8 = DEFPIK_8(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_9(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (520, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_9 = DEFPIK_9(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_10(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (575, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_10 = DEFPIK_10(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_JACK(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (630, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_JACK = DEFPIK_JACK(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_QUEEN(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (685, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_QUEEN = DEFPIK_QUEEN(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_KING(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (740, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_KING = DEFPIK_KING(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def DEFPIK_ASS(sheet, width, height, scale, color):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(sheet, (0, 0), (80, 305, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                return image
    PIK_ASS = DEFPIK_ASS(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
##################### RAND KARTEN ###########################
    def get_imageP1(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(color)
            return image
    frame_P1 = get_imageP1(sprite_sheet_image, 42, 60, 3, SPRITE_TP)#126,180,skalierung,transparenz

    def get_imageG1(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 45, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(color)
            return image
    frame_G1 = get_imageG1(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageF1(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 110, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(color)
            return image
    frame_F1 = get_imageF1(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageF2(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 110, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(color)
            return image
    frame_F2 = get_imageF2(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageG2(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 45, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(color)
            return image
    frame_G2 = get_imageG2(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageP2(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(color)
            return image
    frame_P2 = get_imageP2(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
##################### Reihe 1-4 KARTEN ###########################
    def get_imageR11(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R11 = get_imageR11(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR12(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R12 = get_imageR12(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR13(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R13 = get_imageR13(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR21(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R21 = get_imageR21(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR22(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R22 = get_imageR22(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR23(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R23 = get_imageR23(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR31(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R31 = get_imageR31(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR32(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R32 = get_imageR32(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR33(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R33 = get_imageR33(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR41(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R41 = get_imageR41(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR42(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R42 = get_imageR42(sprite_sheet_image, 42, 60, 3, SPRITE_TP)

    def get_imageR43(sheet, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(sheet, (0, 0), (795, 175, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image = pygame.transform.rotate(image, 90)
            image.set_colorkey(color)
            return image
    frame_R43 = get_imageR43(sprite_sheet_image, 42, 60, 3, SPRITE_TP)
    #Liste wird erstellt und gemischt
    CARDS_32 = [HERZ_7, HERZ_8, HERZ_9, HERZ_10, HERZ_JACK, HERZ_QUEEN, HERZ_KING, HERZ_ASS,
            KARO_7, KARO_8, KARO_9, KARO_10, KARO_JACK, KARO_QUEEN, KARO_KING, KARO_ASS,
            KREUZ_7, KREUZ_8, KREUZ_9, KREUZ_10, KREUZ_JACK, KREUZ_QUEEN, KREUZ_KING, KREUZ_ASS,
            PIK_7, PIK_8, PIK_9, PIK_10, PIK_JACK, PIK_QUEEN, PIK_KING, PIK_ASS]
    random.shuffle(CARDS_32)
    CARDS_P1 = CARDS_32 [0:10]
    CARDS_P2 = CARDS_32 [10:20]
    CARDS_TABLE = CARDS_32 [20:]
    
    while True:
        BG_PSC_LOAD()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()#Mausposition wird ermittelt
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        white = (255,255,255)
        if P1 >= 10:
            P1 = 0
        if P2 >= 10:
            P2 = 0
##################### RAND KARTEN ###########################
        #Schaltfläche wird erstellt, die sich farblich ändert, wenn man mit der Maus drüber ist. geht
        if 50 + 130 > PLAY_MOUSE_POS[0] > 50 and 486 + 184 > PLAY_MOUSE_POS[1] > 486:
            pygame.draw.rect(SCREEN, white,(50,486,130,184))
            MOUSE_POS_P1 = True
            if MOUSE_POS_P1 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    P1 += 1
                    print(P1)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(50,486,130,184))
            MOUSE_POS_P1 = False

        if 1100 + 130 > PLAY_MOUSE_POS[0] > 1100 and 486 + 184 > PLAY_MOUSE_POS[1] > 486:
            pygame.draw.rect(SCREEN, white,(1100,486,130,184))
            MOUSE_POS_P2 = True
            if MOUSE_POS_P2 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    P2 += 1
                    print(P2)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(1100,486,130,184))
            MOUSE_POS_P2 = False
        
        if 50 + 130 > PLAY_MOUSE_POS[0] > 50 and 266 + 184 > PLAY_MOUSE_POS[1] > 266:
            pygame.draw.rect(SCREEN, white,(50,266,130,184))
            MOUSE_POS_G1 = True
            if MOUSE_POS_G1 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    G1 += 1
                    print(G1)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(50,266,130,184))
            MOUSE_POS_G1 = False     
       
        if 1100 + 130 > PLAY_MOUSE_POS[0] > 1100 and 266 + 184 > PLAY_MOUSE_POS[1] > 266:
            pygame.draw.rect(SCREEN, white,(1100,266,130,184))
            MOUSE_POS_G2 = True
            if MOUSE_POS_G2 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    G2 += 1
                    print(G2)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(1100,266,130,184))
            MOUSE_POS_G2 = False

        if 50 + 130 > PLAY_MOUSE_POS[0] > 50 and 50 + 184 > PLAY_MOUSE_POS[1] > 50:
            pygame.draw.rect(SCREEN, white,(50,50,130,184))
            MOUSE_POS_F1 = True
            if MOUSE_POS_F1 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    F1 += 1
                    print(F1)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(50,50,130,184))
            MOUSE_POS_F1 = False
        
        if 1100 + 130 > PLAY_MOUSE_POS[0] > 1100 and 50 + 184 > PLAY_MOUSE_POS[1] > 50:
            pygame.draw.rect(SCREEN, white,(1100,50,130,184))
            MOUSE_POS_F2 = True
            if MOUSE_POS_F2 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    F2 += 1
                    print(F2)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(1100,50,130,184))
            MOUSE_POS_F2 = False
##################### Reihe 1-4 KARTEN ###########################
#R1
        if 208 + 184 > PLAY_MOUSE_POS[0] > 208 and 134 + 130 > PLAY_MOUSE_POS[1] > 134:
            pygame.draw.rect(SCREEN, white,(208,134,184,130))
            MOUSE_POS_R11 = True
            if MOUSE_POS_R11 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R11 += 1
                    print(R11)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(208,134,184,130))
            MOUSE_POS_R11 = False

        if 208 + 184 > PLAY_MOUSE_POS[0] > 208 and 294 + 130 > PLAY_MOUSE_POS[1] > 294:
            pygame.draw.rect(SCREEN, white,(208,294,184,130))
            MOUSE_POS_R12 = True
            if MOUSE_POS_R12 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R12 += 1
                    print(R12)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(208,294,184,130))
            MOUSE_POS_R12 = False

        if 208 + 184 > PLAY_MOUSE_POS[0] > 208 and 454 + 130 > PLAY_MOUSE_POS[1] > 454:
            pygame.draw.rect(SCREEN, white,(208,454,184,130))
            MOUSE_POS_R13 = True
            if MOUSE_POS_R13 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R13 += 1
                    print(R13)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(208,454,184,130))
            MOUSE_POS_R13 = False
#R2
        if 431 + 184 > PLAY_MOUSE_POS[0] > 431 and 134 + 130 > PLAY_MOUSE_POS[1] > 134:
            pygame.draw.rect(SCREEN, white,(431,134,184,130))
            MOUSE_POS_R21 = True
            if MOUSE_POS_R21 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R21 += 1
                    print(R21)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(431,134,184,130))
            MOUSE_POS_R21 = False

        if 431 + 184 > PLAY_MOUSE_POS[0] > 431 and 294 + 130 > PLAY_MOUSE_POS[1] > 294:
            pygame.draw.rect(SCREEN, white,(431,294,184,130))
            MOUSE_POS_R22 = True
            if MOUSE_POS_R22 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R22 += 1
                    print(R22)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(431,294,184,130))
            MOUSE_POS_R22 = False

        if 431 + 184 > PLAY_MOUSE_POS[0] > 431 and 454 + 130 > PLAY_MOUSE_POS[1] > 454:
            pygame.draw.rect(SCREEN, white,(431,454,184,130))
            MOUSE_POS_R23 = True
            if MOUSE_POS_R23 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R23 += 1
                    print(R23)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(431,454,184,130))
            MOUSE_POS_R23 = False
#R3
        if 669 + 184 > PLAY_MOUSE_POS[0] > 669 and 134 + 130 > PLAY_MOUSE_POS[1] > 134:
            pygame.draw.rect(SCREEN, white,(669,134,184,130))
            MOUSE_POS_R31 = True
            if MOUSE_POS_R31 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R31 += 1
                    print(R31)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(669,134,184,130))
            MOUSE_POS_R31 = False

        if 669 + 184 > PLAY_MOUSE_POS[0] > 669 and 294 + 130 > PLAY_MOUSE_POS[1] > 294:
            pygame.draw.rect(SCREEN, white,(669,294,184,130))
            MOUSE_POS_R32 = True
            if MOUSE_POS_R32 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R32 += 1
                    print(R32)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(669,294,184,130))
            MOUSE_POS_R32 = False

        if 669 + 184 > PLAY_MOUSE_POS[0] > 669 and 454 + 130 > PLAY_MOUSE_POS[1] > 454:
            pygame.draw.rect(SCREEN, white,(669,454,184,130))
            MOUSE_POS_R33 = True
            if MOUSE_POS_R33 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R33 += 1
                    print(R33)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(669,454,184,130))
            MOUSE_POS_R33 = False
#R4
        if 892 + 184 > PLAY_MOUSE_POS[0] > 892 and 134 + 130 > PLAY_MOUSE_POS[1] > 134:
            pygame.draw.rect(SCREEN, white,(892,134,184,130))
            MOUSE_POS_R41 = True
            if MOUSE_POS_R41 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R41 += 1
                    print(R41)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(892,134,184,130))
            MOUSE_POS_R41 = False
        
        if 892 + 184 > PLAY_MOUSE_POS[0] > 892 and 294 + 130 > PLAY_MOUSE_POS[1] > 294:
            pygame.draw.rect(SCREEN, white,(892,294,184,130))
            MOUSE_POS_R42 = True
            if MOUSE_POS_R42 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R42 += 1
                    print(R42)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(892,294,184,130))
            MOUSE_POS_R42 = False

        if 892 + 184 > PLAY_MOUSE_POS[0] > 892 and 454 + 130 > PLAY_MOUSE_POS[1] > 454:
            pygame.draw.rect(SCREEN, white,(892,454,184,130))
            MOUSE_POS_R43 = True
            if MOUSE_POS_R43 == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Anweisung das sich das Image ändert, wenn man mit der Maus über der Schaltfläche ist und klickt.        
                if CLICK == 0:
                    CLICK = 60
                if CLICK == 60:
                    R43 += 1
                    print(R43)
            if CLICK != 0:
                CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(892,454,184,130))
            MOUSE_POS_R43 = False        
##################### RAND KARTEN ###########################
        if P1 == 0:
            SCREEN.blit(frame_P1, (52, 488))
        elif P1 == 1:
            SCREEN.blit(CARDS_P1[0], (52, 488))
        #elif P1 == 2:
            #SCREEN.blit(CARDS_P1[1], (52, 488))
        if P2 == 0:
            SCREEN.blit(frame_P2, (1102, 488))
        elif P2 == 1:
            SCREEN.blit(CARDS_P2[0], (1102, 488))
        if G1 == 0:
            SCREEN.blit(frame_G1, (52, 268))
        elif G1 == 1:
            SCREEN.blit(CARDS_P1[1], (52, 268))
        if G2 == 0:
            SCREEN.blit(frame_G2, (1102, 268))
        elif G2 == 1:
            SCREEN.blit(CARDS_P2[1], (1102, 268))
        if F1 == 0:
            SCREEN.blit(frame_F1, (52, 52))
        elif F1 == 1:
            SCREEN.blit(CARDS_P1[2], (52, 52))
        if F2 == 0:
            SCREEN.blit(frame_F2, (1102, 52))
        elif F2 == 1:
            SCREEN.blit(CARDS_P2[2], (1102, 52))
##################### Reihe 1-4 KARTEN ###########################
#R1
        if R11 == 0:
            SCREEN.blit(frame_R11, (210, 136))
        elif R11 == 1:
            SCREEN.blit(CARDS_TABLE[0], (210, 136))
        if R12 == 0:
            SCREEN.blit(frame_R12, (210, 296))
        elif R12 == 1:
            SCREEN.blit(CARDS_TABLE[1], (210, 296))
        if R13 == 0:
            SCREEN.blit(frame_R13, (210, 456))
        elif R13 == 1:
            SCREEN.blit(CARDS_TABLE[2], (210, 456))
#R2
        if R21 == 0:
            SCREEN.blit(frame_R21, (433, 136))
        elif R21 == 1:
            SCREEN.blit(CARDS_TABLE[3], (433, 136))
        if R22 == 0:
            SCREEN.blit(frame_R22, (433, 296))
        elif R22 == 1:
            SCREEN.blit(CARDS_TABLE[4], (433, 296))
        if R23 == 0:
            SCREEN.blit(frame_R23, (433, 456))
        elif R23 == 1:
            SCREEN.blit(CARDS_TABLE[5], (433, 456))
#R3
        if R31 == 0:
            SCREEN.blit(frame_R31, (671, 136))
        elif R31 == 1:
            SCREEN.blit(CARDS_TABLE[6], (671, 136))
        if R32 == 0:
            SCREEN.blit(frame_R32, (671, 296))
        elif R32 == 1:
            SCREEN.blit(CARDS_TABLE[7], (671, 296))
        if R33 == 0:
            SCREEN.blit(frame_R33, (671, 456))
        elif R33 == 1:
            SCREEN.blit(CARDS_TABLE[8], (671, 456))
#R4
        if R41 == 0:
            SCREEN.blit(frame_R41, (894, 136))
        elif R41 == 1:
            SCREEN.blit(CARDS_TABLE[9], (894, 136))
        if R42 == 0:
            SCREEN.blit(frame_R42, (894, 296))
        elif R42 == 1:
            SCREEN.blit(CARDS_TABLE[10], (894, 296))
        if R43 == 0:
            SCREEN.blit(frame_R43, (894, 456))
        elif R43 == 1:
            SCREEN.blit(CARDS_TABLE[11], (894, 456))
##################### HERZ KARTEN ###########################
        '''SCREEN.blit(HERZ_2, (50, 490))        
        SCREEN.blit(HERZ_3, (50, 490))
        SCREEN.blit(HERZ_4, (50, 490))
        SCREEN.blit(HERZ_5, (50, 490))
        SCREEN.blit(HERZ_6, (50, 490))
        '''
        '''SCREEN.blit(HERZ_7, (50, 490))
        SCREEN.blit(HERZ_8, (50, 490))
        SCREEN.blit(HERZ_9, (50, 490))
        SCREEN.blit(HERZ_10, (50, 490))
        SCREEN.blit(HERZ_JACK, (50, 490))
        SCREEN.blit(HERZ_QUEEN, (50, 490))
        SCREEN.blit(HERZ_KING, (50, 490))
        SCREEN.blit(HERZ_ASS, (50, 490))'''
##################### KARO KARTEN ###########################
        '''SCREEN.blit(KARO_2, (50, 490))
        SCREEN.blit(KARO_3, (50, 490))
        SCREEN.blit(KARO_4, (50, 490))
        SCREEN.blit(KARO_5, (50, 490))
        SCREEN.blit(KARO_6, (50, 490))
        '''
        '''SCREEN.blit(KARO_7, (50, 490))
        SCREEN.blit(KARO_8, (50, 490))
        SCREEN.blit(KARO_9, (50, 490))
        SCREEN.blit(KARO_10, (50, 490))
        SCREEN.blit(KARO_JACK, (50, 490))
        SCREEN.blit(KARO_QUEEN, (50, 490))
        SCREEN.blit(KARO_KING, (50, 490))
        SCREEN.blit(KARO_ASS, (50, 490))'''
##################### KREUZ KARTEN ##########################
        '''SCREEN.blit(KREUZ_2, (50, 490))
        SCREEN.blit(KREUZ_3, (50, 490))
        SCREEN.blit(KREUZ_4, (50, 490))
        SCREEN.blit(KREUZ_5, (50, 490))
        SCREEN.blit(KREUZ_6, (50, 490))
        '''
        '''SCREEN.blit(KREUZ_7, (50, 490))
        SCREEN.blit(KREUZ_8, (50, 490))
        SCREEN.blit(KREUZ_9, (50, 490))
        SCREEN.blit(KREUZ_10, (50, 490))
        SCREEN.blit(KREUZ_JACK, (50, 490))
        SCREEN.blit(KREUZ_QUEEN, (50, 490))
        SCREEN.blit(KREUZ_KING, (50, 490))
        SCREEN.blit(KREUZ_ASS, (50, 490))'''
##################### PIK KARTEN ############################
        '''SCREEN.blit(PIK_2, (50, 490))
        SCREEN.blit(PIK_3, (50, 490))
        SCREEN.blit(PIK_4, (50, 490))
        SCREEN.blit(PIK_5, (50, 490))
        SCREEN.blit(PIK_6, (50, 490))
        '''
        '''SCREEN.blit(PIK_7, (50, 490))
        SCREEN.blit(PIK_8, (50, 490))
        SCREEN.blit(PIK_9, (50, 490))
        SCREEN.blit(PIK_10, (50, 490))
        SCREEN.blit(PIK_JACK, (50, 490))
        SCREEN.blit(PIK_QUEEN, (50, 490))
        SCREEN.blit(PIK_KING, (50, 490))
        SCREEN.blit(PIK_ASS, (50, 490))'''
        #Erstellung eines Buttens mit Textinputmöglichkeit. Input kommt von button.py
        PLAY_BACK = Button(image=None, pos=(35, 695), 
            text_input="Back", font=get_font(25), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        START_BUTTON = Button(image=None, pos=(1104, 695), 
            text_input="Start", font=get_font(25), base_color="White", hovering_color="Green")
        START_BUTTON.changeColor(PLAY_MOUSE_POS)
        START_BUTTON.update(SCREEN)
        #Ausführung von Anweisungen, durch bestimmte Interaktionen, wie Mausklick auf einer bestimmten Position. Import von button.py und pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Programm beenden, wenn das X vom Fenster gedrückt wird
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):#Ausführen der Anweisung, wenn Maus auf festgelegter position ist und eine Maustaste gedrückt wird
                    click_sound.play()
                    play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    print(1)
            '''if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("links")
                if event.button == 2:
                    print("mitte")
                if event.button == 3:
                    print("rechts")
                if event.button == 4:
                    print("hoch")
                if event.button == 5:
                    print("runter")'''
        clock.tick(60)
        pygame.display.update()#Bildschirm wird aktualisiert
    
def skin_select():
    pygame.display.set_caption("Skin Selection")

    global BG_PSC_SELECT

    while True:
        SKIN_SELECT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#2b2a2a")

        if BG_PSC_SELECT == 0:
            bgtxt = "Soccerfield simple"
        elif BG_PSC_SELECT == 1:
            bgtxt = "Soccerfield fire and water"
        elif BG_PSC_SELECT == 2:
            bgtxt = "Soccerfield fire and ice"
        elif BG_PSC_SELECT == 3:
            bgtxt = "Test Image"
        else:
            bgtxt = "Soccerfield simple"
        
        SKIN_SELECT_BACK = Button(image=None, pos=(640, 560), 
                            text_input="Back", font=get_font(75), base_color="WHITE", hovering_color="Green")

        SKIN_SELECT_BACK.changeColor(SKIN_SELECT_MOUSE_POS)
        SKIN_SELECT_BACK.update(SCREEN)

        SKIN_SELECT_CARDSOCCER_BG = Button(image=None, pos=(640, 460), 
                            text_input=bgtxt, font=get_font(75), base_color="WHITE", hovering_color="Green")

        SKIN_SELECT_CARDSOCCER_BG.changeColor(SKIN_SELECT_MOUSE_POS)
        SKIN_SELECT_CARDSOCCER_BG.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_SELECT_CARDSOCCER_BG.checkForInput(SKIN_SELECT_MOUSE_POS):
                    click_sound.play()
                    if BG_PSC_SELECT == 4:
                        BG_PSC_SELECT = 0
                    else:
                        BG_PSC_SELECT += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_SELECT_BACK.checkForInput(SKIN_SELECT_MOUSE_POS):
                    click_sound.play()
                    options()
        
        pygame.display.update()

def options():

    pygame.display.set_caption("Options")

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

        OPTIONS_BACK = Button(image=None, pos=(640, 560), 
                            text_input="Back", font=get_font(75), base_color="WHITE", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        OPTIONS_SKINS = Button(image=None, pos=(640, 460), 
                            text_input="Skin Menu", font=get_font(75), base_color="WHITE", hovering_color="Green")

        OPTIONS_SKINS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_SKINS.update(SCREEN)

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
                if OPTIONS_SKINS.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    skin_select()
                                    
        pygame.display.update()

def main_menu():

    pygame.display.set_caption("Card Games")

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