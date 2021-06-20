import pygame
from pygame_gui.elements.ui_button import UIButton
from pygame_gui.ui_manager import IUIManagerInterface
from pygame_gui.core.ui_element import UIElement


class Button(UIButton):
    def __init__(self, relative_rect: pygame.Rect, text: str, manager: IUIManagerInterface, font: pygame.font.Font):
        super(Button, self).__init__(relative_rect, "", manager)

