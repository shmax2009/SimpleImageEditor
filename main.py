import pygame
import pygame_gui
import easygui
import settings
import shutil
from controller import Controller
import os
from ScreenSize import get_window
from utils import Utils

# -------initialize-------

controller_for_image = Controller()
pygame.init()

# --get display size--
wd, hd = get_window()
settings.coficient = (wd / settings.DisplayWidth, hd / settings.DisplayHeight)
# --get display size--

from scenes import start_menu, second_menu, work_scene, brightness_scene, color_scene, sharp_scene, contrast_scene

pygame.display.set_caption('Small Photo Editor')
window_surface = pygame.display.set_mode(settings.update((settings.Width, settings.Height)))
print(settings.update((settings.Width, settings.Height)))
background = pygame.Surface(settings.update((settings.Width, settings.Height)))
background.fill(pygame.Color('#AA00FF'))

scene = None

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
            if os.path.exists("contrast." + image_path.split(".")[-1]):
                os.remove("contrast." + image_path.split(".")[-1])
            image_path = ""

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if scene.name == "start menu" and event.ui_element == scene.buttons["get started"]:
                    scene = second_menu

                if scene.name == "second menu" and event.ui_element == scene.buttons["choose photo"]:
                    # Open file:
                    original_image_path = (easygui.fileopenbox())
                    if (not Utils.check_file(original_image_path)):
                        continue
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
                    contrast_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
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
                    if os.path.exists("contrast." + image_path.split(".")[-1]):
                        os.remove("contrast." + image_path.split(".")[-1])

                    brightness_scene.sliders["slider"].set_current_value(100)
                    color_scene.sliders["slider"].set_current_value(100)
                    sharp_scene.sliders["slider"].set_current_value(100)
                    contrast_scene.sliders["slider"].set_current_value(100)
                    image_path = ""

                if scene.name == "work scene" and event.ui_element == scene.buttons["save"]:
                    shutil.copy(image_path, original_image_path)
                if scene.name == "work scene" and event.ui_element == scene.buttons["Brightness"]:
                    scene = brightness_scene
                if scene.name == "work scene" and event.ui_element == scene.buttons["Set Color"]:
                    scene = color_scene
                if scene.name == "work scene" and event.ui_element == scene.buttons["Sharp"]:
                    scene = sharp_scene
                if scene.name == "work scene" and event.ui_element == scene.buttons["Contrast"]:
                    scene = contrast_scene

                if scene.name == "work scene" and event.ui_element == scene.toggles["toggle"]:
                    if scene.toggles["toggle"].text == "-":
                        scene.image_to_max_size(image_path, settings.Image_position, settings.Image_scale, "image")
                        brightness_scene.image_to_max_size(image_path, settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_max_size(image_path, settings.Image_position, settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_max_size(image_path, settings.Image_position, settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_max_size(image_path, settings.Image_position, settings.Image_scale,
                                                      "image")
                    if scene.toggles["toggle"].text == "+":
                        scene.image_to_min_size(image_path, settings.Image_position, settings.Image_scale, "image")
                        brightness_scene.image_to_min_size(image_path, settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_min_size(image_path, settings.Image_position, settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_min_size(image_path, settings.Image_position, settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_min_size(image_path, settings.Image_position, settings.Image_scale,
                                                      "image")

                if scene.name == "brightness scene" and event.ui_element == scene.buttons["exit"]:
                    if os.path.exists("brightness." + image_path.split(".")[-1]):
                        shutil.copy("brightness." + image_path.split(".")[-1], ".image." + image_path.split(".")[-1])

                    work_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    color_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    sharp_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    contrast_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    scene = work_scene

                    if work_scene.toggles["toggle"].text == '-':
                        scene.image_to_max_size("brightness." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                        brightness_scene.image_to_max_size("brightness." + image_path.split(".")[-1],
                                                           settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_max_size("brightness." + image_path.split(".")[-1],
                                                      settings.Image_position, settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_max_size("brightness." + image_path.split(".")[-1],
                                                         settings.Image_position, settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_max_size("brightness." + image_path.split(".")[-1],
                                                      settings.Image_position, settings.Image_scale,
                                                      "image")
                    else:
                        scene.image_to_min_size("brightness." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                        brightness_scene.image_to_min_size("brightness." + image_path.split(".")[-1],
                                                           settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_min_size("brightness." + image_path.split(".")[-1],
                                                      settings.Image_position, settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_min_size("brightness." + image_path.split(".")[-1],
                                                         settings.Image_position, settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_min_size("brightness." + image_path.split(".")[-1],
                                                      settings.Image_position, settings.Image_scale,
                                                      "image")

                if scene.name == "color scene" and event.ui_element == scene.buttons["exit"]:
                    if os.path.exists("color." + image_path.split(".")[-1]):
                        shutil.copy("color." + image_path.split(".")[-1], ".image." + image_path.split(".")[-1])
                    work_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    brightness_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    sharp_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    contrast_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    scene = work_scene
                    if work_scene.toggles["toggle"].text == '-':
                        scene.image_to_max_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                        brightness_scene.image_to_max_size("color." + image_path.split(".")[-1],
                                                           settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_max_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_max_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                         settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_max_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")
                    else:
                        scene.image_to_min_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                        brightness_scene.image_to_min_size("color." + image_path.split(".")[-1],
                                                           settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_min_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_min_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                         settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_min_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")

                if scene.name == "sharp scene" and event.ui_element == scene.buttons["exit"]:
                    if os.path.exists("sharp." + image_path.split(".")[-1]):
                        shutil.copy("sharp." + image_path.split(".")[-1], ".image." + image_path.split(".")[-1])
                    work_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    brightness_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    color_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    contrast_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    scene = work_scene
                    if work_scene.toggles["toggle"].text == '-':
                        scene.image_to_max_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                        brightness_scene.image_to_max_size("sharp." + image_path.split(".")[-1],
                                                           settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_max_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_max_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                         settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_max_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")
                    else:
                        scene.image_to_min_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                        brightness_scene.image_to_min_size("sharp." + image_path.split(".")[-1],
                                                           settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_min_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_min_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                         settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_min_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")

                if scene.name == "contrast scene" and event.ui_element == scene.buttons["exit"]:
                    if os.path.exists("contrast." + image_path.split(".")[-1]):
                        shutil.copy("contrast." + image_path.split(".")[-1], ".image." + image_path.split(".")[-1])
                    work_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    brightness_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    color_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    sharp_scene.add_image(image_path, settings.Image_position, settings.Image_scale, "image")
                    scene = work_scene
                    if work_scene.toggles["toggle"].text == '-':
                        scene.image_to_max_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                        brightness_scene.image_to_max_size("contrast." + image_path.split(".")[-1],
                                                           settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_max_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_max_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                         settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_max_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")
                    else:
                        scene.image_to_min_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                        brightness_scene.image_to_min_size("contrast." + image_path.split(".")[-1],
                                                           settings.Image_position, settings.Image_scale,
                                                           "image")
                        color_scene.image_to_min_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")
                        contrast_scene.image_to_min_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                         settings.Image_scale,
                                                         "image")
                        sharp_scene.image_to_min_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                      settings.Image_scale,
                                                      "image")

            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if scene.name == "brightness scene" and event.ui_element == scene.sliders["slider"]:
                    controller_for_image.apply_brighten(image_path, scene.sliders["slider"].current_value)
                    scene.add_image("brightness." + image_path.split(".")[-1], settings.Image_position,
                                    settings.Image_scale, "image")
                    if work_scene.toggles["toggle"].text == '-':
                        scene.image_to_max_size("brightness." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                    else:
                        scene.image_to_min_size("brightness." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")

                if scene.name == "color scene" and event.ui_element == scene.sliders["slider"]:
                    controller_for_image.apply_color(image_path, scene.sliders["slider"].current_value)
                    scene.add_image("color." + image_path.split(".")[-1], settings.Image_position,
                                    settings.Image_scale, "image")
                    if work_scene.toggles["toggle"].text == '-':
                        scene.image_to_max_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                    else:
                        scene.image_to_min_size("color." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                if scene.name == "sharp scene" and event.ui_element == scene.sliders["slider"]:
                    controller_for_image.apply_sharpness(image_path, scene.sliders["slider"].current_value)
                    scene.add_image("sharp." + image_path.split(".")[-1], settings.Image_position,
                                    settings.Image_scale, "image")
                    if work_scene.toggles["toggle"].text == '-':
                        scene.image_to_max_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                    else:
                        scene.image_to_min_size("sharp." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                if scene.name == "contrast scene" and event.ui_element == scene.sliders["slider"]:
                    controller_for_image.apply_contrast(image_path, scene.sliders["slider"].current_value)
                    scene.add_image("contrast." + image_path.split(".")[-1], settings.Image_position,
                                    settings.Image_scale, "image")
                    if work_scene.toggles["toggle"].text == '-':
                        scene.image_to_max_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
                    else:
                        scene.image_to_min_size("contrast." + image_path.split(".")[-1], settings.Image_position,
                                                settings.Image_scale, "image")
        scene.manager.process_events(event)

    scene.manager.update(time_delta)
    # -------draw-------

    window_surface.blit(background, (0, 0))
    scene.draw(window_surface)

    # -------draw-------

    pygame.display.update()
