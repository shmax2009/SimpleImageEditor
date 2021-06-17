import pygame
import pygame_gui
import settings


class Scene:
    def __init__(self, theme: str, name: str):
        self.name = name
        self.manager = pygame_gui.UIManager((settings.Width, settings.Height), theme)
        self.buttons = dict()
        self.texts = list()
        self.images = dict()

    def add_button(self, position: (int, int), size: (int, int), text: str):
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(position, size),
                                              text=text,
                                              manager=self.manager)
        self.buttons[text] = button

    def add_text(self, position: (int, int), text: str, color: (int, int, int),
                 font: pygame.font.Font):
        text_ = font.render(text, True, color)
        textRect = text_.get_rect()
        textRect.center = position

        self.texts.append((text_, textRect))

    def add_image(self, path: str, position: (int, int), size: (int, int), name: str):
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, size)
        self.images[name] = (image, position)

    def draw(self, window):
        self.manager.draw_ui(window)
        for text in self.texts:
            text_, rect = text
            window.blit(text_, rect)

        for image in self.images.values():
            image_, pos = image
            window.blit(image_, pos)
