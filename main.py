
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
CARD_SELECT = 0
CB_SELECT = 0
BG = pygame.image.load("assets/bg_test1.png")
BG = pygame.transform.scale(BG,( 1920, 980))

def BG_PSC_LOAD():
    # Lädt den Cardsoccer background und je nach einstellung ändert sich dieser
    global BG_PSC_SELECT
    if CB_SELECT == 0:
        if BG_PSC_SELECT == 0:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield.png")
        elif BG_PSC_SELECT == 1:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield fire and water.png")
        elif BG_PSC_SELECT == 2:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield fire and ice.png")
        elif BG_PSC_SELECT == 3:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/high contrast.png")
        elif BG_PSC_SELECT == 4:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/tabletop.png")
        elif BG_PSC_SELECT == 5:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/testbackground.png")
        else:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield.png")
    else:
        if BG_PSC_SELECT == 0:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield.png")
        elif BG_PSC_SELECT == 1:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield fire and water.png")
        elif BG_PSC_SELECT == 2:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield fire and ice.png")
        elif BG_PSC_SELECT == 3:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/high contrast.png")
        elif BG_PSC_SELECT == 4:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/tabletop.png")
        elif BG_PSC_SELECT == 5:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/testbackground.png")
        else:
            BG_PSC = pygame.image.load("assets//cardsoccer backgrounds/soccerfield.png")


    BG_PSC = pygame.transform.scale(BG_PSC,( 1180, 620))
    SCREEN.blit(BG_PSC, (50, 50))

def CARD_LOAD():
    global CARD_SELECT
    global SPRITE_TP
    global sprite_sheet_image
    SPRITE_TP = (0, 0, 0)
    if CB_SELECT == 0:
        if CARD_SELECT == 0:
            sprite_sheet_image = pygame.image.load("assets/cards/testcards5.png").convert_alpha()
        elif CARD_SELECT == 1:
            sprite_sheet_image = pygame.image.load("assets/cards/red prayers.png").convert_alpha()
    else:
        if CARD_SELECT == 0:
            sprite_sheet_image = pygame.image.load("assets/cards/testcards5.png").convert_alpha()
        elif CARD_SELECT == 1:
            sprite_sheet_image = pygame.image.load("assets/cards/red prayers colorblind.png").convert_alpha()

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def play():

    pygame.display.set_caption("Game Selection")
    BG = pygame.image.load("assets/bg_test1.png")
    BG = pygame.transform.scale(BG,( 2620, 1080))
    while True:
        SCREEN.fill("#000000")
        SCREEN.blit(BG, (-1320, -300))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        '''PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)'''

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

    global SPRITE_TP
    global CARD_SELECT
    global BG_PSC_SELECT
    CARD_LOAD()
    SCREEN.fill("#2b2a2a")
    pygame.display.set_caption("Card Soccer")
    #Variablen innerhalb von der Funktion werden festgelegt
    P1 = 0#P=Player
    P2 = 0
    G1 = 0#G=Goal
    G2 = 0
    F1 = 0#F=Fail
    F2 = 0
    R11 = 0#R=Reihe
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
#
    def get_image(sheet, width, height, scale, color, x, y, symbol, value):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return [image, symbol, value]
    def get_image_rotate(sheet, width, height, scale, color, x, y, symbol, value):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image = pygame.transform.rotate(image, 90)
        image.set_colorkey(color)
        return [image, symbol, value]
##################### RAND KARTEN ###########################
    frame_P1 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)#width,height,skalierung,transparenz,x,y
    frame_G1 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 45, "frame", 55)
    frame_F1 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 110, "frame", 55)
    frame_F2 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 110, "frame", 55)
    frame_G2 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 45, "frame", 55)
    frame_P2 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
##################### Reihe 1-4 KARTEN ###########################
    frame_R11 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R12 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R13 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R21 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R22 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R23 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R31 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R32 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R33 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R41 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R42 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
    frame_R43 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 795, 175, "frame", 55)
##################### HERZ KARTEN ###########################
    '''HERZ_2 = DEFHERZ_2(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 135, 110)
    HERZ_3 = DEFHERZ_3(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 190, 110)
    HERZ_4 = DEFHERZ_4(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 245, 110)
    HERZ_5 = DEFHERZ_5(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 300, 110)
    HERZ_6 = DEFHERZ_6(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 355, 110)
    '''
    HERZ_7 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 410, 110, "HERZ", 7)
    
    HERZ_8 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 465, 110, "HERZ", 8)
    
    HERZ_9 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 520, 110, "HERZ", 9)
    
    HERZ_10 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 575, 110, "HERZ", 10)
    
    HERZ_JACK = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 630, 110, "HERZ", 11)
    
    HERZ_QUEEN = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 685, 110, "HERZ", 12)
    
    HERZ_KING = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 740, 110, "HERZ", 13)
    
    HERZ_ASS = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 80, 110, "HERZ", 14)
    
##################### KARO KARTEN ###########################
    '''KARO_2 = DEFKARO_2(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 135, 175)
    KARO_3 = DEFKARO_3(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 190, 175)
    KARO_4 = DEFKARO_4(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 245, 175)
    KARO_5 = DEFKARO_5(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 300, 175)
    KARO_6 = DEFKARO_6(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 355, 175)
    '''
    KARO_7 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 410, 175, "KARO", 7)
    
    KARO_8 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 465, 175, "KARO", 8)
    
    KARO_9 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 520, 175, "KARO", 9)
    
    KARO_10 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 575, 175, "KARO", 10)
    
    KARO_JACK = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 630, 175, "KARO", 11)
    
    KARO_QUEEN = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 685, 175, "KARO", 12)
    
    KARO_KING = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 740, 175, "KARO", 13)
    
    KARO_ASS = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 80, 175, "KARO", 14)
    
##################### KREUZ KARTEN ##########################
    '''KREUZ_2 = DEFKREUZ_2(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 135, 240)
    KREUZ_3 = DEFKREUZ_3(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 190, 240)
    KREUZ_4 = DEFKREUZ_4(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 245, 240)
    KREUZ_5 = DEFKREUZ_5(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 300, 240)
    KREUZ_6 = DEFKREUZ_6(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 355, 240)
    '''
    KREUZ_7 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 410, 240, "KREUZ", 7)
    
    KREUZ_8 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 465, 240, "KREUZ", 8)
    
    KREUZ_9 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 520, 240, "KREUZ", 9)
    
    KREUZ_10 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 575, 240, "KREUZ", 10)
    
    KREUZ_JACK = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 630, 240, "KREUZ", 11)
    
    KREUZ_QUEEN = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 685, 240, "KREUZ", 12)
    
    KREUZ_KING = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 740, 240, "KREUZ", 13)
    
    KREUZ_ASS = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 80, 240, "KREUZ", 14)
    
##################### PIK KARTEN ##########################
    '''PIK_2 = DEFPIK_2(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 135, 305)
    PIK_3 = DEFPIK_3(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 190, 305)
    PIK_4 = DEFPIK_4(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 245, 305)
    PIK_5 = DEFPIK_5(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 300, 305)
    PIK_6 = DEFPIK_6(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 355, 305)
    '''
    PIK_7 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 410, 305, "PIK", 7)
    
    PIK_8 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 465, 305, "PIK", 8)
    
    PIK_9 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 520, 305, "PIK", 9)
    
    PIK_10 = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 575, 305, "PIK", 10)
    
    PIK_JACK = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 630, 305, "PIK", 11)
    
    PIK_QUEEN = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 685, 305, "PIK", 12)
    
    PIK_KING = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 740, 305, "PIK", 13)
    
    PIK_ASS = get_image(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 80, 305, "PIK", 14)
    
    #Liste wird erstellt und gemischt
    CARDS_32 = [HERZ_7, HERZ_8, HERZ_9, HERZ_10, HERZ_JACK, HERZ_QUEEN, HERZ_KING, HERZ_ASS,
            KARO_7, KARO_8, KARO_9, KARO_10, KARO_JACK, KARO_QUEEN, KARO_KING, KARO_ASS,
            KREUZ_7, KREUZ_8, KREUZ_9, KREUZ_10, KREUZ_JACK, KREUZ_QUEEN, KREUZ_KING, KREUZ_ASS,
            PIK_7, PIK_8, PIK_9, PIK_10, PIK_JACK, PIK_QUEEN, PIK_KING, PIK_ASS]
    random.shuffle(CARDS_32)
    CARDS_P1 = CARDS_32 [0:10]
    CARDS_P2 = CARDS_32 [10:20]
    CARDS_TABLE = CARDS_32 [20:]
    CARDS_TABLE2 = []
    CARDS_GOAL = []
    CARDS_FAIL = []

