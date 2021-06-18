# TODO
'''
fix bug with display scailing
'''
import pygame
import pygame_gui
import easygui
import settings
from Scene import Scene
import shutil
from controller import Controller
import os
from ScreenSize import get_window

# -------initialize-------

controller_for_image = Controller()
pygame.init()

# --get display size--
wd, hd = get_window()
settings.coficient = (wd / settings.DisplayWidth, hd / settings.DisplayHeight)
# print(settings.coficient)
# wd, hd = 3840, 3400
settings.screen_cof = (wd / settings.Width, hd / settings.Height)
print(settings.screen_cof)
# --get display size--


pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode(settings.update((settings.Width, settings.Height)))
print(settings.update((settings.Width, settings.Height)))
background = pygame.Surface(settings.update((settings.Width, settings.Height)))
background.fill(pygame.Color('#72C1F2'))

scene = None
min = int(min(settings.coficient))
font = pygame.font.Font('res/arial.ttf', int(20 * min / 1.5))

# initialize start menu scene
start_menu = Scene('res/theme.json', "start menu")
start_menu.add_button((int(580 / 1.5), int(325 / 1.5)), (int(120 / 1.5), int(70 / 1.5)), "get started", font)
start_menu.add_text((int(620 / 1.5), int(225 / 1.5)), "Hi there,small photo editor for you is here!!!!!!", (0, 0, 0),
                    font)
# initialize start menu scene

# initialize second menu scene
second_menu = Scene('res/theme.json', "second menu")
second_menu.add_button((int(480 / 1.5), int(325 / 1.5)), (int(120 / 1.5), int(70 / 1.5)), "choose photo", font)
second_menu.add_button((int(680 / 1.5), int(325 / 1.5)), (int(120 / 1.5), int(70 / 1.5)), "exit", font)
second_menu.add_text((int(620 / 1.5), int(225 / 1.5)), "Hi there,small photo editor for you is here", (0, 0, 0), font)
# initialize second menu scene

