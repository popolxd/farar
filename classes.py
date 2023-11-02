import pygame
from basic_funcs import *
from constants import *
from copy import deepcopy

class Player:
    def __init__(self):
        self.current_image = 0
        self.current_motion = 5

        self.need_to_animate_perpetually = False
        self.need_to_animate_one_time = False

        self.x = 0
        self.y = height * 0.65

        self.x_size = width * 0.13
        self.y_size = width * 0.13

        self.x_size_zoomed = zoom_factor * self.x_size
        self.y_size_zoomed = zoom_factor * self.y_size

        self.player_movement_images = [pygame.transform.scale(pygame.image.load('images/chodza-nova1.png'), (self.x_size, self.y_size)), pygame.transform.scale(pygame.image.load('images/chodza-nova2.png'), (self.x_size, self.y_size)), pygame.transform.scale(pygame.image.load('images/chodza-nova3.png'), (self.x_size, self.y_size)), pygame.transform.scale(pygame.image.load('images/chodza-nova4.png'), (self.x_size, self.y_size))]
        self.player_interaction_images = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/farar-bok.png'), (self.x_size, self.y_size)), True, False), pygame.transform.scale(pygame.image.load('images/farar-interakcia1.png'), (self.x_size, self.y_size)), pygame.transform.scale(pygame.image.load('images/farar-interakcia2.png'), (self.x_size, self.y_size)), pygame.transform.scale(pygame.image.load('images/farar-interakcia3.png'), (self.x_size, self.y_size)), pygame.transform.scale(pygame.image.load('images/farar-interakcia4.png'), (self.x_size, self.y_size))]
        self.player_standing_images = [pygame.transform.scale(pygame.image.load('images/farar-bok.png'), (self.x_size, self.y_size)), pygame.transform.scale(pygame.image.load('images/farar-zad.png'), (self.x_size, self.y_size))]

        self.player_movement_images_zoomed = [pygame.transform.scale(pygame.image.load('images/chodza-nova1.png'), (self.x_size_zoomed, self.y_size_zoomed)), pygame.transform.scale(pygame.image.load('images/chodza-nova2.png'), (self.x_size_zoomed, self.y_size_zoomed)), pygame.transform.scale(pygame.image.load('images/chodza-nova3.png'), (self.x_size_zoomed, self.y_size_zoomed)), pygame.transform.scale(pygame.image.load('images/chodza-nova4.png'), (self.x_size_zoomed, self.y_size_zoomed))]
        self.player_interaction_images_zoomed = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/farar-bok.png'), (self.x_size_zoomed, self.y_size_zoomed)), True, False), pygame.transform.scale(pygame.image.load('images/farar-interakcia1.png'), (self.x_size_zoomed, self.y_size_zoomed)), pygame.transform.scale(pygame.image.load('images/farar-interakcia2.png'), (self.x_size_zoomed, self.y_size_zoomed)), pygame.transform.scale(pygame.image.load('images/farar-interakcia3.png'), (self.x_size_zoomed, self.y_size_zoomed)), pygame.transform.scale(pygame.image.load('images/farar-interakcia4.png'), (self.x_size_zoomed, self.y_size_zoomed))]
        self.player_standing_images_zoomed = [pygame.transform.scale(pygame.image.load('images/farar-bok.png'), (self.x_size_zoomed, self.y_size_zoomed)), pygame.transform.scale(pygame.image.load('images/farar-zad.png'), (self.x_size_zoomed, self.y_size_zoomed))]

        self.player_images = [
            [self.player_standing_images[1]], # back pickup
            [self.player_movement_images[0], self.player_movement_images[1], self.player_movement_images[2], self.player_movement_images[3]], # right
            [pygame.transform.flip(self.player_movement_images[0], True, False), pygame.transform.flip(self.player_movement_images[1], True, False), pygame.transform.flip(self.player_movement_images[2], True, False), pygame.transform.flip(self.player_movement_images[3], True, False)], # left
            [self.player_interaction_images[0], self.player_interaction_images[1], self.player_interaction_images[2], self.player_interaction_images[3], self.player_interaction_images[4], self.player_interaction_images[3], self.player_interaction_images[2], self.player_interaction_images[1], self.player_interaction_images[0]], # right pickup
            [pygame.transform.flip(self.player_interaction_images[0], True, False), pygame.transform.flip(self.player_interaction_images[1], True, False), pygame.transform.flip(self.player_interaction_images[2], True, False), pygame.transform.flip(self.player_interaction_images[3], True, False), pygame.transform.flip(self.player_interaction_images[4], True, False), pygame.transform.flip(self.player_interaction_images[3], True, False), pygame.transform.flip(self.player_interaction_images[2], True, False), pygame.transform.flip(self.player_interaction_images[1], True, False), pygame.transform.flip(self.player_interaction_images[0], True, False)], # left pickup
            [pygame.transform.flip(self.player_standing_images[0], True, False)], # standing still right
            [self.player_standing_images[0]], # standing still left
        ]

        self.player_images_zoomed = [
            [self.player_standing_images_zoomed[1]], # back pickup
            [self.player_movement_images_zoomed[0], self.player_movement_images_zoomed[1], self.player_movement_images_zoomed[2], self.player_movement_images_zoomed[3]], # right
            [pygame.transform.flip(self.player_movement_images_zoomed[0], True, False), pygame.transform.flip(self.player_movement_images_zoomed[1], True, False), pygame.transform.flip(self.player_movement_images_zoomed[2], True, False), pygame.transform.flip(self.player_movement_images_zoomed[3], True, False)], # left
            [self.player_interaction_images_zoomed[0], self.player_interaction_images_zoomed[1], self.player_interaction_images_zoomed[2], self.player_interaction_images_zoomed[3], self.player_interaction_images_zoomed[4], self.player_interaction_images_zoomed[3], self.player_interaction_images_zoomed[2], self.player_interaction_images_zoomed[1], self.player_interaction_images_zoomed[0]], # right pickup
            [pygame.transform.flip(self.player_interaction_images_zoomed[0], True, False), pygame.transform.flip(self.player_interaction_images_zoomed[1], True, False), pygame.transform.flip(self.player_interaction_images_zoomed[2], True, False), pygame.transform.flip(self.player_interaction_images_zoomed[3], True, False), pygame.transform.flip(self.player_interaction_images_zoomed[4], True, False), pygame.transform.flip(self.player_interaction_images_zoomed[3], True, False), pygame.transform.flip(self.player_interaction_images_zoomed[2], True, False), pygame.transform.flip(self.player_interaction_images_zoomed[1], True, False), pygame.transform.flip(self.player_interaction_images_zoomed[0], True, False)], # left pickup
            [pygame.transform.flip(self.player_standing_images_zoomed[0], True, False)], # standing still right
            [self.player_standing_images_zoomed[0]], # standing still left
        ]

        self.player_rect = pygame.Rect(self.x, self.y, width * 0.1, width * 0.1)
        self.player_velocity = 600 / fps # daj to potom späť na 300

        self.target_pos_x = self.x

    def draw(self, zoomed):
        if zoomed:
            win.blit(self.player_images_zoomed[self.current_motion][int(self.current_image)], (self.player_rect.x - self.player_rect.size[0] * (zoom_factor - 1) / 2, self.player_rect.y - self.player_rect.size[1] * (zoom_factor - 1)))  
        else:
            win.blit(self.player_images[self.current_motion][int(self.current_image)], (self.player_rect.x, self.player_rect.y))  

    def move(self, zoomed_factor):
        if self.target_pos_x != self.player_rect.x: # toto budem musiet doriesit aj pre ypsilonovu a nejake paths spravit
            if abs(self.target_pos_x - self.player_rect.x) <= self.player_velocity * zoomed_factor:
                self.player_rect.x = self.target_pos_x
                self.need_to_animate_perpetually = False
                self.current_image = 0
            else:
                if self.player_rect.x > self.target_pos_x:
                    self.player_rect.x -= self.player_velocity * zoomed_factor
                else:
                    self.player_rect.x += self.player_velocity * zoomed_factor

        if self.need_to_animate_perpetually:
            self.animate_perpetually()
        elif self.need_to_animate_one_time:
            self.animate_one_time()

    def animate_perpetually(self):
        self.current_image += 5 / fps

        if self.current_image >= len(self.player_images[self.current_motion]):
            self.current_image = 0

    def animate_one_time(self):
        self.current_image += 10 / fps

        if self.current_image >= len(self.player_images[self.current_motion]):
            self.current_image = 0
            self.need_to_animate_one_time = False

    def change_position(self, new_x, new_y):
        self.player_rect.x = new_x
        self.player_rect.y = new_y
        self.target_pos_x = new_x

    def change_target_pos(self, new_target, target_width, in_background): # budem musiet nejake paths spravit
        if in_background:
            self.target_pos_x = int(new_target - self.player_rect.size[0] / 2 + target_width / 2 - retarded_constant_because_images_are_not_symetrical)
        else:
            if new_target > self.player_rect.x:
                self.target_pos_x = new_target - self.player_rect.size[0],
                self.target_pos_x = self.target_pos_x[0] # TOTO ROBIM LEBO TEN PYTHON JE RETARDOVANY
            elif new_target < self.player_rect.x:
                self.target_pos_x = int(new_target + target_width  - retarded_constant_because_images_are_not_symetrical)

        if self.target_pos_x > self.player_rect.x:
                self.current_motion = 1
        elif self.target_pos_x < self.player_rect.x:
            self.current_motion = 2

        self.need_to_animate_perpetually = True

    def change_motion(self, next_motion, optional=-1): # ked dochodil a ide volaco pickupnut
        if next_motion == 'back_interact':
            self.current_motion = 0
            self.need_to_animate_one_time = True

        elif next_motion == 'standing_still':
            if self.current_motion == 1:
                self.current_motion = 5
            elif self.current_motion == 2:
                self.current_motion = 6
            else:
                self.current_motion = optional
        
        else: # tuto budem striedat medzi left alebo right pickup
            if self.current_motion == 1:
                self.current_motion = 3
            elif self.current_motion == 2:
                self.current_motion = 4
            else:
                self.current_motion = optional

            self.need_to_animate_one_time = True

    def ended_movement(self):
        return True if self.target_pos_x == self.player_rect.x  else False
    
    def get_player_hint_rect(self):
        return pygame.Rect(self.player_rect.x + self.player_rect.size[0] / 4, self.player_rect.y, self.player_rect.size[0] / 2, self.player_rect.size[1])
    
