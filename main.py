import pygame
import pygame_gui
import easygui
import settings
from Scene import Scene

# -------initialize-------

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((settings.Width, settings.Height))

background = pygame.Surface((settings.Width, settings.Height))
background.fill(pygame.Color('#72C1F2'))

scene = None

font = pygame.font.Font('res/arial.ttf', 20)

# initialize start menu scene
start_menu = Scene('res/theme.json', "start menu")
start_menu.add_button((580, 325), (120, 70), "get started")
start_menu.add_text((620, 225), "Hi there,small photo editor for you is here", (0, 0, 0), font)
# initialize start menu scene


# initialize second menu scene
second_menu = Scene('res/theme.json', "second menu")
second_menu.add_button((480, 325), (120, 70), "choose photo")
second_menu.add_button((680, 325), (120, 70), "exit")
second_menu.add_text((620, 225), "Hi there,small photo editor for you is here", (0, 0, 0), font)
# initialize second menu scene

# initialize work scene
work_scene = Scene('res/theme.json', "work scene")
work_scene.add_button((165, 600), (200, 90), "Brightness")
work_scene.add_button((415, 600), (200, 90), "Blur")
work_scene.add_button((665, 600), (200, 90), "Adge")
work_scene.add_button((915, 600), (200, 90), "exit")
# initialize work  scene


scene = start_menu
clock = pygame.time.Clock()
is_running = True
# -------initialize-------
while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if scene.name == "start menu" and event.ui_element == scene.buttons["get started"]:
                    scene = second_menu

                if scene.name == "second menu" and event.ui_element == scene.buttons["choose photo"]:
                    # Open file:
                    image_path = (easygui.fileopenbox())
                    work_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    scene = work_scene
                if scene.name == "second menu" and event.ui_element == scene.buttons["exit"]:
                    is_running = False

                if scene.name == "work scene" and event.ui_element == scene.buttons["exit"]:
                    scene = second_menu
        scene.manager.process_events(event)

    scene.manager.update(time_delta)
    # -------draw-------

    window_surface.blit(background, (0, 0))
    scene.draw(window_surface)

    # -------draw-------

    pygame.display.update()