# initialize work scene
work_scene = Scene('res/theme.json', "work scene")
work_scene.add_button((int(165 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "Brightness", font)
work_scene.add_button((int(415 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "Set Color", font)
work_scene.add_button((int(665 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "Sharp", font)
work_scene.add_button((int(915 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "exit", font)
work_scene.add_button((int(0 / 1.5), int(50 / 1.5)), (int(150 / 1.5), int(90 / 1.5)), "save", font)
# initialize work  scene

# initialize Brightness scene
brightness_scene = Scene('res/theme.json', "brightness scene")
rect = pygame.Rect(int(200 / 1.5), int(600 / 1.5), int(600 / 1.5), int(30 / 1.5))
brightness_scene.add_slider(rect, "slider")
brightness_scene.add_button((int(915 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "exit", font)

# initialize Brightness scene


# initialize Color scene
color_scene = Scene('res/theme.json', "color scene")
rect = pygame.Rect(int(200 / 1.5), int(600 / 1.5), int(600 / 1.5), int(30 / 1.5))
color_scene.add_slider(rect, "slider")
color_scene.add_button((int(915 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "exit", font)

# initialize Color scene

# initialize Sharp scene
sharp_scene = Scene('res/theme.json', "sharp scene")
rect = pygame.Rect(int(200 / 1.5), int(600 / 1.5), int(600 / 1.5), int(30 / 1.5))
sharp_scene.add_slider(rect, "slider")
sharp_scene.add_button((int(915 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "exit", font)
# initialize Sharp scene

scene = start_menu
clock = pygame.time.Clock()
is_running = True
image_path = ""
original_image_path = ""

# -------initialize-------
while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            original_image_path = ""
            if os.path.exists(image_path):
                os.remove(image_path)

            if os.path.exists("brightness." + image_path.split(".")[-1]):
                os.remove("brightness." + image_path.split(".")[-1])
            if os.path.exists("color." + image_path.split(".")[-1]):
                os.remove("color." + image_path.split(".")[-1])
            if os.path.exists("sharp." + image_path.split(".")[-1]):
                os.remove("sharp." + image_path.split(".")[-1])
            image_path = ""

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if scene.name == "start menu" and event.ui_element == scene.buttons["get started"]:
                    scene = second_menu

                if scene.name == "second menu" and event.ui_element == scene.buttons["choose photo"]:
                    # Open file:
                    original_image_path = (easygui.fileopenbox())
                    type = original_image_path.split(".")[-1]
                    f = open(".image." + type, "w+")
                    f.close()
                    shutil.copy(original_image_path, ".image." + type)
                    image_path = ".image." + type
                    print(image_path)
                    work_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    brightness_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    color_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    sharp_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    scene = work_scene
                if scene.name == "second menu" and event.ui_element == scene.buttons["exit"]:
                    is_running = False

                if scene.name == "work scene" and event.ui_element == scene.buttons["exit"]:
                    scene = second_menu
                    original_image_path = ""
                    if os.path.exists(image_path):
                        os.remove(image_path)

                    if os.path.exists("brightness." + image_path.split(".")[-1]):
                        os.remove("brightness." + image_path.split(".")[-1])
                    if os.path.exists("color." + image_path.split(".")[-1]):
                        os.remove("color." + image_path.split(".")[-1])
                    if os.path.exists("sharp." + image_path.split(".")[-1]):
                        os.remove("sharp." + image_path.split(".")[-1])
                    brightness_scene.sliders["slider"].set_current_value(100)
                    color_scene.sliders["slider"].set_current_value(100)
                    sharp_scene.sliders["slider"].set_current_value(100)
                    image_path = ""
                if scene.name == "work scene" and event.ui_element == scene.buttons["save"]:
                    shutil.copy(image_path, original_image_path)
                if scene.name == "work scene" and event.ui_element == scene.buttons["Brightness"]:
                    scene = brightness_scene
                if scene.name == "work scene" and event.ui_element == scene.buttons["Set Color"]:
                    scene = color_scene
                if scene.name == "work scene" and event.ui_element == scene.buttons["Sharp"]:
                    scene = sharp_scene
                if scene.name == "brightness scene" and event.ui_element == scene.buttons["exit"]:
                    shutil.copy("brightness." + image_path.split(".")[-1], ".image." + image_path.split(".")[-1])
                    work_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    color_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    sharp_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    scene = work_scene

                if scene.name == "color scene" and event.ui_element == scene.buttons["exit"]:
                    shutil.copy("color." + image_path.split(".")[-1], ".image." + image_path.split(".")[-1])
                    work_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    brightness_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    sharp_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    scene = work_scene
                if scene.name == "sharp scene" and event.ui_element == scene.buttons["exit"]:
                    shutil.copy("sharp." + image_path.split(".")[-1], ".image." + image_path.split(".")[-1])
                    work_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    brightness_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    color_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    scene = work_scene
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if scene.name == "brightness scene" and event.ui_element == scene.sliders["slider"]:
                    controller_for_image.apply_brighten(image_path, scene.sliders["slider"].current_value)
                    scene.add_image("brightness." + image_path.split(".")[-1], settings.Image_position,
                                    settings.Image_scale, "image")
                if scene.name == "color scene" and event.ui_element == scene.sliders["slider"]:
                    controller_for_image.apply_color(image_path, scene.sliders["slider"].current_value)
                    scene.add_image("color." + image_path.split(".")[-1], settings.Image_position,
                                    settings.Image_scale, "image")
                if scene.name == "sharp scene" and event.ui_element == scene.sliders["slider"]:
                    controller_for_image.apply_sharpness(image_path, scene.sliders["slider"].current_value)
                    scene.add_image("sharp." + image_path.split(".")[-1], settings.Image_position,
                                    settings.Image_scale, "image")
        scene.manager.process_events(event)

    scene.manager.update(time_delta)
    # -------draw-------

    window_surface.blit(background, (0, 0))
    scene.draw(window_surface)

    # -------draw-------

    pygame.display.update()