class RoomManager:
    def __init__(self):
        self.current_room = 0
        self.current_cursor_image = 0

        self.light_precision = 50
        self.reach_constant = width * 0.5 / self.light_precision

        self.room_lightings = [pygame.Surface((width, height), pygame.SRCALPHA), pygame.Surface((width, height), pygame.SRCALPHA), pygame.Surface((width, height), pygame.SRCALPHA)]

        self.lowest_lightings = [150, 150, 150]
        self.static_lights_pos = [(width * 0.2 - width * 0.025, height * 0.5), 
                                  (width * 0.25 + width * 0.02 * zoom_factor, height * 0.25), 
                                  (width * 0.47 - width * 0.025, height * 0.45)]

        for i in range(3):
            self.room_lightings[i].fill((0, 0, 0, self.lowest_lightings[i]))
            self.room_lightings[i] = draw_light(self.light_precision, self.reach_constant, self.room_lightings[i], self.lowest_lightings[i], self.static_lights_pos[i][0], self.static_lights_pos[i][1])

        self.backgrounds = [room0image, room1image, room2image]
        self.foregrounds = [] # not yet implemented

        self.doors = [
            [
                {
                    'name': 'door0to1',
                    'rect': pygame.Rect(width * 0.06, height * 0.65, width * 0.1, height * 0.25),
                    'when_interactable': 0,
                    'in_background': True,
                    'cursor_image': 1,
                },
                {
                    'name': 'door0to2',
                    'rect': pygame.Rect(width * 0.95, 0, width * 0.05, height),
                    'when_interactable': 0,
                    'in_background': True,
                    'cursor_image': 4,
                },
                {
                    'name': 'door book',
                    'rect': pygame.Rect(width * 0.895, height * 0.73, width * 0.02, height * 0.05),
                    'when_interactable': 6,
                    'in_background': True
                }
            ],
            [
                {
                    'name': 'door1to0',
                    'rect': pygame.Rect(width * 0.208, height * 0.58, width * 0.14, height * 0.3),
                    'when_interactable': 0,
                    'in_background': True,
                    'cursor_image': 5,
                },
                {
                    'name': 'door organ',
                    'rect': pygame.Rect(width * 0.68, height * 0.4, width * 0.18, height * 0.4),
                    'when_interactable': 0,
                    'in_background': True,
                }
            ],
            [
                {
                    'name': 'door2to0',
                    'rect': pygame.Rect(width * 0.15, 0, width * 0.05, height),
                    'when_interactable': 0,
                    'in_background': True,
                    'cursor_image': 3,
                },
                {
                    'name': 'door chalice',
                    'rect': pygame.Rect(width * 0.43, height * 0.67, width * 0.0205, height * 0.041),
                    'when_interactable': 4,
                    'in_background': False,
                },
                {
                    'name': 'door bible',
                    'rect': pygame.Rect(width * 0.47, height * 0.69, width * 0.032, height * 0.03),
                    'when_interactable': 0,
                    'in_background': True,
                }
            ]
        ]

        self.items = [
            [ ### HLAVNA MIESTNOST ###
                {
                    'name': 'lit candlestick',
                    'rect': pygame.Rect(width * 0.2, height * 0.5, width * 0.05, width * 0.05 / 39 * 65),
                    'image': pygame.transform.scale(pygame.image.load('images/svietnik1.png'), (width * 0.05, width * 0.05 / 39 * 65)),
                    'when_interactable': -1,
                },
                {
                    'name': 'lighter',
                    'rect': pygame.Rect(width * 0.562, height * 0.787, width * 0.0075, width * 0.015),
                    'image': pygame.transform.scale(pygame.image.load('images/zapalovac.png'), (width * 0.0075, width * 0.015)),
                    'when_interactable': 0,
                    'interaction_message': 'Zobral si zapaľovač.',
                    'monolog': 'Aha, tu ho mám! Keby som len ten svietnik dočiahol...',
                    'replace_item': None,
                    'in_background': False,
                },
                {
                    'name': 'place for chair',
                    'rect': pygame.Rect(width * 0.735, height * 0.745, width * 0.04, width * 0.04 / 40 * 70),
                    'image': None,
                    'when_interactable': 2,
                    'interaction_message': 'Položil si stoličku.',
                    'in_background': False,
                    'replace_item': {
                        'name': 'chair in diferent spot',
                        'rect': pygame.Rect(width * 0.735, height * 0.745, width * 0.04, width * 0.04 / 40 * 70),
                        'image': pygame.transform.scale(pygame.image.load('images/stolicka.png'), (width * 0.04, width * 0.04 / 40 * 70)),
                        'when_interactable': -1
                    }

                },
                {
                    'name': 'candelstick',
                    'rect': pygame.Rect(width * 0.73, height * 0.5, width * 0.05, width * 0.05 / 39 * 65),
                    'image': pygame.transform.scale(pygame.image.load('images/svietnik0.png'), (width * 0.05, width * 0.05 / 39 * 65)),
                    'when_interactable': 3,
                    'interaction_message': 'Zapálil si prvé svetlo.',
                    'in_background': True,
                    'failed_interaction_message': {
                        0: 'Nemáš nič na zažanie svetla.',
                        1: 'Nedočiahneš tam, je to moc vysoko.',
                        2: 'Nemáš položenú stoličku'
                    },
                    'replace_item': {
                        'name': 'lit candelstick',
                        'rect': pygame.Rect(width * 0.73, height * 0.5, width * 0.05, width * 0.05 / 39 * 65),
                        'image': pygame.transform.scale(pygame.image.load('images/svietnik1.png'), (width * 0.05, width * 0.05 / 39 * 65)),
                        'when_interactable': -1,
                    }
                },
            ],
            [ ### ORGANOVA MIESTNOST ###
                {
                    'name': 'chair',
                    'rect': pygame.Rect(width * 0.57, height * 0.69, width * 0.04 * zoom_factor, width * 0.04 / 40 * 70 * zoom_factor),
                    'image': pygame.transform.scale(pygame.image.load('images/stolicka.png'), (width * 0.04 * zoom_factor, width * 0.04 / 40 * 70 * zoom_factor)),
                    'when_interactable': 1,
                    'interaction_message': 'Zobral si stoličku',
                    'replace_item': None,
                    'in_background': False
                },
                {
                    'name': 'lit candelstick',
                    'rect': pygame.Rect(width * 0.25, height * 0.25, width * 0.04 * zoom_factor, width * 0.04 / 39 * 65 * zoom_factor),
                    'image': pygame.transform.scale(pygame.image.load('images/svietnik1.png'), (width * 0.04 * zoom_factor, width * 0.04 / 39 * 65 * zoom_factor)),
                    'when_interactable': -1,
                }
            ],
            [ ### OLTAROVA MIESTNOST ###
                {
                    'name': 'altar',
                    'rect': pygame.Rect(width * 0.29, height * 0.59 + width * 0.06, width * 0.04, width * 0.08),
                    'image': pygame.transform.scale(pygame.image.load('images/oltar.png'), (width * 0.04, width * 0.08)),
                    'when_interactable': 11,
                    'interaction_message': 'Rozmlátil si oltár',
                    'in_background': False,
                    'replace_item': None
                },
                {
                    'name': 'lit candelstick',
                    'rect': pygame.Rect(width * 0.47, height * 0.45, width * 0.05, width * 0.05 / 39 * 65),
                    'image': pygame.transform.scale(pygame.image.load('images/svietnik1.png'), (width * 0.05, width * 0.05 / 39 * 65)),
                    'when_interactable': -1,
                }
            ]
        ]

        self.filter = pygame.Surface((width, height), pygame.SRCALPHA)

        self.interactions_made = 0
        self.about_to_interact_with = None

        self.text_visible = False
        self.text_obj = None
        self.text_time = 0

        self.monolog_visible = True
        self.monolog_obj = classic_font.render('Sakra! Zhasol mi svietnik a ja som zabudol, kde som dal zapaľovač.', 0, font_color)
        self.monolog_time = 6 * fps

        self.interactive_image_active = False
        self.current_interactive_image = ''

        self.cut_scenes = [
            [pygame.transform.scale(pygame.image.load('images/cutsceny/1.png'), (width, height))],
            [pygame.transform.scale(pygame.image.load('images/cutsceny/9.png'), (width, height))]
        ]

        self.cut_scene_active = True
        self.cut_scene_time_elapsed = 0
        self.cut_scenes_played = 0
        self.scenes_in_cut_scenes_played = 0
        self.cut_scene_length = [6 * fps, 20 * fps]
        self.fading_length = 2 * fps

        self.skip_one_interact = False

        # trappdoors pin stuff
        self.current_emojis = 'aaaa'
        self.right_emojis = 'eajc'

        self.draw_axe = True

        # organ tones stuff
        self.organ_tones_played = '0000'
        self.right_organ_sound = '5757'

        # minigame stuff
        self.default_map = [
            [2, 2],
            [0, 0],
            [0, 0],
            [0, 0],
            [1, 1]
        ]
        self.map = [
            [2, 2],
            [0, 0],
            [0, 0],
            [0, 0],
            [1, 1]
        ]
        self.right_map = [
            [1, 1],
            [0, 0],
            [0, 0],
            [0, 0],
            [2, 2]
        ]
        self.piece_selected = None
        self.optimal_num_of_moves = 18
        self.num_of_moves_used = 0

        self.show_hint = False

        self.num_of_moves_used_text = classic_font.render('Počet použitých krokov: ' + str(self.num_of_moves_used), False, font_color)

        # animovanie papieriku
        self.total_animation_time = 2 * fps
        self.current_animation_time = 0
        self.animate_paper = False

        # trezor stuff
        self.right_pin = '1234'
        self.current_pin = ''

        self.numbers_of_pin_objs = [big_font.render('', False, font_color)] * 4

        # hints
        self.hints = [
            'Marí sa mi, že je tmavohnedej farby. Určite by som ho nenechal pri organe alebo pri oltári.',
            'Potrebujem niečo, na čo by som sa mohol postaviť. Nejaký kus nábytku...',
            'Stačí tú stoličku už len položiť na správne miesto.',
            'Už na svietnik dočiahnem, treba ho zapáliť',
            'Jaj už viem! Víno je predsa symbolizuje krv!',
            'Asi by som si ten spis mal prečítať, možno v ňom je niečo zaujímavé.',
            'Možnože hladám nejaký predmet, ktorý patril židom. Oni zvykli predmety veľmi dobre označiť.',
            'Treba ich na organe zahrať 2-krát po sebe, v takom poradí, v akom sú v biblii.',
            'Zdrab papiera? Idem sa naň pozreť.',
            '...', # tuto je napoveda priamo v minihre
            'V oltári? Fú, to ho nejako budem musieť zničiť, aby som sa doň dostal.',
            'Teraz už len sa musím dostať do vnútra oltára.',
            'Možno ten organ hral nejaké tóny, ktoré by nejakým spôsobom predstavovali číslice v trezore...',
            '...'
        ]

    def draw(self, click, mouse):
        if not self.cut_scene_active:

            if not self.interactive_image_active:
                win.blit(self.backgrounds[self.current_room], (0, 0))

                for i in self.items[self.current_room]:
                    if i['image'] != None:
                        win.blit(i['image'], (i['rect'].x, i['rect'].y))

                for i in self.doors[self.current_room]:
                    if i['name'] == 'door broken altar' or i['name'] == 'door trapdoors':
                        win.blit(i['image'], (i['rect'].x, i['rect'].y))

                player.draw(True if self.current_room == 1 else False)
                
                win.blit(self.room_lightings[self.current_room], (0, 0))
                win.blit(self.filter, (0, 0))

                if self.animate_paper:
                    self.animate_item(self.items[1][1])
            
            else:
                self.draw_interactive_image_active(click, mouse)

            if self.text_visible and self.text_time > 0: # displaying pop up message
                win.blit(banner_image, (width * 0.2, height * 0.05))
                win.blit(self.text_obj, (width * 0.27, height * 0.15))
                self.text_time -= 1

            if self.monolog_visible and self.monolog_time > 0:
                win.blit(self.monolog_obj, (width * 0.1, height * 0.9))
                self.monolog_time -= 1

        elif self.cut_scene_active:
            self.draw_cut_scene()

        win.blit(mouse_images[self.current_cursor_image], mouse)
        self.current_cursor_image = 0

    def interact(self, click, mouse):
        if self.skip_one_interact:
            self.skip_one_interact = False

        else:
            if not self.cut_scene_active and not self.interactive_image_active:

                if pygame.Rect.collidepoint(player.get_player_hint_rect(), mouse):
                    self.current_cursor_image = 2
                    if click:
                        interaction_sound.play()
                        self.monolog_visible = True
                        self.monolog_time = 6 * fps
                        self.monolog_obj = classic_font.render(self.hints[self.interactions_made], False, font_color)
                
                else:
                    for i in self.items[self.current_room]: # checking items collision
                        if pygame.Rect.collidepoint(i['rect'], mouse):

                            if self.current_cursor_image != 1 and i['when_interactable'] == self.interactions_made: # nastavovanie kurzora
                                self.current_cursor_image = 1

                            if click and self.about_to_interact_with == None:

                                if i['when_interactable'] == self.interactions_made:
                                    interaction_sound.play()
                                    player.change_target_pos(i['rect'].x, i['rect'].size[0], i['in_background'])
                                    self.about_to_interact_with = i

                                else:
                                    if 'failed_interaction_message' in i.keys() and self.interactions_made in i['failed_interaction_message'].keys():

                                        self.text_visible = True
                                        self.text_time = 3 * fps # time of message on the screen
                                        self.text_obj = classic_font.render(i['failed_interaction_message'][self.interactions_made], 0, font_color)

                    for i in self.doors[self.current_room]: # checking doors collision
                        if pygame.Rect.collidepoint(i['rect'], mouse):

                            if i['name'][:5] == 'door ' and i['when_interactable'] <= self.interactions_made:
                                self.current_cursor_image = 1
                            elif i['name'][:5] != 'door ' and i['when_interactable'] <= self.interactions_made:
                                self.current_cursor_image = i['cursor_image']

                            if click and self.about_to_interact_with == None:
                                if i['when_interactable'] <= self.interactions_made:
                                    interaction_sound.play()
                                    player.change_target_pos(i['rect'].x, i['rect'].size[0], i['in_background'])
                                    self.about_to_interact_with = i

                if self.about_to_interact_with != None:
                    if player.ended_movement():
                        self.handle_interaction()

                player.move(zoom_factor if self.current_room == 1 else 1)

    def handle_interaction(self):
        if self.about_to_interact_with['name'][0:4] != 'door':
            self.interactions_made += 1

        self.object_keys = self.about_to_interact_with.keys()


        if self.about_to_interact_with['in_background']:
            player.change_motion('back_interact')
        else:
            player.change_motion('side_interact')

        if 'monolog' in self.object_keys:

            self.monolog_visible = True
            self.monolog_time = 6 * fps
            self.monolog_obj = classic_font.render(self.about_to_interact_with['monolog'], 0, font_color)

        if 'interaction_message' in self.object_keys:

            self.text_visible = True
            self.text_time = 3 * fps # time of message on the screen
            self.text_obj = classic_font.render(self.about_to_interact_with['interaction_message'], 0, font_color)

        if 'replace_item' in self.object_keys:
            if self.about_to_interact_with['replace_item'] != None:
                self.items[self.current_room].append(self.about_to_interact_with['replace_item'])

            self.items[self.current_room].remove(self.about_to_interact_with)
            
        self.handle_special_effects(self.about_to_interact_with)

        self.about_to_interact_with = None

    def handle_special_effects(self, i):
        match i['name']:
            case 'candelstick':
                # doriesovanie svetiel
                self.room_lightings[self.current_room] = draw_light(self.light_precision, 
                    self.reach_constant, 
                    self.room_lightings[self.current_room], 
                    self.lowest_lightings[self.current_room],
                    i['rect'].x + i['rect'].size[0] / 2,
                    i['rect'].y)

                # zapinanie interactive imagu
                self.interactive_image_active = True
                self.current_interactive_image = 'lighting_candlestick'

                # spawnovanie klikatelneho poklopu
                self.doors[self.current_room].append({
                    'name': 'door trapdoors',
                    'rect': pygame.Rect(width * 0.73, height * 0.88, width * 0.05, width * 0.05 / 40 * 6),
                    'image': pygame.transform.scale(pygame.image.load('images/poklop.png'), (width * 0.05, width * 0.05 / 40 * 6)),
                    'when_interactable': 0,
                    'in_background': True,
                })

            case 'door trapdoors':
                self.interactive_image_active = True

                if self.interactions_made < 5:
                    self.current_interactive_image = 'locked_trapdoors'
                else:
                    self.current_interactive_image = 'unlocked_trapdoors'

            case 'door chalice':
                self.interactive_image_active = True
                self.current_interactive_image = 'chalice'

            case 'door bible':
                self.interactive_image_active = True
                self.current_interactive_image = 'bible'

            case 'door book':
                self.interactive_image_active = True
                self.current_interactive_image = 'book'

            case 'door organ':
                self.interactive_image_active = True
                self.current_interactive_image = 'organ'

            case 'paper with minigame':
                self.interactive_image_active = True
                self.current_interactive_image = 'paper with minigame'

            case 'altar':
                self.doors[self.current_room].append({
                    'name': 'door broken altar',
                    'rect': pygame.Rect(width * 0.29, height * 0.59 + width * 0.06, width * 0.04, width * 0.08),
                    'image': pygame.transform.scale(pygame.image.load('images/oltar2.png'), (width * 0.04, width * 0.08)),
                    'when_interactable': 0,
                    'in_background': False,
                })

            case 'door broken altar':
                self.interactive_image_active = True
                self.current_interactive_image = 'inside of altar'

            ### ONLY DOORS ###

            case 'door0to1':
                self.current_room = 1
                player.change_position(width * 0.1, height * 0.65)
                player.change_motion('standing_still', 5)

                if 'monolog' in self.doors[0][0]:
                    self.doors[0][0].pop('monolog')

            case 'door0to2':
                self.current_room = 2
                player.change_position(width * 0.15, height * 0.6)
                player.change_motion('standing_still', 5)

            case 'door1to0':
                self.current_room = 0
                player.change_position(0, height * 0.65)
                player.change_motion('standing_still', 5)

            case 'door2to0':
                self.current_room = 0
                player.change_position(width * 0.9, height * 0.65)
                player.change_motion('standing_still', 6)

    def draw_cut_scene(self):
        win.blit(self.cut_scenes[self.cut_scenes_played][self.cut_scene_time_elapsed // self.cut_scene_length[self.cut_scenes_played]], (0, 0))

        if self.cut_scene_time_elapsed % self.cut_scene_length[self.cut_scenes_played] <= self.fading_length:
            self.filter.fill((0, 0, 0, 255 - (self.cut_scene_time_elapsed % self.cut_scene_length[self.cut_scenes_played]) / self.fading_length * 255))

        if self.cut_scene_time_elapsed % self.cut_scene_length[self.cut_scenes_played] >= self.cut_scene_length[self.cut_scenes_played] - self.fading_length:
            self.filter.fill((0, 0, 0, (self.cut_scene_time_elapsed % self.cut_scene_length[self.cut_scenes_played] - (self.cut_scene_length[self.cut_scenes_played] - self.fading_length)) / self.fading_length * 255))

        win.blit(self.filter, (0, 0))

        self.cut_scene_time_elapsed += 1

        if self.cut_scene_time_elapsed == self.cut_scene_length[self.cut_scenes_played] * len(self.cut_scenes[self.cut_scenes_played]):
            self.filter.fill((0, 0, 0, 0))
            self.cut_scenes_played += 1
            self.cut_scene_time_elapsed = 0
            self.cut_scene_active = False

            if self.cut_scenes_played == 2:
                self.interactive_image_active = True
                self.current_interactive_image = 'end'
                self.interactions_made += 1


    def draw_interactive_image_active(self, click, mouse):
        match self.current_interactive_image:
            case 'lighting_candlestick':
                self.current_cursor_image = 1
                if click:
                    self.interactive_image_active = False
                    self.current_interactive_image = ''
                    self.skip_one_interact = True

                    self.monolog_visible = True
                    self.monolog_obj = classic_font.render('Je zamknutý. Je na ňom nejaký čudný nápis. Čo len môže znamenať?', False, font_color)
                    self.monolog_time = 6 * fps

                win.blit(falling_screen, (0, 0))

            case 'locked_trapdoors':
                if pygame.Rect.collidepoint(pygame.Rect(width * 0.03, width * 0.03, width * 0.1, height * 0.1), mouse): # toto že keď exitne
                    self.current_cursor_image = 1
                    if click:
                        self.current_interactive_image = ''
                        self.interactive_image_active = False
                        self.skip_one_interact = True

                for i in range(12):
                    if pygame.Rect.collidepoint(pygame.Rect(width * 0.125 * ((i % 6) + 1) + (i // 6) * width * 0.031, height * 0.241 + height * 0.252 * ((i // 6) + 1), width * 0.113, width * 0.113), mouse):
                        self.current_cursor_image = 1
                        if click:
                            self.current_emojis = self.current_emojis[1:]
                            self.current_emojis += chr(97 + i)

                            if self.current_emojis == self.right_emojis:
                                self.current_interactive_image = 'unlocked_trapdoors'
                                self.interactions_made += 1

                                self.text_visible = True
                                self.text_obj = classic_font.render('Otvoril si poklop.', False, font_color)
                                self.text_time = 3 * fps

                                self.monolog_visible = True
                                self.monolog_obj = classic_font.render('Super! Je tu sekera a nejaký list. Vyzerá byť starý...', False, font_color)
                                self.monolog_time = 6 * fps

                win.blit(locked_trapdoors_image, (0, 0))
                win.blit(arrow_back, (width * 0.03, width * 0.03))

            case 'unlocked_trapdoors':
                if pygame.Rect.collidepoint(pygame.Rect(width * 0.03, width * 0.03, width * 0.1, height * 0.1), mouse): # toto že keď exitne
                    self.current_cursor_image = 1
                    if click:
                        self.current_interactive_image = ''
                        self.interactive_image_active = False
                        self.skip_one_interact = True

                elif pygame.Rect.collidepoint(pygame.Rect(width * 0.22, height * 0.15, width * 0.2, width * 0.4), mouse): # sekera
                    if self.interactions_made == 10:
                        self.current_cursor_image = 1
                        if click:
                            self.interactions_made += 1
                            self.draw_axe = False

                            self.text_visible = True
                            self.text_obj = classic_font.render('Zobral si sekeru.', False, font_color)
                            self.text_time = 3 * fps
                
                elif pygame.Rect.collidepoint(pygame.Rect(width * 0.5, height * 0.15, width * 0.35, width * 0.4), mouse):
                    self.current_cursor_image = 1
                    if click:
                        self.current_interactive_image = 'diary'
                        if self.interactions_made == 5:
                            self.interactions_made += 1

                win.blit(unlocked_trapdoors_image, (0, 0))
                win.blit(arrow_back, (width * 0.03, width * 0.03))

                if self.draw_axe:
                    win.blit(axe, (width * 0.22, height * 0.15)) # sekera

            case 'chalice':
                self.current_cursor_image = 1
                if click:
                    self.interactive_image_active = False
                    self.current_interactive_image = ''
                    self.skip_one_interact = True

                win.blit(chalice_image, (0, 0))

            case 'diary':
                self.current_cursor_image = 1
                if click:
                    self.current_interactive_image = 'diary2'

                win.blit(diary1_image, (0, 0))

            case 'diary2':
                self.current_cursor_image = 1
                if click:
                    self.interactive_image_active = False
                    self.current_interactive_image = ''
                    self.skip_one_interact = True

                    if self.interactions_made == 6:
                        self.monolog_visible = True
                        self.monolog_obj = classic_font.render('Musím vrátiť ten poklad, komu patrí. Ale kto mi ukáže cestu? Veď židia tu už dlho nie sú!', False, font_color)
                        self.monolog_time = 6 * fps

                win.blit(diary2_image, (0, 0))

            case 'bible':
                self.current_cursor_image = 1
                if click:
                    self.interactive_image_active = False
                    self.current_interactive_image = ''
                    self.skip_one_interact = True
                
                win.blit(bible_image, (0, 0))

            case 'book':
                self.current_cursor_image = 1
                if click:
                    if self.interactions_made == 6:
                        self.interactions_made += 1

                        self.monolog_visible = True
                        self.monolog_obj = classic_font.render('Aké prikázania porušil? Musím ísť znova prečítať ten spis.', False, font_color)
                        self.monolog_time = 6 * fps

                    self.interactive_image_active = False
                    self.current_interactive_image = ''
                    self.skip_one_interact = True
                
                win.blit(jew_book_image, (0, 0))

            case 'organ':
                win.blit(organ_image, (0, 0))
                win.blit(arrow_back, (width * 0.03, width * 0.03))

                if pygame.Rect.collidepoint(pygame.Rect(width * 0.03, width * 0.03, width * 0.1, height * 0.1), mouse): # toto že keď exitne
                    self.current_cursor_image = 1
                    if click:
                        self.current_interactive_image = ''
                        self.interactive_image_active = False
                        self.skip_one_interact = True

                if self.interactions_made >= 9:
                    win.blit(restart_image, (width * 0.895, width * 0.0175))
                    if pygame.Rect.collidepoint(pygame.Rect(width * 0.895, width * 0.0175, width * 0.075, width * 0.075), mouse):
                        win.blit(click_to_play_again_text, (mouse[0] - width / 1280 * 55, mouse[1] + width / 1280 * 30))
                        self.current_cursor_image = 1
                        if click:
                            pass # zahra sa hudbicka znova

                for i in range(1, 9):
                    if pygame.Rect.collidepoint(pygame.Rect(width * 0.442 + width * 0.038 * i, height * 0.54, width * 0.028, height * 0.15), mouse):
                        self.current_cursor_image = 1
                        if click:
                            if self.interactions_made == 7:
                                self.organ_tones_played = self.organ_tones_played[1:]
                                self.organ_tones_played += str(i)

                                if self.organ_tones_played == self.right_organ_sound:
                                    self.interactive_image_active = False
                                    self.current_interactive_image = ''
                                    self.skip_one_interact = True

                                    self.text_visible = True
                                    self.text_obj = classic_font.render('Niečo vyletelo z jednej trubky organu.', False, font_color)
                                    self.text_time = 3 * fps

                                    self.interactions_made += 1

                                    # vyjde ti papierik
                                    self.items[self.current_room].append({
                                        'name': 'paper with minigame',
                                        'rect': pygame.Rect(width * 0.76, height * 0.36, width * 0.02, width * 0.02),
                                        'image': pygame.transform.scale(pygame.image.load('images/papier.png'), (width * 0.02, height * 0.02)),
                                        'when_interactable': 8,
                                        'interaction_message': 'Zobral si papierik zo zeme.',
                                        'replace_item': None,
                                        'in_background': False
                                    })

                                    self.animate_paper = True

            case 'paper with minigame':
                if pygame.Rect.collidepoint(pygame.Rect(width * 0.08, width * 0.035, width * 0.075, width * 0.075), mouse): # toto že keď restartne
                    self.current_cursor_image = 1
                    if click:
                        self.map = deepcopy(self.default_map)
                        self.num_of_moves_used = 0
                        self.num_of_moves_used_text = classic_font.render('Počet použitých krokov: ' + str(self.num_of_moves_used), False, font_color)

                elif pygame.Rect.collidepoint(pygame.Rect(width * 0.895, width * 0.0175, width * 0.075, width * 0.075), mouse):
                    self.current_cursor_image = 1
                    if click:
                        self.show_hint = True

                for y in range(len(self.map)):
                    for x in range(len(self.map[y])):
                        if pygame.Rect.collidepoint(pygame.Rect(height * 0.3 + height * 0.11 * x, height * 0.22 + height * 0.125 * y, height * 0.1, height * 0.1), mouse):
                            
                            self.current_cursor_image = 1

                            if click:
                                self.piece_selected

                                if self.map[y][x] != 0:
                                    self.piece_selected = {'pos': (x, y), 'type': self.map[y][x]}
                                else:
                                    if self.piece_selected != None and is_valid_move((x, y), self.piece_selected['pos'], self.map):
                                        self.map[self.piece_selected['pos'][1]][self.piece_selected['pos'][0]] = 0
                                        self.map[y][x] = self.piece_selected['type']
                                        self.piece_selected['pos'] = (x, y)

                                        self.num_of_moves_used += 1
                                        self.num_of_moves_used_text = classic_font.render('Počet použitých krokov: ' + str(self.num_of_moves_used), False, font_color)

                                        if self.map == self.right_map:
                                            if self.num_of_moves_used > self.optimal_num_of_moves:
                                                self.map = deepcopy(self.default_map)
                                                self.num_of_moves_used = 0
                                                self.num_of_moves_used_text = classic_font.render('Počet použitých krokov: ' + str(self.num_of_moves_used), False, font_color)

                                            else:
                                                self.interactive_image_active = False
                                                self.current_interactive_image = ''
                                                self.skip_one_interact = True

                                                self.text_visible = True
                                                self.text_obj = classic_font.render('Organ začal z ničoho nič hrať.', False, font_color)
                                                self.text_time = 3 * fps

                                                self.interactions_made += 1
                    
                win.blit(paper_minigame_image, (0, 0))

                for y in range(len(self.map)):
                    for x in range(len(self.map[y])):
                        if self.map[y][x] == 1:
                            pygame.draw.circle(win, font_color, (height * 0.3 + height * 0.11 * x + height * 0.05, height * 0.22 + height * 0.125 * y + height * 0.05), height * 0.03)
                        elif self.map[y][x] == 2:
                            pygame.draw.circle(win, (40, 40, 40), (height * 0.3 + height * 0.11 * x + height * 0.05, height * 0.22 + height * 0.125 * y + height * 0.05), height * 0.03)
                
                if self.show_hint:
                    pygame.draw.line(win, font_color, (height * 0.46, height * 0.22 + height * 0.125 * 4 + height * 0.05), (height * 0.46, height * 0.22 + height * 0.125 * 2 + height * 0.05), 3)
                    pygame.draw.line(win, (40, 40, 40), (height * 0.35, height * 0.22 + height * 0.125 * 0 + height * 0.05), (height * 0.35, height * 0.22 + height * 0.125 * 3 + height * 0.05), 3)
                    pygame.draw.line(win, (40, 40, 40), (height * 0.35, height * 0.22 + height * 0.125 * 3 + height * 0.05), (height * 0.45, height * 0.22 + height * 0.125 * 3 + height * 0.05), 3)
                    pygame.draw.line(win, (40, 40, 40), (height * 0.45, height * 0.22 + height * 0.125 * 3 + height * 0.05), (height * 0.45, height * 0.22 + height * 0.125 * 4 + height * 0.05), 3)

                win.blit(self.num_of_moves_used_text, (width * 0.65, height * 0.8))
                win.blit(restart_image, (width * 0.08, width * 0.035)) # toto bude repeat button
                win.blit(help_image, (width * 0.895, width * 0.0175)) # toto je help button

            case 'inside of altar':
                if pygame.Rect.collidepoint(pygame.Rect(width * 0.03, width * 0.03, width * 0.1, height * 0.1), mouse):
                    self.current_cursor_image = 1
                    if click:
                        self.interactive_image_active = False
                        self.current_interactive_image = ''
                        self.skip_one_interact = True

                win.blit(trezor_image, (0, 0))

                for i in range(9):
                    if pygame.Rect.collidepoint(pygame.Rect(width * 0.15 + (i % 3) * width * 0.125 - (1 if i > 2 and i < 6 else 0) * width * 0.027, height * 0.17 + (i // 3) * height * 0.25, width * 0.1, width * 0.12), mouse):
                        self.current_cursor_image = 1
                        if click:
                            
                            if len(self.current_pin) < 4:
                                self.current_pin += str(i + 1)

                                self.numbers_of_pin_objs[len(self.current_pin) - 1] = big_font.render(str(i + 1), False, font_color)

                if pygame.Rect.collidepoint(pygame.Rect(width * 0.59, height * 0.559, width * 0.1, width * 0.12), mouse):
                    self.current_cursor_image = 1
                    if click:
                        if self.current_pin == self.right_pin:
                            self.interactive_image_active = False
                            self.current_interactive_image = ''
                            self.skip_one_interact = True

                            self.cut_scene_active = True

                        else:
                            for i in range(4):
                                self.numbers_of_pin_objs[i] = big_font.render('', False, font_color)

                            self.current_pin = ''

                elif pygame.Rect.collidepoint(pygame.Rect(width * 0.59 + width * 0.125, height * 0.559, width * 0.1, width * 0.12), mouse):
                    self.current_cursor_image = 1
                    if click:
                        for i in range(4):
                            self.numbers_of_pin_objs[i] = big_font.render('', False, font_color)

                        self.current_pin = ''

                for i in range(len(self.numbers_of_pin_objs)):
                    win.blit(self.numbers_of_pin_objs[i], (width * 0.586 + i * width * 0.083, height * 0.174))

                win.blit(arrow_back, (width * 0.03, width * 0.03))

            case 'end':

                if pygame.Rect.collidepoint(pygame.Rect(width * 0.16, height * 0.54, width * 0.255, height * 0.2), mouse): # retry
                    self.current_cursor_image = 1
                    if click:
                        room_manager.__init__()
                        player.__init__()

                elif pygame.Rect.collidepoint(pygame.Rect(width * 0.59, height * 0.54, width * 0.255, height * 0.2), mouse): # exit
                    self.current_cursor_image = 1

                win.blit(end_image, (0, 0))

    def animate_item(self, item):
        item['rect'].y -= (self.total_animation_time / 4 - self.current_animation_time) / fps * 7 * self.total_animation_time / fps
        item['rect'].x -= 200 / fps

        if self.current_animation_time == self.total_animation_time:
            self.animate_paper = False

        self.current_animation_time += 1

    def return_current_interaction(self):
        return self.interactions_made

room_manager = RoomManager()
player = Player()