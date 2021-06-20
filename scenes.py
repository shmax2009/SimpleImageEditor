from Scene import Scene

import pygame
import settings
from pygame.font import Font

min = int(min(settings.coficient))
pygame.init()
font = Font('res/arial.ttf', int(20 * min / 1.5))
font_for_main_text = Font('res/arial.ttf', int(60 * min / 1.5))
font_for_heading = Font('res/arial.ttf', int(30 * min / 1.5))

# initialize start menu scene
start_menu = Scene('res/theme.json', "start menu")
start_menu.add_button((int(580 / 1.5), int(325 / 1.5)), (int(120 / 1.5), int(70 / 1.5)), "get started", font)
start_menu.add_text((int(640 / 1.5), int(240 / 1.5)), "", (0, 0, 0),
                    font_for_main_text)
# end initialize start menu scene

# initialize second menu scene
second_menu = Scene('res/theme.json', "second menu")
second_menu.add_button((int(480 / 1.5), int(325 / 1.5)), (int(120 / 1.5), int(70 / 1.5)), "choose photo", font)
second_menu.add_button((int(680 / 1.5), int(325 / 1.5)), (int(120 / 1.5), int(70 / 1.5)), "exit", font)
second_menu.add_text((int(620 / 1.5), int(225 / 1.5)), "Hi there,small photo editor for you is here", (0, 0, 0),
                     font_for_main_text)
# end initialize second menu scene

# initialize work scene
work_scene = Scene('res/theme.json', "work scene")
work_scene.add_button((int(165 / 1.5), int(600 / 1.5)), (int(150 / 1.5), int(90 / 1.5)), "Brightness", font)
work_scene.add_button((int(355 / 1.5), int(600 / 1.5)), (int(150 / 1.5), int(90 / 1.5)), "Set Color", font)
work_scene.add_button((int(550 / 1.5), int(600 / 1.5)), (int(150 / 1.5), int(90 / 1.5)), "Sharp", font)
work_scene.add_button((int(745 / 1.5), int(600 / 1.5)), (int(150 / 1.5), int(90 / 1.5)), "Contrast", font)
work_scene.add_button((int(1137 / 1.5), int(40 / 1.5)), (int(100 / 1.5), int(50 / 1.5)), "exit", font)
work_scene.add_button((int(940 / 1.5), int(600 / 1.5)), (int(150 / 1.5), int(90 / 1.5)), "save", font)
work_scene.add_toggle((0, 0), (30, 27), ("+", "-"), "toggle", font_for_main_text)
# end initialize work  scene

# initialize Brightness scene
brightness_scene = Scene('res/theme.json', "brightness scene")
brightness_scene.add_text((int(216 / 1.5), int(614 / 1.5)), "-", (0, 0, 0), font_for_heading)
brightness_scene.add_text((int(784 / 1.5), int(615 / 1.5)), "+", (0, 0, 0), font_for_heading)
brightness_scene.add_text((int(500 / 1.5), int(650 / 1.5)), "change brightness of the chosen photo", (0, 0, 0),
                          font_for_heading)
rect = pygame.Rect(int(200 / 1.5), int(600 / 1.5), int(600 / 1.5), int(30 / 1.5))
brightness_scene.add_slider(rect, "slider")
brightness_scene.add_button((int(915 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "exit", font)

# end initialize Brightness scene


# initialize Color scene
color_scene = Scene('res/theme.json', "color scene")
color_scene.add_text((int(216 / 1.5), int(614 / 1.5)), "-", (0, 0, 0), font_for_heading)
color_scene.add_text((int(784 / 1.5), int(615 / 1.5)), "+", (0, 0, 0), font_for_heading)
color_scene.add_text((int(500 / 1.5), int(650 / 1.5)), "change color saturation of the chosen photo", (0, 0, 0),
                     font_for_heading)
rect = pygame.Rect(int(200 / 1.5), int(600 / 1.5), int(600 / 1.5), int(30 / 1.5))
color_scene.add_slider(rect, "slider")
color_scene.add_button((int(915 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "exit", font)
# end initialize Color scene

# initialize Sharp scene
sharp_scene = Scene('res/theme.json', "sharp scene")
sharp_scene.add_text((int(216 / 1.5), int(614 / 1.5)), "-", (0, 0, 0), font_for_heading)
sharp_scene.add_text((int(784 / 1.5), int(615 / 1.5)), "+", (0, 0, 0), font_for_heading)
sharp_scene.add_text((int(500 / 1.5), int(650 / 1.5)), "change sharpness of the chosen photo", (0, 0, 0),
                     font_for_heading)
rect = pygame.Rect(int(200 / 1.5), int(600 / 1.5), int(600 / 1.5), int(30 / 1.5))
sharp_scene.add_slider(rect, "slider")
sharp_scene.add_button((int(915 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "exit", font)

# end initialize Sharp scene

# initialize Contrast scene
contrast_scene = Scene('res/theme.json', "contrast scene")
contrast_scene.add_text((int(216 / 1.5), int(614 / 1.5)), "-", (0, 0, 0), font_for_heading)
contrast_scene.add_text((int(784 / 1.5), int(615 / 1.5)), "+", (0, 0, 0), font_for_heading)
contrast_scene.add_text((int(500 / 1.5), int(650 / 1.5)), "change contrast of the chosen photo", (0, 0, 0),
                        font_for_heading)
rect = pygame.Rect(int(200 / 1.5), int(600 / 1.5), int(600 / 1.5), int(30 / 1.5))
contrast_scene.add_slider(rect, "slider")
contrast_scene.add_button((int(915 / 1.5), int(600 / 1.5)), (int(200 / 1.5), int(90 / 1.5)), "exit", font)

# end initialize Contrast scene