##################### HERZ KARTEN ###########################
    if HERZ_7 in CARDS_TABLE:
        HERZ_7 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 410, 110, "HERZ", 7)
        CARDS_TABLE2.append(HERZ_7)
    if HERZ_8 in CARDS_TABLE:
        HERZ_8 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 465, 110, "HERZ", 8)
        CARDS_TABLE2.append(HERZ_8)
    if HERZ_9 in CARDS_TABLE:
        HERZ_9 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 520, 110, "HERZ", 9)
        CARDS_TABLE2.append(HERZ_9)
    if HERZ_10 in CARDS_TABLE:
        HERZ_10 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 575, 110, "HERZ", 10)
        CARDS_TABLE2.append(HERZ_10)
    if HERZ_JACK in CARDS_TABLE:
        HERZ_JACK = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 630, 110, "HERZ", 11)
        CARDS_TABLE2.append(HERZ_JACK)
    if HERZ_QUEEN in CARDS_TABLE:
        HERZ_QUEEN = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 685, 110, "HERZ", 12)
        CARDS_TABLE2.append(HERZ_QUEEN)
    if HERZ_KING in CARDS_TABLE:
        HERZ_KING = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 740, 110, "HERZ", 13)
        CARDS_TABLE2.append(HERZ_KING)
    if HERZ_ASS in CARDS_TABLE:
        HERZ_ASS = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 80, 110, "HERZ", 14)
        CARDS_TABLE2.append(HERZ_ASS)
##################### KARO KARTEN ###########################
    if KARO_7 in CARDS_TABLE:
        KARO_7 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 410, 175, "KARO", 7)
        CARDS_TABLE2.append(KARO_7)
    if KARO_8 in CARDS_TABLE:
        KARO_8 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 465, 175, "KARO", 8)
        CARDS_TABLE2.append(KARO_8)
    if KARO_9 in CARDS_TABLE:
        KARO_9 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 520, 175, "KARO", 9)
        CARDS_TABLE2.append(KARO_9)
    if KARO_10 in CARDS_TABLE:
        KARO_10 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 575, 175, "KARO", 10)
        CARDS_TABLE2.append(KARO_10)
    if KARO_JACK in CARDS_TABLE:
        KARO_JACK = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 630, 175, "KARO", 11)
        CARDS_TABLE2.append(KARO_JACK)
    if KARO_QUEEN in CARDS_TABLE:
        KARO_QUEEN = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 685, 175, "KARO", 12)
        CARDS_TABLE2.append(KARO_QUEEN)
    if KARO_KING in CARDS_TABLE:
        KARO_KING = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 740, 175, "KARO", 13)
        CARDS_TABLE2.append(KARO_KING)
    if KARO_ASS in CARDS_TABLE:
        KARO_ASS = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 80, 175, "KARO", 14)
        CARDS_TABLE2.append(KARO_ASS)
##################### KREUZ KARTEN ##########################
    if KREUZ_7 in CARDS_TABLE:
        KREUZ_7 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 410, 240, "KREUZ", 7)
        CARDS_TABLE2.append(KREUZ_7)
    if KREUZ_8 in CARDS_TABLE:
        KREUZ_8 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 465, 240, "KREUZ", 8)
        CARDS_TABLE2.append(KREUZ_8)
    if KREUZ_9 in CARDS_TABLE:
        KREUZ_9 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 520, 240, "KREUZ", 9)
        CARDS_TABLE2.append(KREUZ_9)
    if KREUZ_10 in CARDS_TABLE:
        KREUZ_10 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 575, 240, "KREUZ", 10)
        CARDS_TABLE2.append(KREUZ_10)
    if KREUZ_JACK in CARDS_TABLE:
        KREUZ_JACK = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 630, 240, "KREUZ", 11)
        CARDS_TABLE2.append(KREUZ_JACK)
    if KREUZ_QUEEN in CARDS_TABLE:
        KREUZ_QUEEN = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 685, 240, "KREUZ", 12)
        CARDS_TABLE2.append(KREUZ_QUEEN)
    if KREUZ_KING in CARDS_TABLE:
        KREUZ_KING = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 740, 240, "KREUZ", 13)
        CARDS_TABLE2.append(KREUZ_KING)
    if KREUZ_ASS in CARDS_TABLE:
        KREUZ_ASS = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 80, 240, "KREUZ", 14)
        CARDS_TABLE2.append(KREUZ_ASS)
##################### PIK KARTEN ##########################
    if PIK_7 in CARDS_TABLE:
        PIK_7 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 410, 305, "PIK", 7)
        CARDS_TABLE2.append(PIK_7)
    if PIK_8 in CARDS_TABLE:
        PIK_8 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 465, 305, "PIK", 8)
        CARDS_TABLE2.append(PIK_8)
    if PIK_9 in CARDS_TABLE:
        PIK_9 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 520, 305, "PIK", 9)
        CARDS_TABLE2.append(PIK_9)
    if PIK_10 in CARDS_TABLE:
        PIK_10 = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 575, 305, "PIK", 10)
        CARDS_TABLE2.append(PIK_10)
    if PIK_JACK in CARDS_TABLE:
        PIK_JACK = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 630, 305, "PIK", 11)
        CARDS_TABLE2.append(PIK_JACK)
    if PIK_QUEEN in CARDS_TABLE:
        PIK_QUEEN = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 685, 305, "PIK", 12)
        CARDS_TABLE2.append(PIK_QUEEN)
    if PIK_KING in CARDS_TABLE:
        PIK_KING = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 740, 305, "PIK", 13)
        CARDS_TABLE2.append(PIK_KING)
    if PIK_ASS in CARDS_TABLE:
        PIK_ASS = get_image_rotate(sprite_sheet_image, 42, 60, 3, SPRITE_TP, 80, 305, "PIK", 14)
        CARDS_TABLE2.append(PIK_ASS)

