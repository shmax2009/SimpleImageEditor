import pygame
import pygame_gui
import settings
from Toggle import Toggle


class Scene:
    def __init__(self, theme: str, name: str):
        self.name = name
        self.manager = pygame_gui.UIManager(settings.update((settings.Width, settings.Height)), theme)
        self.buttons = dict()
        self.texts = list()
        self.images = dict()
        self.sliders = dict()
        self.toggles = dict()

    def add_button(self, position: (int, int), size: (int, int), text: str, font_: pygame.font.Font):
        position_ = position
        rect = pygame.Rect(position, size)
        position = settings.update(position)
        size = settings.update(size)
        # print(position, size)
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(position, size),
            text="",
            manager=self.manager)

        self.add_text(rect.center, text, (0, 0, 0), font_)
        self.buttons[text] = button

    def add_text(self, position: (int, int), text: str, color: (int, int, int),
                 font: pygame.font.Font):
        position = settings.update(position)
        text_ = font.render(text, True, color)
        text_rect = text_.get_rect()
        text_rect.center = position

        self.texts.append((text_, text_rect))

    def add_image(self, path: str, position: (int, int), size: (int, int), name: str):
        position = settings.update(position)
        size = settings.update(size)
        # print(size)
        image = pygame.image.load(path)
        im_x, im_y = pygame.Surface.get_size(image)
        # print(im_x, im_y)
        fl_x, fl_y = (size)
        fl_x = min(im_x, fl_x)
        fl_y = min(im_y, fl_y)
        f_size = (fl_x, fl_y)
        image = pygame.transform.scale(image, f_size)
        x, y = position
        sx, sy = size
        x = x + (sx - fl_x) / 2
        y = y + (sy - fl_y) / 2
        position = (x, y)
        self.images[name] = (image, position)

    def add_slider(self, rect: pygame.Rect, name: str):
        rect.size = settings.update(rect.size)
        rect.left, rect.top = settings.update((rect.left, rect.top))
        slider = pygame_gui.elements.UIHorizontalSlider(rect, 100, (0, 200), manager=self.manager)
        self.sliders[name] = slider
        # slider.set_current_valu(50)

    def add_toggle(self, position: (int, int), size: (int, int), text: (str, str), name: str, font: pygame.font.Font):
        position = settings.update(position)
        size = settings.update(size)
        rect = pygame.Rect(position, size)
        toggle = Toggle(rect, text, manager=self.manager, font=font)
        self.toggles[name] = toggle

    def draw(self, window):
        for image in self.images.values():
            image_, pos = image
            window.blit(image_, pos)

        self.manager.draw_ui(window)

        for text in self.texts:
            text_, rect = text
            window.blit(text_, rect)

    def image_to_max_size(self, path: str, position: (int, int), size: (int, int), name: str):
        position = settings.update(position)
        size = settings.update(size)
        image = pygame.image.load(path)
        # im_x, im_y = pygame.Surface.get_size(image)
        image = pygame.transform.scale(image, size)
        self.images[name] = (image, position)


    def image_to_min_size(self, path: str, position: (int, int), size: (int, int), name: str):
        position = settings.update(position)
        size = settings.update(size)
        # print(size)
        image = pygame.image.load(path)
        im_x, im_y = pygame.Surface.get_size(image)
        # print(im_x, im_y)
        fl_x, fl_y = (size)
        fl_x = min(im_x, fl_x)
        fl_y = min(im_y, fl_y)
        f_size = (fl_x, fl_y)
        image = pygame.transform.scale(image, f_size)
        x, y = position
        sx, sy = size
        x = x + (sx - fl_x) / 2
        y = y + (sy - fl_y) / 2
        position = (x, y)
        self.images[name] = (image, position)