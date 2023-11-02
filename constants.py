import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

size_of_screen = pygame.display.get_desktop_sizes()

if size_of_screen[0][0] / size_of_screen[0][1] > 1280 / 720:
    height = size_of_screen[0][1]
    width = size_of_screen[0][1] / 720 * 1280
else:
    width = size_of_screen[0][0]
    height = size_of_screen[0][0] / 1280 * 720

fps = 30

fade_speed = 10
zoom_factor = 1.45

icon = pygame.image.load('images/icon.png')

kurzor1 = pygame.transform.scale(pygame.image.load('images/kurzor2.png'), (width / 1280 * 30, width / 1280 * 30))
kurzor2 = pygame.transform.scale(pygame.image.load('images/kurzor1.png'), (width / 1280 * 30, width / 1280 * 30))
kurzor3 = pygame.transform.scale(pygame.image.load('images/kurzor3.png'), (width / 1280 * 30, width / 1280 * 30))

mouse_images = [
    kurzor1, # klasicka sipka
    kurzor2, # paprca
    kurzor3, # otaznik
    pygame.transform.flip(pygame.transform.rotate(kurzor2, 90), False, True), # sipka dolava
    pygame.transform.rotate(kurzor2, 270), # sipka doprava
    pygame.transform.rotate(kurzor2, 180) # sipka dole
]

room0image = pygame.transform.scale(pygame.image.load('images/scena1.png'), (width, height))
room1image = pygame.transform.scale(pygame.image.load('images/scena3.png'), (width, height))
room2image = pygame.transform.scale(pygame.image.load('images/scena2.png'), (width, height))

locked_trapdoors_image = pygame.transform.scale(pygame.image.load('images/cutsceny/4.png'), (width, height))
chalice_image = pygame.transform.scale(pygame.image.load('images/cutsceny/2.png'), (width, height))
unlocked_trapdoors_image = pygame.transform.scale(pygame.image.load('images/cutsceny/5.png'), (width, height))
axe = pygame.transform.scale(pygame.image.load('images/cutsceny/sekera.png'), (width * 0.2, width * 0.4))
diary1_image = pygame.transform.scale(pygame.image.load('images/cutsceny/strana1.png'), (width, height))
diary2_image = pygame.transform.scale(pygame.image.load('images/cutsceny/strana2.png'), (width, height))
bible_image = pygame.transform.scale(pygame.image.load('images/cutsceny/3.png'), (width, height))
jew_book_image = pygame.transform.scale(pygame.image.load('images/cutsceny/jew.png'), (width, height))
organ_image = pygame.transform.scale(pygame.image.load('images/cutsceny/8.png'), (width, height))
paper_minigame_image = pygame.transform.scale(pygame.image.load('images/cutsceny/6.png'), (width, height))
arrow_back = pygame.transform.scale(pygame.image.load('images/sipka.png'), (width * 0.1, width * 0.05))
restart_image = pygame.transform.scale(pygame.image.load('images/restart.png'), (width * 0.075, width * 0.075))
trezor_image = pygame.transform.scale(pygame.image.load('images/cutsceny/trezor.png'), (width, height))
banner_image = pygame.transform.scale(pygame.image.load('images/banner.png'), (width * 0.6, width * 0.6 / 4))
end_image = pygame.transform.scale(pygame.image.load('images/cutsceny/10.png'), (width, height))
help_image = pygame.transform.scale(mouse_images[2], (width * 0.075, width * 0.075))

retarded_constant_because_images_are_not_symetrical = width * 0.02

small_font = pygame.font.SysFont('Calibri', int(width / 1280 * 20))
classic_font = pygame.font.SysFont('Calibri', int(width / 1280 * 30))
big_font = pygame.font.SysFont('Calibri', int(width / 1280 * 70))
font_color = (220, 220, 220)

click_to_play_again_text = small_font.render('Click to hear again', False, (20, 20, 20))

falling_screen = pygame.Surface((width, height))
falling_screen.blit(classic_font.render('Uf, Spadol som! Prečo ten pád znel tak duto? Je tu nejaký starý poklop.', False, (230, 230, 230)), (width * 0.1, height * 0.9))

interaction_sound = pygame.mixer.Sound('sound/click.mp3')

clock = pygame.time.Clock()
win = pygame.display.set_mode((width, height))