####################### P1 K1 R1
    CHECKP1_K1_R11 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[0][1] or CARDS_P1[0][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K1_R11 = 1
    CHECKP1_K1_R12 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[1][1] or CARDS_P1[0][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K1_R12 = 1
    CHECKP1_K1_R13 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[2][1] or CARDS_P1[0][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K1_R13 = 1
####################### P1 K1 R2
    CHECKP1_K1_R21 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[3][1] or CARDS_P1[0][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K1_R21 = 1
    CHECKP1_K1_R22 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[4][1] or CARDS_P1[0][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K1_R22 = 1
    CHECKP1_K1_R23 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[5][1] or CARDS_P1[0][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K1_R23 = 1
####################### P1 K1 R3
    CHECKP1_K1_R31 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[6][1] or CARDS_P1[0][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K1_R31 = 1
    CHECKP1_K1_R32 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[7][1] or CARDS_P1[0][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K1_R32 = 1
    CHECKP1_K1_R33 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[8][1] or CARDS_P1[0][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K1_R33 = 1
####################### P1 K1 R4
    CHECKP1_K1_R41 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[9][1] or CARDS_P1[0][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K1_R41 = 1
    CHECKP1_K1_R42 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[10][1] or CARDS_P1[0][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K1_R42 = 1
    CHECKP1_K1_R43 = 0
    if CARDS_P1[0][1] == CARDS_TABLE2[11][1] or CARDS_P1[0][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K1_R43 = 1
####################### P1 K2 R1
    CHECKP1_K2_R11 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[0][1] or CARDS_P1[1][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K2_R11 = 1
    CHECKP1_K2_R12 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[1][1] or CARDS_P1[1][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K2_R12 = 1
    CHECKP1_K2_R13 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[2][1] or CARDS_P1[1][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K2_R13 = 1
####################### P1 K2 R2
    CHECKP1_K2_R21 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[3][1] or CARDS_P1[1][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K2_R21 = 1
    CHECKP1_K2_R22 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[4][1] or CARDS_P1[1][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K2_R22 = 1
    CHECKP1_K2_R23 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[5][1] or CARDS_P1[1][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K2_R23 = 1
####################### P1 K2 R3
    CHECKP1_K2_R31 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[6][1] or CARDS_P1[1][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K2_R31 = 1
    CHECKP1_K2_R32 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[7][1] or CARDS_P1[1][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K2_R32 = 1
    CHECKP1_K2_R33 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[8][1] or CARDS_P1[1][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K2_R33 = 1
####################### P1 K2 R4
    CHECKP1_K2_R41 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[9][1] or CARDS_P1[1][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K2_R41 = 1
    CHECKP1_K2_R42 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[10][1] or CARDS_P1[1][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K2_R42 = 1
    CHECKP1_K2_R43 = 0
    if CARDS_P1[1][1] == CARDS_TABLE2[11][1] or CARDS_P1[1][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K2_R43 = 1
####################### P1 K3 R1
    CHECKP1_K3_R11 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[0][1] or CARDS_P1[2][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K3_R11 = 1
    CHECKP1_K3_R12 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[1][1] or CARDS_P1[2][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K3_R12 = 1
    CHECKP1_K3_R13 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[2][1] or CARDS_P1[2][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K3_R13 = 1
####################### P1 K3 R2
    CHECKP1_K3_R21 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[3][1] or CARDS_P1[2][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K3_R21 = 1
    CHECKP1_K3_R22 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[4][1] or CARDS_P1[2][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K3_R22 = 1
    CHECKP1_K3_R23 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[5][1] or CARDS_P1[2][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K3_R23 = 1
####################### P1 K3 R3
    CHECKP1_K3_R31 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[6][1] or CARDS_P1[2][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K3_R31 = 1
    CHECKP1_K3_R32 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[7][1] or CARDS_P1[2][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K3_R32 = 1
    CHECKP1_K3_R33 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[2][1] or CARDS_P1[2][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K3_R33 = 1
####################### P1 K3 R4
    CHECKP1_K3_R41 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[9][1] or CARDS_P1[2][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K3_R41 = 1
    CHECKP1_K3_R42 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[10][1] or CARDS_P1[2][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K3_R42 = 1
    CHECKP1_K3_R43 = 0
    if CARDS_P1[2][1] == CARDS_TABLE2[11][1] or CARDS_P1[2][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K3_R43 = 1
####################### P1 K4 R1
    CHECKP1_K4_R11 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[0][1] or CARDS_P1[3][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K4_R11 = 1
    CHECKP1_K4_R12 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[1][1] or CARDS_P1[3][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K4_R12 = 1
    CHECKP1_K4_R13 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[2][1] or CARDS_P1[3][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K4_R13 = 1
####################### P1 K4 R2
    CHECKP1_K4_R21 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[3][1] or CARDS_P1[3][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K4_R21 = 1
    CHECKP1_K4_R22 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[4][1] or CARDS_P1[3][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K4_R22 = 1
    CHECKP1_K4_R23 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[5][1] or CARDS_P1[3][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K4_R23 = 1
####################### P1 K4 R3
    CHECKP1_K4_R31 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[6][1] or CARDS_P1[3][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K4_R31 = 1
    CHECKP1_K4_R32 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[7][1] or CARDS_P1[3][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K4_R32 = 1
    CHECKP1_K4_R33 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[8][1] or CARDS_P1[3][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K4_R33 = 1
####################### P1 K4 R4
    CHECKP1_K4_R41 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[9][1] or CARDS_P1[3][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K4_R41 = 1
    CHECKP1_K4_R42 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[10][1] or CARDS_P1[3][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K4_R42 = 1
    CHECKP1_K4_R43 = 0
    if CARDS_P1[3][1] == CARDS_TABLE2[11][1] or CARDS_P1[3][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K4_R43 = 1
####################### P1 K5 R1
    CHECKP1_K5_R11 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[0][1] or CARDS_P1[4][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K5_R11 = 1
    CHECKP1_K5_R12 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[1][1] or CARDS_P1[4][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K5_R12 = 1
    CHECKP1_K5_R13 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[2][1] or CARDS_P1[4][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K5_R13 = 1
####################### P1 K5 R2
    CHECKP1_K5_R21 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[3][1] or CARDS_P1[4][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K5_R21 = 1
    CHECKP1_K5_R22 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[4][1] or CARDS_P1[4][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K5_R22 = 1
    CHECKP1_K5_R23 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[5][1] or CARDS_P1[4][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K5_R23 = 1
####################### P1 K5 R3
    CHECKP1_K5_R31 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[6][1] or CARDS_P1[4][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K5_R31 = 1
    CHECKP1_K5_R32 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[7][1] or CARDS_P1[4][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K5_R32 = 1
    CHECKP1_K5_R33 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[8][1] or CARDS_P1[4][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K5_R33 = 1
####################### P1 K5 R4
    CHECKP1_K5_R41 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[9][1] or CARDS_P1[4][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K5_R41 = 1
    CHECKP1_K5_R42 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[10][1] or CARDS_P1[4][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K5_R42 = 1
    CHECKP1_K5_R43 = 0
    if CARDS_P1[4][1] == CARDS_TABLE2[11][1] or CARDS_P1[4][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K5_R43 = 1
####################### P1 K6 R1
    CHECKP1_K6_R11 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[0][1] or CARDS_P1[5][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K6_R11 = 1
    CHECKP1_K6_R12 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[1][1] or CARDS_P1[5][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K6_R12 = 1
    CHECKP1_K6_R13 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[2][1] or CARDS_P1[5][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K6_R13 = 1
####################### P1 K6 R2
    CHECKP1_K6_R21 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[3][1] or CARDS_P1[5][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K6_R21 = 1
    CHECKP1_K6_R22 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[4][1] or CARDS_P1[5][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K6_R22 = 1
    CHECKP1_K6_R23 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[5][1] or CARDS_P1[5][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K6_R23 = 1
####################### P1 K6 R3
    CHECKP1_K6_R31 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[6][1] or CARDS_P1[5][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K6_R31 = 1
    CHECKP1_K6_R32 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[7][1] or CARDS_P1[5][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K6_R32 = 1
    CHECKP1_K6_R33 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[8][1] or CARDS_P1[5][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K6_R33 = 1
####################### P1 K6 R4
    CHECKP1_K6_R41 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[9][1] or CARDS_P1[5][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K6_R41 = 1
    CHECKP1_K6_R42 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[10][1] or CARDS_P1[5][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K6_R42 = 1
    CHECKP1_K6_R43 = 0
    if CARDS_P1[5][1] == CARDS_TABLE2[11][1] or CARDS_P1[5][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K6_R43 = 1
####################### P1 K7 R1
    CHECKP1_K7_R11 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[0][1] or CARDS_P1[6][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K7_R11 = 1
    CHECKP1_K7_R12 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[1][1] or CARDS_P1[6][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K7_R12 = 1
    CHECKP1_K7_R13 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[2][1] or CARDS_P1[6][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K7_R13 = 1
####################### P1 K7 R2
    CHECKP1_K7_R21 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[3][1] or CARDS_P1[6][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K7_R21 = 1
    CHECKP1_K7_R22 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[4][1] or CARDS_P1[6][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K7_R22 = 1
    CHECKP1_K7_R23 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[5][1] or CARDS_P1[6][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K7_R23 = 1
####################### P1 K7 R3
    CHECKP1_K7_R31 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[6][1] or CARDS_P1[6][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K7_R31 = 1
    CHECKP1_K7_R32 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[7][1] or CARDS_P1[6][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K7_R32 = 1
    CHECKP1_K7_R33 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[8][1] or CARDS_P1[6][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K7_R33 = 1
####################### P1 K7 R4
    CHECKP1_K7_R41 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[9][1] or CARDS_P1[6][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K7_R41 = 1
    CHECKP1_K7_R42 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[10][1] or CARDS_P1[6][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K7_R42 = 1
    CHECKP1_K7_R43 = 0
    if CARDS_P1[6][1] == CARDS_TABLE2[11][1] or CARDS_P1[6][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K7_R43 = 1
####################### P1 K8 R1
    CHECKP1_K8_R11 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[0][1] or CARDS_P1[7][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K8_R11 = 1
    CHECKP1_K8_R12 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[1][1] or CARDS_P1[7][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K8_R12 = 1
    CHECKP1_K8_R13 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[2][1] or CARDS_P1[7][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K8_R13 = 1
####################### P1 K8 R2
    CHECKP1_K8_R21 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[3][1] or CARDS_P1[7][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K8_R21 = 1
    CHECKP1_K8_R22 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[4][1] or CARDS_P1[7][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K8_R22 = 1
    CHECKP1_K8_R23 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[5][1] or CARDS_P1[7][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K8_R23 = 1
####################### P1 K8 R3
    CHECKP1_K8_R31 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[6][1] or CARDS_P1[7][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K8_R31 = 1
    CHECKP1_K8_R32 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[7][1] or CARDS_P1[7][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K8_R32 = 1
    CHECKP1_K8_R33 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[8][1] or CARDS_P1[7][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K8_R33 = 1
####################### P1 K8 R4
    CHECKP1_K8_R41 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[9][1] or CARDS_P1[7][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K8_R41 = 1
    CHECKP1_K8_R42 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[10][1] or CARDS_P1[7][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K8_R42 = 1
    CHECKP1_K8_R43 = 0
    if CARDS_P1[7][1] == CARDS_TABLE2[11][1] or CARDS_P1[7][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K8_R43 = 1
####################### P1 K9 R1
    CHECKP1_K9_R11 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[0][1] or CARDS_P1[8][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K9_R11 = 1
    CHECKP1_K9_R12 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[1][1] or CARDS_P1[8][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K9_R12 = 1
    CHECKP1_K9_R13 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[2][1] or CARDS_P1[8][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K9_R13 = 1
####################### P1 K9 R2
    CHECKP1_K9_R21 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[3][1] or CARDS_P1[8][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K9_R21 = 1
    CHECKP1_K9_R22 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[4][1] or CARDS_P1[8][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K9_R22 = 1
    CHECKP1_K9_R23 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[5][1] or CARDS_P1[8][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K9_R23 = 1
####################### P1 K9 R3
    CHECKP1_K9_R31 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[6][1] or CARDS_P1[8][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K9_R31 = 1
    CHECKP1_K9_R32 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[7][1] or CARDS_P1[8][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K9_R32 = 1
    CHECKP1_K9_R33 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[8][1] or CARDS_P1[8][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K9_R33 = 1
####################### P1 K9 R4
    CHECKP1_K9_R41 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[9][1] or CARDS_P1[8][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K9_R41 = 1
    CHECKP1_K9_R42 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[10][1] or CARDS_P1[8][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K9_R42 = 1
    CHECKP1_K9_R43 = 0
    if CARDS_P1[8][1] == CARDS_TABLE2[11][1] or CARDS_P1[8][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K9_R43 = 1
####################### P1 K10 R1
    CHECKP1_K10_R11 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[0][1] or CARDS_P1[9][2] == CARDS_TABLE2[0][2]:
        CHECKP1_K10_R11 = 1
    CHECKP1_K10_R12 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[1][1] or CARDS_P1[9][2] == CARDS_TABLE2[1][2]:
        CHECKP1_K10_R12 = 1
    CHECKP1_K10_R13 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[2][1] or CARDS_P1[9][2] == CARDS_TABLE2[2][2]:
        CHECKP1_K10_R13 = 1
####################### P1 K10 R2
    CHECKP1_K10_R21 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[3][1] or CARDS_P1[9][2] == CARDS_TABLE2[3][2]:
        CHECKP1_K10_R21 = 1
    CHECKP1_K10_R22 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[4][1] or CARDS_P1[9][2] == CARDS_TABLE2[4][2]:
        CHECKP1_K10_R22 = 1
    CHECKP1_K10_R23 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[5][1] or CARDS_P1[9][2] == CARDS_TABLE2[5][2]:
        CHECKP1_K10_R23 = 1
####################### P1 K10 R3
    CHECKP1_K10_R31 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[6][1] or CARDS_P1[9][2] == CARDS_TABLE2[6][2]:
        CHECKP1_K10_R31 = 1
    CHECKP1_K10_R32 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[7][1] or CARDS_P1[9][2] == CARDS_TABLE2[7][2]:
        CHECKP1_K10_R32 = 1
    CHECKP1_K10_R33 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[8][1] or CARDS_P1[9][2] == CARDS_TABLE2[8][2]:
        CHECKP1_K10_R33 = 1
####################### P1 K10 R4
    CHECKP1_K10_R41 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[9][1] or CARDS_P1[9][2] == CARDS_TABLE2[9][2]:
        CHECKP1_K10_R41 = 1
    CHECKP1_K10_R42 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[10][1] or CARDS_P1[9][2] == CARDS_TABLE2[10][2]:
        CHECKP1_K10_R42 = 1
    CHECKP1_K10_R43 = 0
    if CARDS_P1[9][1] == CARDS_TABLE2[11][1] or CARDS_P1[9][2] == CARDS_TABLE2[11][2]:
        CHECKP1_K10_R43 = 1
####################### P2 K1 R1
    CHECKP2_K1_R11 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[0][1] or CARDS_P2[0][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K1_R11 = 1
    CHECKP2_K1_R12 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[1][1] or CARDS_P2[0][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K1_R12 = 1
    CHECKP2_K1_R13 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[2][1] or CARDS_P2[0][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K1_R13 = 1
####################### P2 K1 R2
    CHECKP2_K1_R21 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[3][1] or CARDS_P2[0][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K1_R21 = 1
    CHECKP2_K1_R22 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[4][1] or CARDS_P2[0][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K1_R22 = 1
    CHECKP2_K1_R23 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[5][1] or CARDS_P2[0][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K1_R23 = 1
####################### P2 K1 R3
    CHECKP2_K1_R31 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[6][1] or CARDS_P2[0][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K1_R31 = 1
    CHECKP2_K1_R32 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[7][1] or CARDS_P2[0][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K1_R32 = 1
    CHECKP2_K1_R33 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[8][1] or CARDS_P2[0][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K1_R33 = 1
####################### P2 K1 R4
    CHECKP2_K1_R41 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[9][1] or CARDS_P2[0][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K1_R41 = 1
    CHECKP2_K1_R42 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[10][1] or CARDS_P2[0][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K1_R42 = 1
    CHECKP2_K1_R43 = 0
    if CARDS_P2[0][1] == CARDS_TABLE2[11][1] or CARDS_P2[0][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K1_R43 = 1
####################### P2 K2 R1
    CHECKP2_K2_R11 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[0][1] or CARDS_P2[1][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K2_R11 = 1
    CHECKP2_K2_R12 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[1][1] or CARDS_P2[1][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K2_R12 = 1
    CHECKP2_K2_R13 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[2][1] or CARDS_P2[1][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K2_R13 = 1
####################### P2 K2 R2
    CHECKP2_K2_R21 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[3][1] or CARDS_P2[1][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K2_R21 = 1
    CHECKP2_K2_R22 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[4][1] or CARDS_P2[1][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K2_R22 = 1
    CHECKP2_K2_R23 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[5][1] or CARDS_P2[1][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K2_R23 = 1
####################### P2 K2 R3
    CHECKP2_K2_R31 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[6][1] or CARDS_P1[1][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K2_R31 = 1
    CHECKP2_K2_R32 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[7][1] or CARDS_P1[1][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K2_R32 = 1
    CHECKP2_K2_R33 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[8][1] or CARDS_P1[1][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K2_R33 = 1
####################### P1 K2 R4
    CHECKP2_K2_R41 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[9][1] or CARDS_P2[1][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K2_R41 = 1
    CHECKP2_K2_R42 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[10][1] or CARDS_P2[1][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K2_R42 = 1
    CHECKP2_K2_R43 = 0
    if CARDS_P2[1][1] == CARDS_TABLE2[11][1] or CARDS_P2[1][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K2_R43 = 1
####################### P2 K3 R1
    CHECKP2_K3_R11 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[0][1] or CARDS_P2[2][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K3_R11 = 1
    CHECKP2_K3_R12 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[1][1] or CARDS_P2[2][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K3_R12 = 1
    CHECKP2_K3_R13 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[2][1] or CARDS_P2[2][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K3_R13 = 1
####################### P2 K3 R2
    CHECKP2_K3_R21 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[3][1] or CARDS_P2[2][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K3_R21 = 1
    CHECKP2_K3_R22 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[4][1] or CARDS_P2[2][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K3_R22 = 1
    CHECKP2_K3_R23 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[5][1] or CARDS_P2[2][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K3_R23 = 1
####################### P2 K3 R3
    CHECKP2_K3_R31 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[6][1] or CARDS_P2[2][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K3_R31 = 1
    CHECKP2_K3_R32 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[7][1] or CARDS_P2[2][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K3_R32 = 1
    CHECKP2_K3_R33 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[2][1] or CARDS_P2[2][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K3_R33 = 1
####################### P2 K3 R4
    CHECKP2_K3_R41 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[9][1] or CARDS_P2[2][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K3_R41 = 1
    CHECKP2_K3_R42 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[10][1] or CARDS_P2[2][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K3_R42 = 1
    CHECKP2_K3_R43 = 0
    if CARDS_P2[2][1] == CARDS_TABLE2[11][1] or CARDS_P2[2][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K3_R43 = 1
####################### P2 K4 R1
    CHECKP2_K4_R11 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[0][1] or CARDS_P2[3][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K4_R11 = 1
    CHECKP2_K4_R12 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[1][1] or CARDS_P2[3][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K4_R12 = 1
    CHECKP2_K4_R13 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[2][1] or CARDS_P2[3][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K4_R13 = 1
####################### P2 K4 R2
    CHECKP2_K4_R21 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[3][1] or CARDS_P2[3][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K4_R21 = 1
    CHECKP2_K4_R22 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[4][1] or CARDS_P2[3][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K4_R22 = 1
    CHECKP2_K4_R23 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[5][1] or CARDS_P2[3][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K4_R23 = 1
####################### P2 K4 R3
    CHECKP2_K4_R31 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[6][1] or CARDS_P2[3][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K4_R31 = 1
    CHECKP2_K4_R32 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[7][1] or CARDS_P2[3][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K4_R32 = 1
    CHECKP2_K4_R33 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[8][1] or CARDS_P2[3][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K4_R33 = 1
####################### P2 K4 R4
    CHECKP2_K4_R41 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[9][1] or CARDS_P2[3][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K4_R41 = 1
    CHECKP2_K4_R42 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[10][1] or CARDS_P2[3][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K4_R42 = 1
    CHECKP2_K4_R43 = 0
    if CARDS_P2[3][1] == CARDS_TABLE2[11][1] or CARDS_P2[3][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K4_R43 = 1
####################### P2 K5 R1
    CHECKP2_K5_R11 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[0][1] or CARDS_P2[4][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K5_R11 = 1
    CHECKP2_K5_R12 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[1][1] or CARDS_P2[4][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K5_R12 = 1
    CHECKP2_K5_R13 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[2][1] or CARDS_P2[4][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K5_R13 = 1
####################### P2 K5 R2
    CHECKP2_K5_R21 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[3][1] or CARDS_P2[4][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K5_R21 = 1
    CHECKP2_K5_R22 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[4][1] or CARDS_P2[4][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K5_R22 = 1
    CHECKP2_K5_R23 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[5][1] or CARDS_P2[4][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K5_R23 = 1
####################### P2 K5 R3
    CHECKP2_K5_R31 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[6][1] or CARDS_P2[4][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K5_R31 = 1
    CHECKP2_K5_R32 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[7][1] or CARDS_P2[4][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K5_R32 = 1
    CHECKP2_K5_R33 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[8][1] or CARDS_P2[4][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K5_R33 = 1
####################### P2 K5 R4
    CHECKP2_K5_R41 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[9][1] or CARDS_P2[4][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K5_R41 = 1
    CHECKP2_K5_R42 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[10][1] or CARDS_P2[4][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K5_R42 = 1
    CHECKP2_K5_R43 = 0
    if CARDS_P2[4][1] == CARDS_TABLE2[11][1] or CARDS_P2[4][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K5_R43 = 1
####################### P2 K6 R1
    CHECKP2_K6_R11 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[0][1] or CARDS_P2[5][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K6_R11 = 1
    CHECKP2_K6_R12 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[1][1] or CARDS_P2[5][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K6_R12 = 1
    CHECKP2_K6_R13 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[2][1] or CARDS_P2[5][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K6_R13 = 1
####################### P2 K6 R2
    CHECKP2_K6_R21 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[3][1] or CARDS_P2[5][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K6_R21 = 1
    CHECKP2_K6_R22 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[4][1] or CARDS_P2[5][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K6_R22 = 1
    CHECKP2_K6_R23 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[5][1] or CARDS_P2[5][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K6_R23 = 1
####################### P2 K6 R3
    CHECKP2_K6_R31 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[6][1] or CARDS_P2[5][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K6_R31 = 1
    CHECKP2_K6_R32 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[7][1] or CARDS_P2[5][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K6_R32 = 1
    CHECKP2_K6_R33 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[8][1] or CARDS_P2[5][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K6_R33 = 1
####################### P2 K6 R4
    CHECKP2_K6_R41 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[9][1] or CARDS_P2[5][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K6_R41 = 1
    CHECKP2_K6_R42 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[10][1] or CARDS_P2[5][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K6_R42 = 1
    CHECKP2_K6_R43 = 0
    if CARDS_P2[5][1] == CARDS_TABLE2[11][1] or CARDS_P2[5][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K6_R43 = 1
####################### P2 K7 R1
    CHECKP2_K7_R11 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[0][1] or CARDS_P2[6][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K7_R11 = 1
    CHECKP2_K7_R12 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[1][1] or CARDS_P2[6][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K7_R12 = 1
    CHECKP2_K7_R13 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[2][1] or CARDS_P2[6][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K7_R13 = 1
####################### P2 K7 R2
    CHECKP2_K7_R21 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[3][1] or CARDS_P2[6][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K7_R21 = 1
    CHECKP2_K7_R22 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[4][1] or CARDS_P2[6][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K7_R22 = 1
    CHECKP2_K7_R23 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[5][1] or CARDS_P2[6][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K7_R23 = 1
####################### P2 K7 R3
    CHECKP2_K7_R31 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[6][1] or CARDS_P2[6][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K7_R31 = 1
    CHECKP2_K7_R32 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[7][1] or CARDS_P2[6][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K7_R32 = 1
    CHECKP2_K7_R33 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[8][1] or CARDS_P2[6][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K7_R33 = 1
####################### P2 K7 R4
    CHECKP2_K7_R41 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[9][1] or CARDS_P2[6][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K7_R41 = 1
    CHECKP2_K7_R42 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[10][1] or CARDS_P2[6][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K7_R42 = 1
    CHECKP2_K7_R43 = 0
    if CARDS_P2[6][1] == CARDS_TABLE2[11][1] or CARDS_P2[6][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K7_R43 = 1
####################### P2 K8 R1
    CHECKP2_K8_R11 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[0][1] or CARDS_P2[7][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K8_R11 = 1
    CHECKP2_K8_R12 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[1][1] or CARDS_P2[7][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K8_R12 = 1
    CHECKP2_K8_R13 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[2][1] or CARDS_P2[7][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K8_R13 = 1
####################### P2 K8 R2
    CHECKP2_K8_R21 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[3][1] or CARDS_P2[7][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K8_R21 = 1
    CHECKP2_K8_R22 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[4][1] or CARDS_P2[7][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K8_R22 = 1
    CHECKP2_K8_R23 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[5][1] or CARDS_P2[7][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K8_R23 = 1
####################### P2 K8 R3
    CHECKP2_K8_R31 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[6][1] or CARDS_P2[7][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K8_R31 = 1
    CHECKP2_K8_R32 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[7][1] or CARDS_P2[7][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K8_R32 = 1
    CHECKP2_K8_R33 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[8][1] or CARDS_P2[7][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K8_R33 = 1
####################### P2 K8 R4
    CHECKP2_K8_R41 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[9][1] or CARDS_P2[7][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K8_R41 = 1
    CHECKP2_K8_R42 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[10][1] or CARDS_P2[7][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K8_R42 = 1
    CHECKP2_K8_R43 = 0
    if CARDS_P2[7][1] == CARDS_TABLE2[11][1] or CARDS_P2[7][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K8_R43 = 1
####################### P2 K9 R1
    CHECKP2_K9_R11 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[0][1] or CARDS_P2[8][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K9_R11 = 1
    CHECKP2_K9_R12 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[1][1] or CARDS_P2[8][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K9_R12 = 1
    CHECKP2_K9_R13 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[2][1] or CARDS_P2[8][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K9_R13 = 1
####################### P2 K9 R2
    CHECKP2_K9_R21 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[3][1] or CARDS_P2[8][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K9_R21 = 1
    CHECKP2_K9_R22 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[4][1] or CARDS_P2[8][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K9_R22 = 1
    CHECKP2_K9_R23 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[5][1] or CARDS_P2[8][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K9_R23 = 1
####################### P2 K9 R3
    CHECKP2_K9_R31 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[6][1] or CARDS_P2[8][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K9_R31 = 1
    CHECKP2_K9_R32 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[7][1] or CARDS_P2[8][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K9_R32 = 1
    CHECKP2_K9_R33 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[8][1] or CARDS_P2[8][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K9_R33 = 1
####################### P2 K9 R4
    CHECKP2_K9_R41 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[9][1] or CARDS_P2[8][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K9_R41 = 1
    CHECKP2_K9_R42 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[10][1] or CARDS_P2[8][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K9_R42 = 1
    CHECKP2_K9_R43 = 0
    if CARDS_P2[8][1] == CARDS_TABLE2[11][1] or CARDS_P2[8][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K9_R43 = 1
####################### P2 K10 R1
    CHECKP2_K10_R11 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[0][1] or CARDS_P2[9][2] == CARDS_TABLE2[0][2]:
        CHECKP2_K10_R11 = 1
    CHECKP2_K10_R12 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[1][1] or CARDS_P2[9][2] == CARDS_TABLE2[1][2]:
        CHECKP2_K10_R12 = 1
    CHECKP2_K10_R13 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[2][1] or CARDS_P2[9][2] == CARDS_TABLE2[2][2]:
        CHECKP2_K10_R13 = 1
####################### P2 K10 R2
    CHECKP2_K10_R21 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[3][1] or CARDS_P2[9][2] == CARDS_TABLE2[3][2]:
        CHECKP2_K10_R21 = 1
    CHECKP2_K10_R22 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[4][1] or CARDS_P2[9][2] == CARDS_TABLE2[4][2]:
        CHECKP2_K10_R22 = 1
    CHECKP2_K10_R23 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[5][1] or CARDS_P2[9][2] == CARDS_TABLE2[5][2]:
        CHECKP2_K10_R23 = 1
####################### P2 K10 R3
    CHECKP2_K10_R31 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[6][1] or CARDS_P2[9][2] == CARDS_TABLE2[6][2]:
        CHECKP2_K10_R31 = 1
    CHECKP2_K10_R32 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[7][1] or CARDS_P2[9][2] == CARDS_TABLE2[7][2]:
        CHECKP2_K10_R32 = 1
    CHECKP2_K10_R33 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[8][1] or CARDS_P2[9][2] == CARDS_TABLE2[8][2]:
        CHECKP2_K10_R33 = 1
####################### P2 K10 R4
    CHECKP2_K10_R41 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[9][1] or CARDS_P2[9][2] == CARDS_TABLE2[9][2]:
        CHECKP2_K10_R41 = 1
    CHECKP2_K10_R42 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[10][1] or CARDS_P2[9][2] == CARDS_TABLE2[10][2]:
        CHECKP2_K10_R42 = 1
    CHECKP2_K10_R43 = 0
    if CARDS_P2[9][1] == CARDS_TABLE2[11][1] or CARDS_P2[9][2] == CARDS_TABLE2[11][2]:
        CHECKP2_K10_R43 = 1

    while True:
        BG_PSC_LOAD()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()#Mausposition wird ermittelt
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        white = (255,255,255)
        S1_R1 = 0
        S1_R2 = 0
        S1_R3 = 0
        S1_R4 = 0
        STEP_5 = False
        STEP_6 = False
        STEP_7 = False
        STEP_8 = False
        STEP_9 = False
        STEP_10 = False
        if P1 >= 10:
            P1 = 0
        if P2 >= 10:
            P2 = 0
##################### RAND KARTEN ###########################
        #Schaltfläche wird erstellt, die sich farblich ändert, wenn man mit der Maus darüber ist. geht
        if 50 + 130 > PLAY_MOUSE_POS[0] > 50 and 486 + 184 > PLAY_MOUSE_POS[1] > 486:
            pygame.draw.rect(SCREEN, white,(50,486,130,184))
            MOUSE_POS_P1 = True
            if MOUSE_POS_P1 == True:#Image ändert sich, wenn mit Maus über Schaltfläche + klickt.
                if CLICK == 5:
                    P1 = 1
                    #print(P1)#gibt für kontrollzwecke P1 aus    
                if CLICK != 0:
                    CLICK -= 1
        elif P1 == 0:
            pygame.draw.rect(SCREEN, green,(50,486,130,184))
        else:
            pygame.draw.rect(SCREEN, blue,(50,486,130,184))
            MOUSE_POS_P1 = False
        
        if 1100 + 130 > PLAY_MOUSE_POS[0] > 1100 and 486 + 184 > PLAY_MOUSE_POS[1] > 486:
            pygame.draw.rect(SCREEN, white,(1100,486,130,184))
            MOUSE_POS_P2 = True
            if MOUSE_POS_P2 == True:       
                if CLICK == 5 and P1 == 1 and R11 == 1 or CLICK == 5 and P1 == 1 and R12 == 1 or CLICK == 5 and P1 == 1 and R13 == 1:
                    P2 = 1
                    #print(P2)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(1100,486,130,184))
            MOUSE_POS_P2 = False
        
        if 50 + 130 > PLAY_MOUSE_POS[0] > 50 and 266 + 184 > PLAY_MOUSE_POS[1] > 266:
            pygame.draw.rect(SCREEN, white,(50,266,130,184))
            MOUSE_POS_G1 = True
            if MOUSE_POS_G1 == True:
                if CLICK == 5:
                    G1 = 1
                    #print(G1)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(50,266,130,184))
            MOUSE_POS_G1 = False     
       
        if 1100 + 130 > PLAY_MOUSE_POS[0] > 1100 and 266 + 184 > PLAY_MOUSE_POS[1] > 266:
            pygame.draw.rect(SCREEN, white,(1100,266,130,184))
            MOUSE_POS_G2 = True
            if MOUSE_POS_G2 == True:
                if CLICK == 5:
                    G2 = 1
                    #print(G2)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(1100,266,130,184))
            MOUSE_POS_G2 = False

        if 50 + 130 > PLAY_MOUSE_POS[0] > 50 and 50 + 184 > PLAY_MOUSE_POS[1] > 50:
            pygame.draw.rect(SCREEN, white,(50,50,130,184))
            MOUSE_POS_F1 = True
            if MOUSE_POS_F1 == True:
                if CLICK == 5:
                    F1 = 1
                    #print(F1)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(50,50,130,184))
            MOUSE_POS_F1 = False

        if 1100 + 130 > PLAY_MOUSE_POS[0] > 1100 and 50 + 184 > PLAY_MOUSE_POS[1] > 50:
            pygame.draw.rect(SCREEN, white,(1100,50,130,184))
            MOUSE_POS_F2 = True
            if MOUSE_POS_F2 == True:
                if CLICK == 5:
                    F2 = 1
                    #print(F2)      
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
            if MOUSE_POS_R11 == True:
                if CLICK == 5 and P1 == 1 and R12 == 0 and R13 == 0:
                    R11 = 1
                    S1_R1 = 1
                    #print(R11)      
                if CLICK != 0:
                    CLICK -= 1
        elif S1_R1 == 0:
            if P1 == 1:
                pygame.draw.rect(SCREEN, green,(208,454,184,130))
        else:
            pygame.draw.rect(SCREEN, blue,(208,134,184,130))
            MOUSE_POS_R11 = False

        if 208 + 184 > PLAY_MOUSE_POS[0] > 208 and 294 + 130 > PLAY_MOUSE_POS[1] > 294:
            pygame.draw.rect(SCREEN, white,(208,294,184,130))
            MOUSE_POS_R12 = True
            if MOUSE_POS_R12 == True:
                if CLICK == 5 and P1 == 1 and R11 == 0 and R13 == 0:
                    R12 = 1
                    S1_R1 = 1
                    #print(R12)      
                if CLICK != 0:
                    CLICK -= 1
        elif S1_R1 == 0:
            if P1 == 1:
                pygame.draw.rect(SCREEN, green,(208,454,184,130))
        else:
            pygame.draw.rect(SCREEN, blue,(208,294,184,130))
            MOUSE_POS_R12 = False

        if 208 + 184 > PLAY_MOUSE_POS[0] > 208 and 454 + 130 > PLAY_MOUSE_POS[1] > 454:
            pygame.draw.rect(SCREEN, white,(208,454,184,130))
            MOUSE_POS_R13 = True
            if MOUSE_POS_R13 == True:
                if CLICK == 5 and P1 == 1 and R11 == 0 and R12 == 0:
                    R13 = 1
                    S1_R1 = 1
                    #print(R13)      
                if CLICK != 0:
                    CLICK -= 1
        elif S1_R1 == 0:
            if P1 == 1:
                pygame.draw.rect(SCREEN, green,(208,454,184,130))
        else:
            pygame.draw.rect(SCREEN, blue,(208,454,184,130))
            MOUSE_POS_R13 = False
#R2
        if 431 + 184 > PLAY_MOUSE_POS[0] > 431 and 134 + 130 > PLAY_MOUSE_POS[1] > 134:
            pygame.draw.rect(SCREEN, white,(431,134,184,130))
            MOUSE_POS_R21 = True
            if MOUSE_POS_R21 == True:
                if CLICK == 5 and R22 == 0 and R23 == 0:
                    R21 = 1
                    #print(R21)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(431,134,184,130))
            MOUSE_POS_R21 = False

        if 431 + 184 > PLAY_MOUSE_POS[0] > 431 and 294 + 130 > PLAY_MOUSE_POS[1] > 294:
            pygame.draw.rect(SCREEN, white,(431,294,184,130))
            MOUSE_POS_R22 = True
            if MOUSE_POS_R22 == True:
                if CLICK == 5 and R21 == 0 and R23 == 0:
                    R22 = 1
                    #print(R22)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(431,294,184,130))
            MOUSE_POS_R22 = False

        if 431 + 184 > PLAY_MOUSE_POS[0] > 431 and 454 + 130 > PLAY_MOUSE_POS[1] > 454:
            pygame.draw.rect(SCREEN, white,(431,454,184,130))
            MOUSE_POS_R23 = True
            if MOUSE_POS_R23 == True:
                if CLICK == 5 and R21 == 0 and R22 == 0:
                    R23 = 1
                    #print(R23)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(431,454,184,130))
            MOUSE_POS_R23 = False
#R3
        if 669 + 184 > PLAY_MOUSE_POS[0] > 669 and 134 + 130 > PLAY_MOUSE_POS[1] > 134:
            pygame.draw.rect(SCREEN, white,(669,134,184,130))
            MOUSE_POS_R31 = True
            if MOUSE_POS_R31 == True:
                if CLICK == 5 and R32 == 0 and R33 == 0:
                    R31 = 1
                    #print(R31)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(669,134,184,130))
            MOUSE_POS_R31 = False

        if 669 + 184 > PLAY_MOUSE_POS[0] > 669 and 294 + 130 > PLAY_MOUSE_POS[1] > 294:
            pygame.draw.rect(SCREEN, white,(669,294,184,130))
            MOUSE_POS_R32 = True
            if MOUSE_POS_R32 == True:
                if CLICK == 5 and R31 == 0 and R33 == 0:
                    R32 = 1
                    #print(R32)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(669,294,184,130))
            MOUSE_POS_R32 = False

        if 669 + 184 > PLAY_MOUSE_POS[0] > 669 and 454 + 130 > PLAY_MOUSE_POS[1] > 454:
            pygame.draw.rect(SCREEN, white,(669,454,184,130))
            MOUSE_POS_R33 = True
            if MOUSE_POS_R33 == True:
                if CLICK == 5 and R31 == 0 and R32 == 0:
                    R33 = 1
                    #print(R33)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(669,454,184,130))
            MOUSE_POS_R33 = False
#R4
        if 892 + 184 > PLAY_MOUSE_POS[0] > 892 and 134 + 130 > PLAY_MOUSE_POS[1] > 134:
            pygame.draw.rect(SCREEN, white,(892,134,184,130))
            MOUSE_POS_R41 = True
            if MOUSE_POS_R41 == True:
                if CLICK == 5 and P2 == 1 and R42 == 0 and R43 == 0:
                    R41 = 1
                    #print(R41)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(892,134,184,130))
            MOUSE_POS_R41 = False
        
        if 892 + 184 > PLAY_MOUSE_POS[0] > 892 and 294 + 130 > PLAY_MOUSE_POS[1] > 294:
            pygame.draw.rect(SCREEN, white,(892,294,184,130))
            MOUSE_POS_R42 = True
            if MOUSE_POS_R42 == True:
                if CLICK == 5 and P2 == 1 and R41 == 0 and R43 == 0:
                    R42 = 1
                    #print(R42)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(892,294,184,130))
            MOUSE_POS_R42 = False

        if 892 + 184 > PLAY_MOUSE_POS[0] > 892 and 454 + 130 > PLAY_MOUSE_POS[1] > 454:
            pygame.draw.rect(SCREEN, white,(892,454,184,130))
            MOUSE_POS_R43 = True
            if MOUSE_POS_R43 == True:
                if CLICK == 5 and P2 == 1 and R41 == 0 and R42 == 0:
                    R43 = 1
                    #print(R43)      
                if CLICK != 0:
                    CLICK -= 1
        else:
            pygame.draw.rect(SCREEN, blue,(892,454,184,130))
            MOUSE_POS_R43 = False        
##################### RAND KARTEN ###########################
        if P1 == 0:
            SCREEN.blit(frame_P1[0], (52, 488))
        elif P1 == 1:
            SCREEN.blit(CARDS_P1[0][0], (52, 488))
        elif P1 == 2:
            SCREEN.blit(CARDS_P1[1][0], (52, 488))
        elif P1 == 3:
            SCREEN.blit(CARDS_P1[2][0], (52, 488))
        elif P1 == 4:
            SCREEN.blit(CARDS_P1[3][0], (52, 488))
        elif P1 == 5:
            SCREEN.blit(CARDS_P1[4][0], (52, 488))
        elif P1 == 6:
            SCREEN.blit(CARDS_P1[5][0], (52, 488))
        elif P1 == 7:
            SCREEN.blit(CARDS_P1[6][0], (52, 488))
        elif P1 == 8:
            SCREEN.blit(CARDS_P1[7][0], (52, 488))
        elif P1 == 9:
            SCREEN.blit(CARDS_P1[8][0], (52, 488))
        elif P1 == 10:
            SCREEN.blit(CARDS_P1[9][0], (52, 488))

        if P2 == 0:
            SCREEN.blit(frame_P2[0], (1102, 488))
        elif P2 == 1:
            SCREEN.blit(CARDS_P2[0][0], (1102, 488))
        elif P2 == 2:
            SCREEN.blit(CARDS_P2[1][0], (1102, 488))
        elif P2 == 3:
            SCREEN.blit(CARDS_P2[2][0], (1102, 488))
        elif P2 == 4:
            SCREEN.blit(CARDS_P2[3][0], (1102, 488))
        elif P2 == 5:
            SCREEN.blit(CARDS_P2[4][0], (1102, 488))
        elif P2 == 6:
            SCREEN.blit(CARDS_P2[5][0], (1102, 488))
        elif P2 == 7:
            SCREEN.blit(CARDS_P2[6][0], (1102, 488))
        elif P2 == 8:
            SCREEN.blit(CARDS_P2[7][0], (1102, 488))
        elif P2 == 9:
            SCREEN.blit(CARDS_P2[8][0], (1102, 488))
        elif P2 == 10:
            SCREEN.blit(CARDS_P2[9][0], (1102, 488))

        if G1 == 0:
            SCREEN.blit(frame_G1[0], (52, 268))
        elif G1 == 1:
            SCREEN.blit(CARDS_P1[1][0], (52, 268))

        if G2 == 0:
            SCREEN.blit(frame_G2[0], (1102, 268))
        elif G2 == 1:
            SCREEN.blit(CARDS_P2[1][0], (1102, 268))

        if F1 == 0:
            SCREEN.blit(frame_F1[0], (52, 52))
        elif F1 == 1:
            SCREEN.blit(CARDS_P1[2][0], (52, 52))

        if F2 == 0:
            SCREEN.blit(frame_F2[0], (1102, 52))
        elif F2 == 1:
            SCREEN.blit(CARDS_P2[2][0], (1102, 52))
##################### Reihe 1-4 KARTEN ###########################
#R1
        if R11 == 0:
            SCREEN.blit(frame_R11[0], (210, 136))
        elif R11 == 1:
            SCREEN.blit(CARDS_TABLE2[0][0], (210, 136))
        if R12 == 0:
            SCREEN.blit(frame_R12[0], (210, 296))
        elif R12 == 1:
            SCREEN.blit(CARDS_TABLE2[1][0], (210, 296))
        if R13 == 0:
            SCREEN.blit(frame_R13[0], (210, 456))
        elif R13 == 1:
            SCREEN.blit(CARDS_TABLE2[2][0], (210, 456))
#R2
        if R21 == 0:
            SCREEN.blit(frame_R21[0], (433, 136))
        elif R21 == 1:
            SCREEN.blit(CARDS_TABLE2[3][0], (433, 136))
        if R22 == 0:
            SCREEN.blit(frame_R22[0], (433, 296))
        elif R22 == 1:
            SCREEN.blit(CARDS_TABLE2[4][0], (433, 296))
        if R23 == 0:
            SCREEN.blit(frame_R23[0], (433, 456))
        elif R23 == 1:
            SCREEN.blit(CARDS_TABLE2[5][0], (433, 456))
#R3
        if R31 == 0:
            SCREEN.blit(frame_R31[0], (671, 136))
        elif R31 == 1:
            SCREEN.blit(CARDS_TABLE2[6][0], (671, 136))
        if R32 == 0:
            SCREEN.blit(frame_R32[0], (671, 296))
        elif R32 == 1:
            SCREEN.blit(CARDS_TABLE2[7][0], (671, 296))
        if R33 == 0:
            SCREEN.blit(frame_R33[0], (671, 456))
        elif R33 == 1:
            SCREEN.blit(CARDS_TABLE2[8][0], (671, 456))
#R4
        if R41 == 0:
            SCREEN.blit(frame_R41[0], (894, 136))
        elif R41 == 1:
            SCREEN.blit(CARDS_TABLE2[9][0], (894, 136))
        if R42 == 0:
            SCREEN.blit(frame_R42[0], (894, 296))
        elif R42 == 1:
            SCREEN.blit(CARDS_TABLE2[10][0], (894, 296))
        if R43 == 0:
            SCREEN.blit(frame_R43[0], (894, 456))
        elif R43 == 1:
            SCREEN.blit(CARDS_TABLE2[11][0], (894, 456))
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
            if event.type == pygame.MOUSEBUTTONDOWN:#Wenn Maustaste gedrückt wird...
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):#...und wenn Maus auf festgelegter position ist...
                    click_sound.play()#...spiele den Sound ab...
                    play()#...und führe die Funktion aus
                if CLICK == 0:#Wenn Maustaste gedrückt wird und die Variable den festgelegtem Wert hat...
                    CLICK = 5#...lege den Wert der Variable auf
        clock.tick(60)#Legt fest wie oft die schleife durchlaufen wird (60 x in der Sekunde)
        pygame.display.update()#Bildschirm wird aktualisiert
    
def skin_select():
    pygame.display.set_caption("Skin Selection")
    global BG_PSC_SELECT
    global CARD_SELECT
    global CB_SELECT

    while True:
        SKIN_SELECT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#2b2a2a")

        if CB_SELECT ==0:
            cbtxt = "Colorblindmode off"
        else:
            cbtxt = "Colorblindmode on"

        if BG_PSC_SELECT == 0:
            bgtxt = "Soccer BG: Standard"
        elif BG_PSC_SELECT == 1:
            bgtxt = "Soccer BG: Fire and water"
        elif BG_PSC_SELECT == 2:
            bgtxt = "Soccer BG: Fire and ice"
        elif BG_PSC_SELECT == 3:
            bgtxt ="Soccer BG: High Contrast"
        elif BG_PSC_SELECT == 4:
            bgtxt = "Soccer BG: Tabletop"
        elif BG_PSC_SELECT == 5:
            bgtxt = "Soccer BG: Test Image"
        else:
            bgtxt = "Soccer BG: Standard"

        if CARD_SELECT == 0:
            cardtxt = "Cards: Standard" 
        elif CARD_SELECT == 1:
            cardtxt = "Cards: Red Prayers"
        else:
            cardtxt = "Cards: Standard"

        SKIN_SELECT_BACK = Button(image=None, pos=(640, 560), 
                            text_input="Back", font=get_font(60), base_color="WHITE", hovering_color="Green")

        SKIN_SELECT_BACK.changeColor(SKIN_SELECT_MOUSE_POS)
        SKIN_SELECT_BACK.update(SCREEN)

        SKIN_SELECT_CARDSOCCER_BG = Button(image=None, pos=(640, 360), 
                            text_input=bgtxt, font=get_font(60), base_color="WHITE", hovering_color="Green")

        SKIN_SELECT_CARDSOCCER_BG.changeColor(SKIN_SELECT_MOUSE_POS)
        SKIN_SELECT_CARDSOCCER_BG.update(SCREEN)

        SKIN_SELECT_CARDS = Button(image=None, pos=(640, 260), 
                            text_input=cardtxt, font=get_font(60), base_color="WHITE", hovering_color="Green")

        SKIN_SELECT_CARDS.changeColor(SKIN_SELECT_MOUSE_POS)
        SKIN_SELECT_CARDS.update(SCREEN)

        SKIN_CB_SELECT = Button(image=None, pos=(640, 460), 
                            text_input=cbtxt, font=get_font(60), base_color="WHITE", hovering_color="Green")

        SKIN_CB_SELECT.changeColor(SKIN_SELECT_MOUSE_POS)
        SKIN_CB_SELECT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                click_sound.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_SELECT_CARDSOCCER_BG.checkForInput(SKIN_SELECT_MOUSE_POS):
                    click_sound.play()
                    if BG_PSC_SELECT == 4:
                        BG_PSC_SELECT = 0
                    else:
                        BG_PSC_SELECT += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_SELECT_CARDS.checkForInput(SKIN_SELECT_MOUSE_POS):
                    click_sound.play()
                    if CARD_SELECT == 1:
                        CARD_SELECT = 0
                    else:
                        CARD_SELECT += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_CB_SELECT.checkForInput(SKIN_SELECT_MOUSE_POS):
                    click_sound.play()
                    if CB_SELECT == 1:
                        CB_SELECT = 0
                    else:
                        CB_SELECT += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_SELECT_BACK.checkForInput(SKIN_SELECT_MOUSE_POS):
                    click_sound.play()
                    options()
        
        pygame.display.update()

def options():

    pygame.display.set_caption("Options")

    global fullscreen
    global music
    BG = pygame.image.load("assets/bg_test1.png")
    BG = pygame.transform.scale(BG,( 2520, 1280))
    while True:
        SCREEN.fill("#2b2a2a")
        SCREEN.blit(BG, (-250, -300))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        if fullscreen == True:
            fullscreentxt = "Fullscreen ON"
        else:
            fullscreentxt = "Fullscreen OFF"

        if music == False:
            musictxt = "Music off"
        else:
            musictxt = "Music on"

        #OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "WHITE")
        #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_FULLSCREEN = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 260), 
                            text_input=fullscreentxt, font=get_font(75), base_color="WHITE", hovering_color="Green")
        OPTIONS_FULLSCREEN.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_FULLSCREEN.update(SCREEN)
         
        OPTIONS_MUSIC = Button(image=None, pos=(640, 360), 
                            text_input=musictxt, font=get_font(75), base_color="WHITE", hovering_color="Green")
        OPTIONS_MUSIC.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MUSIC.update(SCREEN)

        OPTIONS_SKINS = Button(image=None, pos=(640, 460), 
                            text_input="Skin Menu", font=get_font(75), base_color="WHITE", hovering_color="Green")
        OPTIONS_SKINS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_SKINS.update(SCREEN)

        OPTIONS_BACK = Button(image=None, pos=(640, 560), 
                            text_input="Back", font=get_font(75), base_color="WHITE", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

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
        SCREEN.blit(BG, (-400, -100))

        MENU_MOUSE_POS = pygame.mouse.get_pos() 
        #MENU_TEXT = get_font(120).render("MENU", True, "#e0cfb1")
        #MENU_RECT = MENU_TEXT.get_rect(center=(630, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(630, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#ffffff", hovering_color="#0ba4e0")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(630, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#ffffff", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(630, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#ffffff", hovering_color="Red")

        #SCREEN.blit(MENU_TEXT, MENU_RECT)

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